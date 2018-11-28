#include <cstring>
#include <cstdio>
#include <string>
#include <map>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<string>c, o;
map<string, char>ha;
map<string, int>oa;
int main() {
	int T;
	int cas = 1;
	cin >> T;
	for (cas = 1; cas <= T; ++cas) {
		oa.clear();
		c.clear();
		o.clear();
		ha.clear();

		int cn, on;
		cin >> cn;
		for (int i = 0; i < cn; ++i) {
			string tmp;
			cin >> tmp;
			c.push_back(tmp);
			string cm = "";
			cm += tmp[0];
			cm += tmp[1];
			ha[cm] = tmp[2];

		}
		cin >>on;
		for (int i = 0; i < on; ++i) {
			string tmp;
			cin >> tmp;
			o.push_back(tmp);
			oa[tmp] = 1;
		}
		int len;
		string str;
		cin >> len;
		cin >> str;
		string now = "";
		now += str[0];
		for (int i = 1; i < len; ++i) {
			char c = str[i];
			while ( true ) {
				if ( now.size() == 0 ) {
					now += c;
					break;
				}
				string jiong = "";
				jiong += now[now.size() - 1];
				jiong += c; 
				if ( ha.find ( jiong ) == ha.end() ) {
					reverse (jiong.begin(), jiong.end() );
					if (ha.find(jiong) == ha.end() ) {
						now += c;
						break;
					} else {
						now = now.substr(0, now.size() - 1);
						c = ha[jiong];
					}
				} else {
					now = now.substr(0, now.size() - 1);
					c = ha[jiong];
					continue;
				}	
			}
			if ( now.size() > 1 ) {
				for (int j = 0; j < now.size() - 1; ++j) {
	//			for (int j = now.size() - 2; j >= 0; --j) {
					string ff = "";
					ff += now[j];
					ff += now[now.size() - 1];
					if ( oa.find(ff) == oa.end() ) {
						reverse(ff.begin(), ff.end());
						if ( oa.find (ff) == oa.end()) {
							continue;
						} else {
					//		now = now.substr(0,j);
							now = "";
							break;
						}
					} else {
						now = "";
					//	now = now.substr(0, j);
						break;
					}
				}
			}
		}
		printf("Case #%d: [", cas);
		for (int i = 0; i < now.size(); ++i) {
			if (i) printf(", ");
			printf("%c", now[i]);
		}
		printf("]\n");
	}
	return 0;
}
