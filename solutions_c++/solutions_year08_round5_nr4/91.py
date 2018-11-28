#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

const int MOD = 10007;
int i, j, k, m, n, l, ans;
int a[105][105];
bool f[105][105];

int main() {

//	freopen("x.in", "r", stdin);

	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

//	freopen("D-large.in", "r", stdin);
//	freopen("D-large.out", "w", stdout);

	int tt, tn; cin >> tn;

	F1(tt,tn) {
		printf("Case #%d: ", tt);
		cin >> m >> n >> k;
		F1(i,m) F1(j,n) f[i][j] = true;
		memset(a, 0, sizeof(a));
		while (k--) {
			cin >> i >> j;
			f[i][j] = false;
		}
		a[1][1] = 1;
		F1(i,m) F1(j,n) if (i*j != 1 && f[i][j]) {
			a[i][j] = 0;
			if (i-1>= 1 && j-2>=1) a[i][j] += a[i-1][j-2];
			if (i-2>= 1 && j-1>=1) a[i][j] += a[i-2][j-1];
			a[i][j] %= MOD;
		}
		printf("%d\n", a[m][n]);
	}
	
	return 0;
}
