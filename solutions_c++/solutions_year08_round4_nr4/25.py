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

int i, j, k, m, n, l, i1, i2, ans, cur;
int a[20];
int d[20][20];
string s, p;

int q[16][16][1<<16];

void buildmat() {
	F0(i1,n) F0(i2,n) d[i1][i2] = 0;
	F0(i1,n) F0(i2,n) if (i1 != i2) {
		for (i = 0; i < m; i += n)
			d[i1][i2] += (s[i + i1] != s[i + i2]);
	}
}

int get(int v1, int v2, int mask) {
	if (mask == 0) return d[v1][v2];
	int &ret = q[v1][v2][mask];
	if (ret != -1) return ret;
	ret = inf;

	for (int i = 0; i < n; i++)
		if ((1<<i)&mask)
			ret = min(ret, d[v1][i] + get(i, v2, mask ^ (1<<i)));
	return ret;
}

int main() {

//	freopen("x.in", "r", stdin);

//	freopen("D-small-attempt0.in", "r", stdin);
//	freopen("D-small-attempt0fast.out", "w", stdout);

	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);

	int tt, tn; cin >> tn;

	F1(tt,tn) {
		printf("Case #%d: ", tt);
		ans = inf;

		cin >> n >> s;
		m = SZ(s);

		buildmat();
		memset(q, -1, sizeof(q));

		F0(i1,n) F0(i2,n) if (i1 != i2) {
			cur = 1;
			for (i = 0; i + n < m; i += n) {
				cur += (s[i + i2] != s[i + n + i1]);
			}
			cur += get(i1, i2, ((1<<n)-1)^(1<<i1)^(1<<i2));
			ans = min(ans, cur);
		}
		cout << ans;
		printf("\n");
	}
	
	return 0;
}
