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

int i, j, k, m, l, ans;
ll n;

int isc[1000001];

int main() {
//	freopen("c.in", "r", stdin);

//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("C-small-attempt0.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	for (i = 2; i <= 1000; i++)
		if (!isc[i]) {
			for (j = i*i; j <= 1000000; j+=i)
				isc[j] = 1;
		}

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d: ", tt);
		cin >> n;

		ans = 0;

		if (n == 1) ans = -1;
		
		for (ll i = 2; i * i <= n; i++)
			if (!isc[i]) {
				ll s = i;
				while (s * i <= n) {
					s *= i;
					ans++;
				}
			}

		cout << ans+1 << endl;
	}
	
	return 0;
}
