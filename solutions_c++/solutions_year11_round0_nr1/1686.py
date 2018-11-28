                                                                     
                                                                     
                                                                     
                                             
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

int i, j, k, m, n, l, d;
char ch;
int last[2], x[2], ans;

int main() {

//	freopen("x.in", "r", stdin);
//	freopen("x.out", "w", stdout);

//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tt, tn; cin >> tn;

	F1(tt,tn) {
              ans=0;
		printf("Case #%d: ", tt);
    cin >> n;
    x[0] = x[1] = 1;
    last[0] = last[1] = 0;
    F0(i,n) {
        
        cin >> ch >> d;
        if (ch == 'O') k = 0; else k = 1;
        // last[k] - x[k]
        // ans 
        
        ans = max(ans, abs(d-x[k])+last[k]) + 1;
        
        x[k] = d;
        last[k] = ans;       
    }
        
     
cout << ans;


		printf("\n");
	}
	
	return 0;
}
