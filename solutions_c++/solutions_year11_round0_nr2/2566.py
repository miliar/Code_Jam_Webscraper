/**
	Copyright 2011 Wei Xueliang
**/
#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <map>
using namespace std;

int T;
int N;
string M;
map<string, char> mc;
map<string, char>::iterator it01;
short int md[128][128];
bool me[128];

int main() {
	cin >> T;
	string s;
	char c;
	for (int i = 1; i <= T; i++) {
		memset(md, 0, sizeof(md));
		memset(me, 0, sizeof(me));
		mc.clear();
		cin >> N;
		for (int j = 0; j < N; j++) {
			cin >> s;
			mc[ s.substr(0, 2) ] = s[2];
			string tmp1 = s.substr(1, 1) + s.substr(0, 1);
			mc[ tmp1 ] = s[2];
		}
		cin >> N;
		for (int j = 0; j < N; j++) {
			cin >> s;
			md[s[1]][0] += 1;
			md[s[1]][ md[s[1]][0] ] = s[0];

			//md[s[1]] = s[0];
			//md[s[0]] = s[1];

			md[s[0]][0] += 1;
			md[s[0]][ md[s[0]][0] ] = s[1];
		}
		cin >> N;
		cin >> s;
		string r = s.substr(0, 1);
		for (int j = 1; j < N; j++) {
			c = s[j];
			string tmp1;
			bool found = false;
			if (r.length() > 0) {
				tmp1 = r.substr(r.length() - 1, 1) + c;
				it01 = mc.find(tmp1);
				if (it01 != mc.end()) {
					r = r.substr(0, r.length() - 1) + (it01->second);
					found = true;
				}
			}
			bool can = false;
			if (found == false) {
				int pos = 999;
				for (int zz = 1; zz <= md[c][0]; zz++) {
					char c2 = md[c][zz];
					for (int k = r.length() - 1; k >= 0; k--) {
						if (r[k] == c2) {
							if (k < pos) {
								pos = k;
							}
							can = true;
							break;
						}
					}
				}
				if (can) {
					r = "";
				}
			}
			if (found == false && can == false) {
				r += c;
			}
		}
		cout << "Case #" << i << ": [";
		for (int zz = 0; zz < r.length(); zz++) {
			if (zz != 0) 
				cout << ", ";
			cout << r[zz];
		}
		cout << "]" << endl;
	}
}
