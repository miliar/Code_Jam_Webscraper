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
	int L, D, N;
	cin >> L >> D >> N;
	vector<string> dict;
	for (int i=0;i<D;++i) {
		string s;
		cin >> s;
		dict.push_back(s);
	}

	for (int z=1;z<=N;++z) {
		string s;
		cin >> s;
		vector<set<char> > pat;
		for (int j=0;j<s.length();) {
			set<char> tmp;
			if (s[j]=='(') {
				++j;
				while ('a' <= s[j] && s[j] <= 'z') tmp.insert(s[j]), ++j;
				assert(s[j]==')');
				++j;
			}
			else tmp.insert(s[j]), ++j;
			pat.push_back(tmp);
		}

		int cnt = 0;
		for (int i=0;i<D;++i) if (dict[i].size() == pat.size()) {
			bool ok = 1;
			for (int j=0;j<pat.size();++j) {
				if (!pat[j].count(dict[i][j])) {
					ok = 0;
					break;
				}
			}
			if (ok) ++cnt;
		}
		printf("Case #%d: %d\n", z, cnt);
	}
}
