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

int n, m;
int a[256][256];
char c[256][256];

int dy[4] = {-1, 0, 0, 1};
int dx[4] = {0, -1, 1, 0};

int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    FOR (test, 1, t+1)
    {
        cin >> n >> m;
        REP (i, n)
            REP (j, m)
            {
                cin >> a[i][j];
                c[i][j] = 0;
            }
        char f = 'a';
        REP (i, n)
            REP (j, m)
            if (!c[i][j])
            {
                VPII v;
                v.pb (PII (j, i));
                char ch;
                while (true)
                {
                    int y = v.back().Y;
                    int x = v.back().X;
                    int mi = a[y][x];
                    int ty, tx;
                    REP (dir, 4)
                    {
                        int ny = y + dy[dir];
                        int nx = x + dx[dir];
                        if (ny < 0 || nx < 0 || nx >= m || ny >= n)
                            continue;
                        if (a[ny][nx] < mi)
                        {
                            mi = a[ny][nx];
                            ty = ny;
                            tx = nx;
                        }
                    }                    
                    if (mi == a[y][x])
                    {
                        ch = f++;
                        break;
                    }
                    if (c[ty][tx])
                    {
                        ch = c[ty][tx];
                        break;
                    }
                    v.pb (PII (tx, ty));
                }
                REP (k, SZ (v))
                    c[v[k].Y][v[k].X] = ch;
            }
        printf ("Case #%d:\n", test);
        REP (i, n)
        {
            REP (j, m)
            {
                if (j) printf (" ");
                printf ("%c", c[i][j]);
            }
            printf ("\n");
        }                
    }    
	return 0;
}
