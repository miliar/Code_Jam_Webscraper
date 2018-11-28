#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int t;
	cin >> t;
	string n;

	for (int c = 0; c < t; ++c) {
		cin >> n;
		
		//Read into a vector
		int len = n.size();
		int originallen = len;
		vector<char> digits(len);
		vector<char> original(len);
		for (int i = 0; i < len; i++) {
			digits[i] = n[i];
			original[i] = n[i];
		}

		//char nextchar = '0';
		bool done = false;
		bool first = true;
		string newnum;
		string minnum = "";
		while (!done) {
			do {
				newnum = "";
				for (int i = 0; i < len; i++) {
					newnum += digits[i];
				}

				if (digits[0] != '0' && (len > originallen || newnum > n)) {
					minnum = newnum;
					/*
					if (newnum < minnum || minnum == "") {
						minnum = newnum;
					}
					*/
					done = true;
					break;
				}
			} while (next_permutation(digits.begin(), digits.end()));

			if (done) {
				cout << "Case #" << (c+1) << ": " << minnum << endl;
			}
			else {
				//you need to add a digit
				//No!  you can only add 0's
				digits.insert(digits.begin(), '0');
				sort(digits.begin(), digits.end());
				//len = digits.size();
				len++;
			}
		}

	}
}