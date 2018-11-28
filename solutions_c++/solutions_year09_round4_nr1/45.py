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
char ss[1000];
int d[1000], ans;

int main() {
//	freopen("x.in", "r", stdin);

//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d: ", tt);
		cin >> n; gets(ss);
		F1(i,n) {
			gets(ss);
			d[i] = 0;
			F0(j,n) if (ss[j] == '1') d[i] = max(d[i], j+1);
		}
		ans = 0;
		F1(i,n) {
			for (j = i; j <= n; j++) if (d[j] <= i) break;
			for (k = j; k > i; k--) {
				swap(d[k], d[k-1]);
				ans++;
			}
		}
		
		cout << ans << endl;
	}
	
	return 0;
}
