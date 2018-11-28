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
#define MAXN
using namespace std;
const int INF = 0x3f3f3f3f;
const double eps = 1e-9;
typedef long long LL;
typedef pair<int, int> pii;

int main() {
#ifndef ONLINE_JUDGE
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);
#endif

	int dataset;
	cin>>dataset;
	LL n, pd, pg;
	for (int cas = 1; cas <= dataset; ++cas) {
		cin>>n>>pd>>pg;
		bool ok = false;
		if (pd == 100) {
			if (pg > 0)
				ok = true;
		} else if (pg == 100) {
			if (pd == 100)
				ok = true;
		} else if (pd == 0) {
			ok = true;
		} else if (pg == 0) {
			if (pd == 0)
				ok = true;
		} else if(n>100){
			ok=true;
		} else {
			for (int i = 1; i <= n; ++i) {
				if ((i * pd) % 100 == 0) {
					ok = true;
					break;
				}
			}
		}

		printf("Case #%d: %s\n", cas, ok ? "Possible" : "Broken");
	}

	return 0;
}
