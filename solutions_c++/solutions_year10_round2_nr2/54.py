#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
using namespace std;

#define sz 1011
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

#define pii complex<int>

ll dokad[sz];
ll x[sz];
ll v[sz];

void solve() {
    int n, k, b, t;
    scanf("%d%d%d%d", &n, &k, &b, &t);
    rep (i, n) scanf("%lld", &x[i]);
    rep (i, n) scanf("%lld", &v[i]);
    rep (i, n) dokad[i] = x[i] + v[i] * t;

    int cnt = 0;
    ford (i, n - 1, 0) {
        if (k > 0 && dokad[i] >= b) {
            k--;
            fo (g, i + 1, n - 1) cnt += dokad[g] < b;
        }
    }

    if (k > 0) printf("IMPOSSIBLE");
    else {
        printf("%d", cnt);
    }
}

int main(int argc, char ** argv) {
    //freopen("1.in","r",stdin); 
    //freopen("2.in","r",stdin); 
    //freopen("3.in","r",stdin); 

    //freopen("../B-small-attempt0.in","r",stdin);freopen("../B-small-attempt0.out","w",stdout);
    //freopen("../B-small-attempt1.in","r",stdin);freopen("../B-small-attempt1.out","w",stdout);
    //freopen("../B-small-attempt2.in","r",stdin);freopen("../B-small-attempt2.out","w",stdout);

    freopen("../B-large.in","r",stdin); freopen("../B-large.out","w",stdout);

    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
        cerr << "i" << " " << i << endl;
        printf("Case #%d: ", i);
        solve();
        printf("\n");
        fflush(stdout);
        cerr.flush();
    }
	return 0;
}

