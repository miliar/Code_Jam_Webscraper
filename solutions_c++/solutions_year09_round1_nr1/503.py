#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <sstream>
#include <algorithm>
using namespace std;

string base (int n, int b) {
	string ret;
	while (n) {
		int k = n%b;
		if (0 <= k && k<= 9) ret += (k+48);
		else ret += (k+97);
		n /= b;
	}
	reverse(ret.begin(),ret.end());
	int i = 0;
	while (ret[i] == '0') {
		i++;
		if (i == ret.size()) break;
	}
	ret = ret.substr(i);
	if (ret == "") ret = "0";
	return ret;
}		

int square (string s) {
	int ret = 0;
	for (int i = 0; i < s.size(); i++) {
		if ('0' <= s[i] && s[i] <= '9') {
			ret += (s[i]-48)*(s[i]-48);
		} else {
			ret += (s[i]-87)*(s[i]-87);
		}
	}
	return ret;
}

bool happy (int n, int b) {
	for (int i = 0; i < 10; i++) {
		string s = base(n,b);
		int k = square(s);
		n = k;
		if (n == 1) return true;
	}
	return false;
}

int main () {

	int t;
	cin >> t;
	string tr;
	getline(cin,tr);

	for (int T = 1; T <= t; T++) {
	
		vector <int> ba;
		string s;
		getline(cin,s);
		stringstream ss(s);
		int b;
		while (ss >> b) {
			ba.push_back(b);
		}
		for (int i = 2; ; i++) {
			bool yes = true;
			for (int j = 0; j < ba.size(); j++) {
				if (!happy(i,ba[j])) {
					yes = false;
					break;
				}
			}
			if (yes) {
				cout << "Case #" << T << ": " << i << "\n";
				break;
			}
		}
	}
	return 0;
}
