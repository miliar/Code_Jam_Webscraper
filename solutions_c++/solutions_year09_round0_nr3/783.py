#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
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
const double pi = acos(-1.0);
const int MOD = 10000;
int i, j, k, m, n, l, o;
char s[1000];
string h = "welcome to code jam";
int d[20][1000];

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int tt, tn; scanf("%d\n", &tn);
	m = SZ(h);
	F1(tt,tn) {
		gets(s);
		n = strlen(s);
		memset(d, 0, sizeof(d));
		d[0][0] = 1;
		int ans = 0;
		F1(i,m)	F1(j,n) {
			if (h[i-1] == s[j-1]) {
				F0(k,j)
					d[i][j] = (d[i][j] + d[i-1][k]) % MOD;
			}
			if (i == m) ans = (ans + d[i][j]) % MOD;
		}
		printf("Case #%d: %04d\n", tt, ans);
	}
	return 0;
}
