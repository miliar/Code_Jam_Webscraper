#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;

int main() {
//	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int cass=1; cass<=cas; ++cass) {
		int n, m;
		scanf("%d %d", &n, &m);
		set<string>exi;
		int res = 0;
		for (int i=0; i<n+m; ++i) {
			string s;
			cin >> s;
			int l=s.size();
			for (int j=l-1; j>0; --j) {
				if (j+1==l || s[j+1]=='/') {
					if (exi.find(s.substr(0, j+1))==exi.end()) {
						exi.insert(s.substr(0, j+1));
						if (i>=n) ++res;
					}
					else break;
				}
			}
		}
		printf("Case #%d: %d\n", cass, res);
	}


	return 0;
}