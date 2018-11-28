#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define X first
#define Y second
#define all(v) (v).begin(), (v).end()
#define mp(q, p) make_pair(q, p)
#define sqr(a) ((a) * (a))
#define pb push_back
#define ensure(a) assert(a)

#define pos(a) a.X][a.Y

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1E9 + 7;
const int NMAX = 1E3 + 7;
const ld EPS = 1E-9;

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int a[500][500], da[500][500], H, W, used[500][500];

bool can(pt& c, pt& d){
    assert(da[pos(c)] >= 0);
    pt cur(c.X + dx[da[pos(c)]], c.Y + dy[da[pos(c)]]);
    return cur == d;
}

bool good(pt& a){
    return a.X >= 0 && a.Y >= 0 && a.X < H && a.Y < W;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int N;
    scanf("%d\n", &N);
    for1(T, N){
        printf("Case #%d:\n", T);
        cin >> H >> W;
        memset(used, 0, sizeof(used));
        memset(da, -1, sizeof(da));

        forn(i, H)
            forn(j, W) cin >> a[i][j];

        queue<pt> q; 
        int id = 0;

        forn(i, H)
            forn(j, W){
                int minD = -1, minV = INF;
                forn(dir, 4){
                    pt cur(i + dx[dir], j + dy[dir]);
                    if(good(cur) && a[pos(cur)] < minV){
                        minV = a[pos(cur)];
                        minD = dir;
                    }
                }
                if(minV >= a[i][j]){
                    q.push(pt(i, j));
                    used[i][j] = ++id;
                    continue;
                }
                da[i][j] = minD;
            }

        while(!q.empty()){
            pt t = q.front();
            q.pop();
            forn(dir, 4){
                pt cur(t.X + dx[dir], t.Y + dy[dir]);
                if(good(cur) && !used[pos(cur)] && can(cur, t)){
                    used[pos(cur)] = used[pos(t)];
                    q.push(cur);
                }
            }
        }

        map<int, char> ans;
        forn(i, H){
            forn(j, W){
                if(!ans.count(used[i][j])) ans[used[i][j]] = 'a' + sz(ans);
                cout << ans[used[i][j]] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
