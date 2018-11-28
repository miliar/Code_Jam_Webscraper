#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	for (int z=1;z<=ncases;++z) {
		int c;
		cin >> c;
		map<string, string> combine;
		set<string> oppose;
		for (int i=0;i<c;++i) {
			string s;
			cin >> s;
			combine[string(1,s[0]) + string(1,s[1])] = s.substr(2);
			combine[string(1,s[1]) + string(1,s[0])] = s.substr(2);
		}

		int d;
		cin >> d;
		for (int i=0;i<d;++i) {
			string s;
			cin >> s;
			oppose.insert(s);
		}

		int n;
		cin >> n;
		string s;
		cin >> s;

		string cur;
		for (int i=0;i<s.size();++i) {
			cur.push_back(s[i]);
			if (cur.size() >= 2) {
				string last2 = cur.substr(cur.size()-2);
				for (map<string,string>::iterator it = combine.begin(); it != combine.end(); ++it) {
					if (last2 == it->first) {
						cur = cur.substr(0, cur.size()-2);
						cur += it->second;
						break;
					}
				}
			}

			for (int j=0;j<cur.size();++j) {
				for (int k=0;k<cur.size();++k) if (j != k) {
					if (oppose.count(string(1,cur[j]) + string(1,cur[k]))) {
						cur.clear();
						goto done;
					}
				}
			}
done:;
		}

		printf("Case #%d: [", z);
		for (int i=0;i<cur.size();++i) {
			if (i != 0) printf(", ");
			printf("%c", cur[i]);
		}
		printf("]\n");
	}
}
