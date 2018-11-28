/*
 *  Created on: Sep 12, 2009
 *      Author: Ramesh Rajaby
 */

#include <algorithm>
#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		s = "0" + s;

		next_permutation(s.begin(), s.end());

		cout << "Case #" << i+1 << ": ";
		for (int j = (s[0]=='0'); j < s.length(); j++) {
			cout << s[j];
		} cout << endl;
	}
}

