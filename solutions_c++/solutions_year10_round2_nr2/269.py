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
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int cass=1; cass<=cas; ++cass) {
		int n, k, b, t;
		scanf("%d %d %d %d", &n, &k, &b, &t);
		int x[100], v[100];
		for (int i=0; i<n; ++i) scanf("%d", &x[i]);
		for (int i=0; i<n; ++i) scanf("%d", &v[i]);
		int res = 0;
		int cnt = 0;
		int tmp = 0;
		for (int i=n-1; i>=0; --i) {
			//cout << (b-x[i]+v[i]-1)/v[i] << endl;
			if ((b-x[i]+v[i]-1)/v[i]>t) ++res;
			else {
				++cnt;
				tmp += res;
			}
			if (cnt==k) break;
		}
		if (cnt<k) printf("Case #%d: IMPOSSIBLE\n", cass);
		else printf("Case #%d: %d\n", cass, tmp);
	}


	return 0;
}