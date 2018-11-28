#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define debug(x) {cerr << #x << " = " << x << endl;}
template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

typedef vector<vector<ld> > M;
M getM(int n, int m, ld v = 0){
    return M(n, vector<ld>(m, v));
}
#define pos(a) (a).X][(a).Y
const int dx[] = {0,0,1,-1};
const int dy[] = {1,-1,0,0};

M F, C, d;
int inq[200][200];

int n, m;
ld h;

pt start, end;

bool in(const pt& a){
    return 0 <= a.X && a.X < n && 0 <= a.Y && a.Y < m;
}

inline ld getch(const ld& t){
    return max(h - t * 10, ld(0.0));
}

int can(const pt& a, const pt& b, const ld& ta){
    ld ch = getch(ta);

    ld maxf = max(F[pos(a)], max(F[pos(b)], ch));
    if(maxf <= C[pos(b)] - 50 + EPS){
        if(F[pos(b)] <= C[pos(a)] - 50.0 + EPS){
            if(F[pos(a)] <= ch - 20 + EPS)
                return 1;
            return 10;
        }
        return -1;
    }
            
    return -1;
}

ld getTime(const pt& a, const pt& b, ld ta){
    if(abs(ta) < EPS && can(a, b, ta) != -1) return 0.0;

    ld cf = F[pos(a)], mintime = 1e100, dtime = 0;
    if(cf <= getch(ta) - 20.0 + EPS){
        dtime = max(getch(ta) - (cf + 20.0), ld(0)) / 10.0;
        ld lf = ta, rg = ta + dtime;
        forn(i, 100){
            ld mid = (lf+rg)/2;
            if(can(a, b, mid) != -1)
                rg = mid;
            else
                lf = mid;
        }
        if(can(a, b, rg) != -1)
            mintime = min(mintime, (rg - ta) + 1.0);
    }

    ld lf = ta + dtime, rg = h/10+10;
    forn(i, 100){
        ld mid = (lf+rg)/2;
        if(can(a, b, mid) != -1)
            rg = mid;
        else
            lf = mid;
    }

    if(can(a, b, rg) != -1)
        mintime = min(mintime, (rg - ta) + 10.0);

    return mintime;
}

int main() {
    #ifdef myproject
    freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);
    #endif

    int testCount = 0;
    scanf("%d", &testCount); char testBuf[10]; gets(testBuf);
    for1(currentTest, testCount){
        printf("Case #%d: ", currentTest);
        //solution
        cin >> h >> n >> m;
        F = getM(n, m), C = getM(n, m);
        forn(i, n)
            forn(j, m)
                cin >> C[i][j];
        forn(i, n)
            forn(j, m)
                cin >> F[i][j];

        start = pt(0, 0), end = pt(n-1, m-1);
        d = getM(n, m, 1e100);
        set<pair<ld, pt> > q;

        q.insert(mp(0, start)), d[pos(start)] = 0;

        while(!q.empty()){
            pt v = q.begin()->Y; q.erase(q.begin());

            forn(dr, 4){
                pt u(v.X + dx[dr], v.Y + dy[dr]);
                if(!in(u)) continue;

                ld cost = getTime(v, u, d[pos(v)]);

                if(d[pos(u)] > d[pos(v)] + cost){
                    q.erase(mp(d[pos(u)], u));
                    d[pos(u)] = d[pos(v)] + cost;
                    q.insert(mp(d[pos(u)], u));
                }
            }
        }

        ld ans = d[n-1][m-1];
        printf("%.10lf", double(ans)); 
        fprintf(stderr, "Test #%d: %d\n", currentTest, (int)clock());
        puts("");
    }

    return 0;
}


