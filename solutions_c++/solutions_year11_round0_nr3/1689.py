                                                                     
                                                                     
                                                                     
                                             
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

int i, j, k, m, n, l, d, ans;


int main() {

//	freopen("x.in", "r", stdin);
//	freopen("x.out", "w", stdout);

//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("C-small-attempt0.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int tt, tn; cin >> tn;

	F1(tt,tn) {
		printf("Case #%d: ", tt);
		
		k =0 ;
		ans = 0;
		d = 1000006;
		cin >> n;
		F0(i,n) {
                cin >> j;
                k ^= j;
                ans += j;
                if (j < d) d = j;
                }
                if (k != 0) cout << "NO";
                else cout << ans-d;

		printf("\n");
	}
	
	return 0;
}
