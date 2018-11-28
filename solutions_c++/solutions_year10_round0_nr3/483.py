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

int i, j, k, m, n, l;
ll ans, a[1005], Earn[1005];
char ss[1000002];

int Was[1005];

int main() {
//	freopen("c.in", "r", stdin);
//	freopen("c.out", "w", stdout);

//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("C-small-attempt0.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		ans = 0;

		cin >> m >> k >> n;
		F0(i,n) {
			cin >> a[i];
			Was[i] = 0;
		}

		j = 0;
		for (i = 1; 1; i++) {
			if (Was[j]) break;
			Was[j] = i;
			Earn[i] = 0;
			l = 0;
			while (l < n && Earn[i] + a[(j+l)%n] <= k) {
				Earn[i] += a[(j+l)%n];
				l++;
			}
			j = (j+l) % n;
		}
		if (m < Was[j]) {
			for (l = 1; l <= m; l++)
				ans += Earn[l];
		} else {
			for (l = 1; l < Was[j]; l++)
				ans += Earn[l];
			m -= (Was[j]-1);
			ll all = 0;
			for (l = Was[j]; l < i; l++)
				all += Earn[l];
			ans += (m / (i-Was[j])) * all;
			m %= (i-Was[j]);
			for (l = Was[j]; l < Was[j]+m; l++)
				ans += Earn[l];
		}
		printf("Case #%d: ", tt);
		cout << ans << endl;
	}
	
	return 0;
}
