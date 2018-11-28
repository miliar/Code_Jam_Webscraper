#pragma comment(linker, "/STACK:10000000")

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

const int NMAX = 4000;

vector<int> g[NMAX];
int t1[NMAX], t2[NMAX];
int n, m;

vector<int> ord;
bool used[NMAX][NMAX];

int center;

int getpos(int v, int c){
    if(v < c)
        return c-v;
    return (n-v)+c+1;
}

bool cmp(int a, int b){
    int p1 = getpos(a, center), p2 = getpos(b, center);
    return p1 < p2;
}

void dfs(int p, int v){
    used[p][v] = true;
    ord.pb(v);

    center = v;
    int pos = lower_bound(all(g[v]), p, cmp) - g[v].begin();
    int next = g[v][(pos-1+sz(g[v])) % sz(g[v])];

    if(!used[v][next]){
        dfs(v, next);
    }
}

vector<int> gs[NMAX];
int szgs;
map<pt, vector<int> > next;

int color[NMAX];
int us[NMAX];

void clear_data(){
    forn(i, n)
       g[i].clear();
    forn(i, n) forn(j, n) used[i][j] = false;
    memset(us, 0, sizeof(int)*n);
    memset(color, -1, sizeof(int)*n);
    szgs = 0;
    next.clear();
}

void mark(int v, int u, int ans){
    vector<int>& ng = next[pt(v,u)];

    int idx = -1;
    forn(i, sz(ng)){
        int cg = ng[i];
        if(!us[cg]){
            idx = cg;
            break;
        }
    }

    if(idx == -1) return;
    us[idx] = true;

    vector<int>& vs = gs[idx];

    int pos = find(all(vs), v) - vs.begin();
    if(vs[(pos+1) % sz(vs)] != u)
        reverse(all(vs));
    pos = find(all(vs), v) - vs.begin();    

    int unuscol = 0;

    for(int add = 2; add < sz(vs); add++){
        int i = (pos + add) % sz(vs);
        int ni = (pos + add + 1) % sz(vs);
        int pi = (pos + add - 1 + sz(vs)) % sz(vs);

        while(unuscol == color[v] || unuscol == color[u])
            unuscol++;

        if(unuscol != ans)
            color[vs[i]] = unuscol++;
        else{
            forn(c, ans){
                if(color[vs[pi]] != c && color[vs[ni]] != c){
                    color[vs[i]] = c;
                    break;
                }                    
            }
                   
        }
        assert(color[vs[i]] != -1);
    }

    forn(i, sz(vs)){
        int nv = vs[i], nu = vs[i+1 == sz(vs) ? 0 : i+1];
        mark(nv, nu, ans);
    }
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    cout.precision(10); cout << fixed;

    int testCount;
    cin >> testCount;

    memset(color, -1, sizeof color);

    forn(curTest, testCount){
        printf("Case #%d: ", curTest+1);

        scanf("%d%d", &n, &m);
        forn(i, m)
            scanf("%d", &t1[i]);
        forn(i, m)
            scanf("%d", &t2[i]);

        forn(i, m){
            g[t1[i]-1].pb(t2[i]-1);
            g[t2[i]-1].pb(t1[i]-1);
        }
        forn(i, n){
            g[i].pb((i+1)%n);
            g[(i+1)%n].pb(i);
        }

        forn(i, n){
            center = i;
            sort(all(g[i]), cmp);
        }

        int ans = INF; 
        szgs = 0;
        forn(v, n){
            forn(i, sz(g[v])){
                int u = g[v][i];
                if(!used[v][u]){
                    ord.clear();
                    dfs(v, u);    

                    ans = min(ans, sz(ord));
                    if(sz(ord) != n){   
                        gs[szgs] = ord;
                        forn(i, sz(ord)){
                            int v = ord[i], u = (i+1 == sz(ord) ? ord[0] : ord[i+1]);
                            next[pt(v,u)].pb(szgs);
                            next[pt(u,v)].pb(szgs);
                        }
                        szgs++;
                    }
                }                
            }
        }

        assert(ans > 2 && ans < INF);

        color[0] = 0, color[1] = 1;
        mark(0, 1, ans);

        printf("%d\n", ans);
        forn(i, n)
            printf("%d ", color[i]+1);
        puts("");

        clear_data();
    }
    
    return 0;
}



