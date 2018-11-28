#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <iomanip>
using namespace std;

#define SZ size()
#define PB push_back
#define B begin()
#define E end()
#define SORT(a) sort((a).B, (a).E)
#define REV(a) reverse((a).B, (a).E)
#define UNQ(a) (a).resize(unique((a).B, (a).E) - (a).B)
#define SUM(a) accumulate((a).B, (a).E, 0)
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(__typeof(a.B) i = a.B; i != a.E; i++)
#define SQR(x) ((x) * (x))
#define EUCL(x1, y1, x2, y2) (((x1) - (x2)) * ((x1) - (x2)) + ((y1) - (y2)) * ((y1) - (y2)))
#define MANH(x1, y1, x2, y2) (abs((x1) - (x2)) + abs((y1) - (y2)))
#define CROSS(x1, y1, x2, y2) ((x1) * (y2) - (y1) * (x2))
#define CROSS2(x1, y1, x2, y2, x0, y0) (((x1) - (x0)) * ((y2) - (y0)) - ((y1) - (y0)) * ((x2) - (x0)))
#define DOT(x1, y1, x2, y2) ((x1) * (x2) + (y1) * (y2))
#define DOT2(x1, y1, x2, y2, x0, y0) (((x1) - (x0)) * ((x2) - (x0)) + ((y1) - (y0)) * ((y2) - (y0)))
#define P(a, b) make_pair((a), (b))
#define F first
#define S second
#define DEBUG(a) cout << #a << ": " << (a) << endl;
#define DEBUG1D(a, x1, x2) { for(int _i = (x1); _i < (x2); _i++){ cout << a[_i] << " "; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << a[_i][_j] << " "; } cout << endl; } }

#define MOD 100003
#define MAXN 505

int C[MAXN + 1][MAXN + 1];
void doBinomial()
{
	for(int n = 0, k; n <= MAXN; n++){
		C[n][0] = C[n][n] = 1ULL;
		for(k = 1; k < n; k++){
			C[n][k] = C[n - 1][k] + C[n - 1][k - 1];
		}
		for(k = n + 1; k <= MAXN; k++){
			C[n][k] = 0LL;
		}
	}
}

int dp[MAXN][MAXN];
void doDP()
{
    FOR(n, 2, MAXN){
        dp[n][1] = 1;
        dp[n][n - 1] = 1;
        FOR(len, 2, n - 1){
            dp[n][len] = 0;
            FOR(l, 1, len){
                //cout << n << " " << len << " " << l << "  " << len - l - 1 << " " << n - len - 1 << endl;
                dp[n][len] += (int)(((long long)dp[len][l] * C[n - len - 1][len - l - 1]) % MOD);
                dp[n][len] %= MOD;
            }
        }
    }
    //DEBUG2D(dp, 0, 10, 0, 10);
}

int N, res;
void solve()
{
    res = 0;
    FOR(i, 1, N){
        res += dp[N][i];
        res %= MOD;
    }
    return;
}

int main()
{
    doBinomial();
    doDP();
    ifstream fin("C-small.in");
    ofstream fout("C-small.out");
    int _T;
    fin >> _T;
    for(int _t = 1; _t <= _T; _t++){
        // input
        fin >> N;
        // output
        solve();
        fout << "Case #" << _t << ": " << res << endl;
    }
    return 0;
}
