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
string s[12];

int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

struct ds
{
    vector <int> p;
    int n;
    ds (int n)
    {     
        ds::n = n;   
        REP (i, n)
            p.pb (i);
    }    
    int findset (int x)
    {
        while (x != p[x]) 
        {
            x = p[x];
        }
        return x;
    }
    void join (int x, int y)
    {
        x = findset (x);
        y = findset (y);
        p[x] = y;
    }
    bool connected ()
    {        
        FOR (i, 1, n)
            if (findset (0) != findset (i))
                return false;
        return true;
    }
};

bool is_connected (VPII & a)
{
    ds R (SZ (a));
    REP (i, SZ (a))
        REP (j, i)
            if (abs (a[i].Y-a[j].Y) + abs (a[i].X-a[j].X) == 1)
            {
                R.join (i, j);                
            }
    return R.connected ();
}

int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    FOR (ntest, 1, test+1)
    {
        cout << "Case #" << ntest << ": ";        
        cin >> n >> m;
        REP (i, n)
            cin >> s[i];
        map <VPII, int> a;
        vector <pair <VPII, int> > st;
        VPII init;
        VPII final;
        REP (i, n) REP (j, m)
        {
            if (s[i][j] == 'o' || s[i][j] == 'w')
                init.pb (PII (j, i));
            if (s[i][j] == 'x' || s[i][j] == 'w')
                final.pb (PII (j, i));
        }
        SORT (init);
        SORT (final);
        a[init] = 1;
        st.pb (make_pair (init, 0));
        for (int cr = 0; cr < SZ (st); ++cr)
        {
            VPII cur = st[cr].X;
/*            REP (i, SZ (cur))
                cout << cur[i].Y << ' ' << cur[i].X << endl;
            cout << endl;*/
            int now = a[cur];
            REP (i, SZ (cur))
                s[cur[i].Y][cur[i].X] = '#';
            int mark = st[cr].Y;
            REP (i, SZ (cur))
                REP (j, 4)
                {
                    int ny = cur[i].Y + dy[j];
                    int nx = cur[i].X + dx[j];
                    
                    int fy = cur[i].Y - dy[j];
                    int fx = cur[i].X - dx[j];
                    
                    if (ny < 0 || nx < 0 || ny >= n || nx >= m) continue;
                    if (fy < 0 || fx < 0 || fy >= n || fx >= m) continue;
                    
                    if (s[ny][nx] == '#') continue;
                    if (s[fy][fx] == '#') continue;
                    
                    VPII go = cur;
                    go[i].Y = ny;
                    go[i].X = nx;
                    SORT (go);
                    if (a.count (go))
                        continue;
                    bool gomark = !is_connected (go);
                    if (mark && gomark)                    
                        continue;
                    a[go] = now+1;
                    st.pb (make_pair (go, gomark));
                }
            REP (i, SZ (cur))
                s[cur[i].Y][cur[i].X] = '.';                
        }        
        cout << (a[final]-1) << endl;
    }    
	return 0;
}
