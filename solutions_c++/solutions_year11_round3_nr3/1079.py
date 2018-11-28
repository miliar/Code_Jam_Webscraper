#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <cstring>
using namespace std;

int main()
{
	int c;
	cin >> c;
	for (int i = 0; i < c; i++) {
		int N, L, H;
		cin >> N >> L >> H;
		vector<int> freqs;

		for (int j = 0; j < N; j++) {
			int freq;
			cin >> freq;
			freqs.push_back(freq);
		}

		int result = -1;
		for (int f = L; f <= H && result == -1; f++) {
			bool found = true;
			for (int j = 0; j < freqs.size() && found; j++) {
				if (freqs[j] % f != 0 && f % freqs[j] != 0)
					found = false;
			}
			if (found)
				result = f;
		}

		cout << "Case #" << i+1 << ": ";
		if (result == -1)
			cout << "NO";
		else
			cout << result;
		cout << endl;
	}
}
