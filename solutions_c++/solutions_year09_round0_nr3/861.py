#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long ll;

string f = "welcome to code jam";
int n;
char s[512];
int d[512][32];
const int mod = 10000;

int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf ("%d\n", &n);
    REP (i, n)
    {
        gets (s);
        memset (d, 0, sizeof (d));
        int N = strlen (s);
        d[0][0] = 1;
        REP (j, N)
            REP (k, SZ (f))
            {
                d[j+1][k] += d[j][k];
                d[j+1][k] %= mod;
                if (f[k] == s[j])
                {
                    d[j+1][k+1] += d[j][k];
                    d[j+1][k+1] %= mod;
                }
            }       
        int res = 0;
        REP (j, N+1)
        {
            res += d[j][SZ (f)];
            res %= mod;
        }
        printf ("Case #%d: %04d\n", i+1, res);
    }    
	return 0;
}
