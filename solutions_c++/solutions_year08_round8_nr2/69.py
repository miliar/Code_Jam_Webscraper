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
#include <bitset>
#include <ext/hash_map>
#include <ext/hash_set>

using namespace std;
using namespace __gnu_cxx;

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

int d[512][512];
PII a[512];
int b[512];
int go[512][512];
int use[512][512];

int main() {
	freopen("B-small-attempt3.in", "r", stdin);
//	freopen("B-large.in", "r", stdin);
	freopen("B-small-attempt3.out", "w", stdout);
//	freopen("B-large.out", "w", stdout);

//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	
    int ntest;
    cin >> ntest;
    REP (test, ntest)
    {
                
        cout << "Case #" << (test+1) << ": ";
        
        int n;
        cin >> n;
        
        string col;
        map <string, int> cols;
        
        REP (i, n)
        {
            cin >> col >> a[i].X >> a[i].Y;
            if (cols.count (col))
                b[i] = cols[col];
            else
            {
                cols[col] = SZ (cols) - 1;
                b[i] = cols[col];
            }
        }
        
        int m = SZ (cols);
        REP (i, n)
        {
            REP (j, m)
                go[i][j] = -1;
            
            REP (j, n)
            if (a[j].X <= a[i].Y+1 && a[j].Y > a[i].Y)   
            {         
                go[i][b[j]] = max (go[i][b[j]], a[j].Y);
                use[i][b[j]] = j;
            }
        }
/*        REP(i, n)
        {
            REP (j, m)
            {
                cout << go[i][j] << ' ';
            }
            cout << endl;
        }*/

        REP (i, n)
            REP (j, m+1)
                d[i][j] = INF;
                
        REP (i, n)
        if (a[i].X == 1)
            d[i][m] = 1;


        VPII t;
        REP (i, n)
            t.pb (PII (a[i].Y, i));
        SORT (t);
        int res = INF;
        REP (ii, n)
        {
            int i = t[ii].Y;
            REP (j, m+1)
                if (d[i][j] != INF)
                {
                    if (a[i].Y >= 10000)
                    {
                        res = min (res, d[i][j]);
                        continue;
                    }
                    if (d[i][j] >= res)
                        continue;
                    if (go[i][b[i]] != -1)
                        d[use[i][b[i]]][j] = min (d[use[i][b[i]]][j], d[i][j] + 1);
                    if (j != m && go[i][j] != -1)
                        d[use[i][j]][b[i]] = min (d[use[i][j]][b[i]], d[i][j] + 1);
                        
                    REP (q, m)
                        if (q != b[i] && q != j && go[i][q] != -1)
                        {
                            if (j == m)
                                d[use[i][q]][b[i]] = min (d[use[i][q]][b[i]], d[i][j] + 1);
                            else
                            {
                                int u = use[i][q];
                                
                                int how = d[i][j] + 1;
                                while (a[u].Y != 10000)
                                {
                                    static int f;
                                    f = max (max (go[u][b[i]], go[u][j]), go[u][q]);
                                    if (f == -1)
                                    {
                                        how = INF;
                                        break;
                                    }
                                    how++;
                                    if (f == go[u][b[i]])
                                        u = use[u][b[i]];
                                    else
                                        if (f == go[u][j])
                                            u = use[u][j];
                                        else
                                            u = use[u][q];
                                }
                                
                                res <?= how;
                            }
                        }
                }  
            }
        if (res >= INF)
            cout << "IMPOSSIBLE" << endl;
        else        
            cout << res << endl;        
    }
	return 0;
}
