/*
 *  File: FreeCellStatistics.cpp
 *  ------------------
 *
 *  Created by Elina Robeva on 5/20/11.
 *
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <vector>
using namespace std;


int main() {
	freopen("/Users/erobeva/Downloads/A-large.in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAAAAout.txt", "w", stdout);
	
	int T;
	cin >> T;
	//cout << T;
	for(int i = 0; i < T; ++i) {
		long long N;
		cin >> N;
		int pd, pg;
		cin >> pd >> pg;
		int result = 0;
		if ((pg == 100 && pd < 100) || (pg == 0 && pd > 0)) {
			cout << "Case #" << i + 1 << ": Broken" << endl;
			continue;
		}
		int gcd = 1;
		if (pd % 4 == 0) {
			gcd *= 4;
		} else if (pd % 2 == 0) {
			gcd *= 2;
		}
		if(pd % 25 == 0) {
			gcd *= 25;
		} else if (pd % 5 == 0) {
			gcd *= 5;
		}
		int num = 100/gcd;
		if (N >= num) {
			result = 1;
		}
		if (result == 1) {
			cout << "Case #" << i + 1 << ": Possible" << endl;
		} else {
			cout << "Case #" << i + 1 << ": Broken" << endl;
		}	
	}
	
	return 0;
}
