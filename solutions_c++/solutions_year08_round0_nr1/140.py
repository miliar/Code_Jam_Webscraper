#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double eps = 1e-8;

int i, j, k, m, n, l, o, t, tt;

int Used[1001], CUsed;
char P[1001][1001], Q[1001][1001];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &t);
	for (tt = 1; tt <= t; tt++) {
		scanf("%d\n", &n);
		F0(i,n) gets(P[i]);
		scanf("%d\n", &m);
		F0(i,m) gets(Q[i]);
		int ans = 0;
		CUsed = 0;
		F0(i,n) Used[i] = 0;
		F0(i,m) {
			F0(j,n) if (strcmp(P[j], Q[i]) == 0) break;
			if (!Used[j]) { Used[j] = 1; CUsed++; }
			if (CUsed == n) {
				ans++;
				F0(k,n) Used[k] = 0;
				CUsed = 1;
				Used[j] = 1;
			}
		}
		printf("Case #%d: %d\n", tt, ans);
	}

	return 0;
}
