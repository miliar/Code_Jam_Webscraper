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
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l, ans;
int a[101][101], b[101][101];
int X1[1001], Y1[1001], X2[1001], Y2[1001];

int main() {
//	freopen("c.in", "r", stdin);

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

//	freopen("C-large.in", "r", stdin);
//	freopen("C-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		memset(a, 0, sizeof(a));
		cin >> n;
		F0(i,n) {
			cin >> X1[i] >> Y1[i] >> X2[i] >> Y2[i];
			for (j = X1[i]; j <= X2[i]; j++)
				for (k = Y1[i]; k <= Y2[i]; k++)
					a[j][k] = 1;
		}
		ans = 0;
		while (1) {
			int f = 0;
			F1(i,100) {
				F1(j,100) if (a[i][j]) f = 1;
			}
			if (!f) break;
			ans++;
			F1(i,100) F1(j,100) {
				if (!a[i][j])
					b[i][j] = (a[i-1][j] & a[i][j-1]);
				else 
					b[i][j] = (a[i-1][j] | a[i][j-1]);
			}
			F1(i,100) F1(j,100)
				a[i][j] = b[i][j];
		}

		printf("Case #%d: ", tt);

		cout << ans << endl;
	}
	
	return 0;
}
