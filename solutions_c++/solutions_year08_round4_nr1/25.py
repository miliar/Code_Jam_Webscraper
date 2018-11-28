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

int i, j, k, m, n, l, ans, V;
int a[100001], ch[100001];

int op(int o, int x, int y) {
	if (o == 1) return x & y;
	return x | y;
}

int d[100001][2];

int get(int i, int v) {
	if (i > m) {
		if (v == a[i]) return 0; else return inf;
	}
	int i1, i2;

	int &ret = d[i][v];
	if (ret != -1) return ret;
	ret = inf;
	F0(i1,2) F0(i2,2) if (op(a[i], i1, i2) == v) {
		ret = min(ret, get(2*i, i1) + get(2*i+1, i2));
	}
	if (ch[i]) {
		F0(i1,2) F0(i2,2) if (op(1-a[i], i1, i2) == v) {
			ret = min(ret, get(2*i, i1) + get(2*i+1, i2) + 1);
		}
	}
	return ret;
}

int main() {

//	freopen("x.in", "r", stdin);

//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d: ", tt);
		memset(d, -1, sizeof(d));
		cin >> n >> V;
		m = (n-1) / 2;
		F1(i,n)
		if (i <= m) {
			cin >> a[i] >> ch[i];
		} else 
			cin >> a[i];
		ans = get(1, V);
		if (ans >= inf/2) printf("IMPOSSIBLE");
		else printf("%d", ans);
		
		printf("\n");
	}
	return 0;
}
