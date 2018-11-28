#include <iostream>
#include <set>


using namespace std;


//
// Main Function
//

int main()
{
	// Obtain the number of test cases
	int T;
	cin >> T;
	
	// Handle each test case
	for (int i = 0; i < T; i++) {
		
		// Obtain N, L and H
		int N;
		unsigned long long L, H;
		cin >> N;
		cin >> L;
		cin >> H;
		
		// Obtain the frequencies for the other instruments
		set<unsigned long long> freqSet;
		for (int j = 0; j < N; j++) {
			unsigned long long freq;
			cin >> freq;
			freqSet.insert(freq);
		}
		
		// Use brute force search to find the desired frequency
		// (such approach is feasible on small input sets and small ranges)
		bool looking = true;
		unsigned long long freq = L;
		while ((looking) && (freq <= H)) {
			bool good = true;
			set<unsigned long long>::iterator it   = freqSet.begin();
			set<unsigned long long>::iterator stop = freqSet.end();
			while ((good) && (it != stop)) {
				unsigned long long otherFreq = *it;
				if (freq > otherFreq) {
					if (freq % otherFreq != 0)
						good = false;
				}
				else if (freq < otherFreq) {
					if (otherFreq % freq != 0)
						good = false;
				}
				it++;
			}
			if (good) {
				looking = false;
				break;
			}
			else
				freq++;
		}
		
		cout << "Case #" << i + 1 << ": ";
		if (!looking)
			cout << freq << endl;
		else
			cout << "NO" << endl;
	}
	
	return 0;
}
