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
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << "i" << " " << #x << " " << x << endl; cerr.flush(); } }

#define pii complex<int>


const int sz = 503;
#define MOD ((int)(100003))
ll dp[sz + 11][sz + 11];
ll sol[sz + 11];

ll dw[sz + 11][sz + 11];

void init() {
    dw[0][0] = 1;
    rep (i, sz) {
        if (i % 16 == 0) cerr << i << endl;
        rep (j, sz) {
            if (i && j) dw[i][j] += dw[i-1][j-1];
            if (i) dw[i][j] += dw[i-1][j];
            dw[i][j] %= MOD;
        }
    }
    db(dw[5][2]<<" "<<dw[5][1]);
    // len dlugosc
    fo (i, 2, sz) { // ma i
        fo (ma, 1, i - 1) {
            if (ma == 1) {
                dp[i][ma]++;
                dp[i][ma] %= MOD;
            }
            else {
                fo (nma, 1, ma - 1) {
                    int pi = ma;
                    //fo (pi, 2, i - 1) {
                        int miedzy = i - pi - 1;
                        if (dp[pi][nma] > 0) {
                            int miedzy2 = (ma - 1) - nma;
                            dp[i][ma] += dp[pi][nma] * dw[miedzy][miedzy2];
                            dp[i][ma] %= MOD;
                        }
                   // }
                }
            }
            sol[i] += dp[i][ma];
            sol[i] %= MOD;
        }
    }
}

void solve() {
    int x;
    scanf("%d", &x);
    printf("%lld", ((sol[x] % MOD) + MOD) % MOD);

}

int main(int argc, char ** argv) {
    init();
    cerr<<clock()<<endl;
    //freopen("1.in","r",stdin); 
    //freopen("2.in","r",stdin); 
    //freopen("3.in","r",stdin); 

    //freopen("../C-small-attempt0.in","r",stdin);freopen("../C-small-attempt0.out","w",stdout);
    //freopen("../C-small-attempt1.in","r",stdin);freopen("../C-small-attempt1.out","w",stdout);
    //freopen("../C-small-attempt2.in","r",stdin);freopen("../C-small-attempt2.out","w",stdout);

    freopen("../C-large.in","r",stdin); freopen("../C-large.out","w",stdout);

    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
        cerr << __LINE__ << " " << i << endl;
        printf("Case #%d: ", i);
        solve();
        printf("\n");
        fflush(stdout);
        cerr.flush();
    }
	return 0;
}

