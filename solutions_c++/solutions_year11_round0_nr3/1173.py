#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;


int bit_count(int c) {
	int n=0;
	while (c>>n) n++;
	return n;
}

int main() {
	int t;
	cin >> t;
	
	for (int i=0;i<t;i++) {
		int n;
		cin >> n;
		vector<int> candies;

		for (int j=0;j<n;j++) {
			int c;
			cin >> c;
			candies.push_back(c);
		}
		std::sort(candies.begin(),candies.end());

		int sean = 0;
		int sean_xor = 0;
		int pat_xor = 0;

		while (candies.size()>1) {
			int c = candies.back();
			candies.pop_back();
			sean += c;
			sean_xor ^= c;
		}
		pat_xor = candies.back();
		
		//	cout << "sean ": " << sean << endl;
		if (sean_xor^pat_xor) {
			cout << "Case #" << (i+1) << ": NO"  << endl;
		} else {
			cout << "Case #" << (i+1) << ": " << sean << endl;
		}
	
	}

	return 0;
}
