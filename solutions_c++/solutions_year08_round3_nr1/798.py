#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
#include <list>

using namespace std;

int process_case () {
	int P, K, L;
	cin >> P >> K >> L;
	vector<int> freq;
	freq.reserve(L);
	for (int i=0; i<L; i++){
		cin >> freq[i];
	}
	sort(freq.begin(), freq.begin() + L);
	int k=0;
	int press=0;
	for (int i=0; i<L; i++){
		if ((i%K)==0) {
			k++;
		}
		press += freq[L-1-i]*k;	
	}
	return press;
}

int main() {
	int n;
	cin >> n;
	for (int i=0; i<n; i++){
		cout << "Case #" << i+1 << ": " << process_case() << endl;
	}
	return 0;
}
