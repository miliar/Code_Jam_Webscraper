#include <iostream>
#include <stdlib.h>
#include <vector>
#include <string.h>
using namespace std;


int main() {
	int testcases;
	cin >> testcases;
	for (int tc=0;tc<testcases;tc++) {
		int N;
		cin >> N;

		int val = 0;
		int mval = 100000000;
		int sum = 0;
		for (int i=0;i<N;i++) {
			int curr;
			cin >> curr;
			val = val ^ curr;
			mval = min(mval,curr);
			sum += curr;
		}
		
		cout << "Case #" << (tc+1) << ": ";
		if (val!=0) {
			cout << "NO\n";
		} else {
			cout << (sum-mval) << "\n";
		}
	}
}