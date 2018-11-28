#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <ctime>
#define MAXN 128
using namespace std;
const int INF = 0x3f3f3f3f;
const double eps = 1e-9;
typedef long long LL;
typedef pair<char, char> pcc;

int c, d, n;
char str[103];
vector<pcc> chg[MAXN];
vector<char> clr[MAXN];

char change(char a, char b) {
	for (int i = chg[(int) a].size() - 1; i >= 0; --i) {
		if (chg[(int) a][i].first == b)
			return chg[(int) a][i].second;
	}
	return 0;
}

bool clear(char a, char b) {
	for (int i = clr[(int) a].size() - 1; i >= 0; --i) {
		if (clr[(int) a][i] == b)
			return true;
	}
	return false;
}

int main() {
#ifndef ONLINE_JUDGE
//	freopen("in", "r", stdin);
//    freopen("out", "w", stdout);
#endif

	int dataset;
	char x, y, z;
	scanf("%d", &dataset);
	for (int cas = 1; cas <= dataset; ++cas) {
		for (int i = 0; i < MAXN; ++i) {
			chg[i].clear();
			clr[i].clear();
		}

		scanf("%d", &c);
		for (int i = 0; i < c; ++i) {
			scanf(" %c %c %c", &x, &y, &z);
			chg[(int) x].push_back(make_pair(y, z));
			chg[(int) y].push_back(make_pair(x, z));
		}

		scanf("%d", &d);
		for (int i = 0; i < d; ++i) {
			scanf(" %c %c", &x, &y);
			clr[(int) x].push_back(y);
			clr[(int) y].push_back(x);
		}

		scanf("%d", &n);
		int sz = 0;
		for (int i = 0; i < n; ++i) {
			scanf(" %c", &x);
			bool done=false;
			if (sz) {
				z = change(str[sz - 1], x);
				if (z) {
					str[sz - 1] = z;
					done=true;
				}
			}

			for (int j = 0; j < sz && !done; ++j) {
				if (clear(str[j], x)) {
					sz = 0;
					done=true;
				}
			}

			if(!done)
				str[sz++]=x;
		}

		printf("Case #%d: [", cas);
		if(sz) {
			printf("%c", str[0]);
			for(int i=1; i<sz; ++i) {
				printf(", %c", str[i]);
			}
		}
		printf("]\n");
	}

	return 0;
}
