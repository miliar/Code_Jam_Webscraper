
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;

#define maxn 105
int dp[maxn][maxn];
int sum[maxn];
int cas, n, s, p;
int main() {
    cin >> cas;
    fup(c, 1, cas) {
        CLR(dp);
        cin >> n >> s >> p;
        fup(i, 1, n) cin >> sum[i];
        fup(i, 1, n) {
            fup(a, 0, 10) {
                fup(b, a, min(a + 2, 10)) {
                    int c = sum[i] - a - b;
                    if (c < 0 || c > 10 || c < b || c - a > 2) continue;
                    fup(k, 0, i) {
                        int nk;
                        if (c - a == 2) nk = k + 1;  
                        else nk = k;
                        int x = dp[i - 1][k];
                        if (c >= p) x++; 
                        dp[i][nk] = max(dp[i][nk], x);
                    }
                }
            }
        }
        printf("Case #%d: %d\n", c, dp[n][s]);
    }

	return 0;
}

