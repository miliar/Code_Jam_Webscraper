//#pragma comment(linker, "/STACK:66777216")
#include <iomanip>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>
#include <bitset>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i<_a; ++i)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define DEBUG(x) cout << #x << " = " << x << endl;
#define PR(a,n) cout << #a << " = "; FOR(i,1,n) cout << a[i] << ' '; puts("");
#define PR0(a,n) cout << #a << " = "; REP(i,n) cout << a[i] << ' '; puts("");
using namespace std;

const double PI = acos(-1.0);
const int MN = 30111000;

#define TWO(x) (1<<(x))
#define CONTAIN(S,x) (S & TWO(x))

int s, q, mark[6011][6011], lab[MN], cnt[MN], nBit[100];
pair<int,int> a[MN];
bool isBridge[MN], isFork[MN], isRing[MN];

const int di[] = {0,1,1,0,-1,-1};
const int dj[] = {1,1,0,-1,-1,0};

bool isCorner(int i, int j) {
    if (i == 1 && j == 1) return true;
    if (i == 1 && j == s) return true;
    if (i == s && j == 2*s-1) return true;
    if (i == 2*s-1 && j == 2*s-1) return true;
    if (i == 2*s-1 && j == s) return true;
    if (i == s && j == 1) return true;
    return false;
}

int isEdge(int i, int j) {
    if (isCorner(i,j)) return 0;
    if (i == 1) return 1;
    if (j - i == s-1) return 2;
    if (j == 2*s-1) return 4;
    if (i == 2*s-1) return 8;
    if (i - j == s-1) return 16;
    if (j == 1) return 32;
    return 0;
}

int getRoot(int u) {
    if (lab[u] < 0) return u;
    return lab[u] = getRoot(lab[u]);
}

void merge(int u, int v) {
    int x = lab[u] + lab[v];
    if (lab[u] < lab[v]) {
        lab[u] = x;
        lab[v] = u;
    }
    else {
        lab[v] = x;
        lab[u] = v;
    }
}

void bridge() {
    memset(lab, -1, sizeof lab);
    memset(cnt, 0, sizeof cnt);
    memset(mark, 0, sizeof mark);
    memset(isBridge, false, sizeof isBridge);
    
    FOR(i,1,q) {
        int u = a[i].F, v = a[i].S;
        mark[u][v] = i;
        if (isCorner(u, v)) cnt[i] = 1;
        lab[i] = -1;
        REP(dir,6) {
            int uu = u + di[dir], vv = v + dj[dir];
            if (mark[uu][vv]) {
                int j = mark[uu][vv];
                int x = getRoot(i), y = getRoot(j);
                if (x != y) {
                    if (cnt[x] && cnt[y]) {
                        isBridge[i] = true;
                        return ;
                    }
                    int sum = cnt[x] + cnt[y];
                    merge(x, y);
                    x = getRoot(x);
                    cnt[x] = sum;
                }
            }
        }
    }
}

void fork() {
    memset(lab, -1, sizeof lab);
    memset(cnt, 0, sizeof cnt);
    memset(mark, 0, sizeof mark);
    memset(isFork, false, sizeof isFork);
    
    FOR(i,1,q) {
        int u = a[i].F, v = a[i].S;
        mark[u][v] = i;
        cnt[i] = isEdge(u,v);
        lab[i] = -1;
        
        REP(dir,6) {
            int uu = u + di[dir], vv = v + dj[dir];
            if (mark[uu][vv]) {
                int j = mark[uu][vv];
                int x = getRoot(i), y = getRoot(j);
                if (x != y) {
                    if (nBit[cnt[x] | cnt[y]] == 3) {
                        isFork[i] = true;
                        return ;
                    }
                    int sum = cnt[x] | cnt[y];
                    merge(x, y);
                    x = getRoot(x);
                    cnt[x] = sum;
                }
            }
        }
    }
}

int first(int row) {
    if (row <= s) return 1;
    else return row - s + 1;
}

int last(int row) {
    if (row <= s) return row + s - 1;
    else return s+s-1;
}

int tmp[10];

void ring() {
    memset(lab, -1, sizeof lab);
    memset(cnt, 0, sizeof cnt);
    memset(mark, 0, sizeof mark);
    memset(isRing, false, sizeof isRing);
    
    int now = 0;
    FOR(i,1,q) mark[a[i].F][a[i].S] = -1;
    
    FOR(i,1,s+s-1) FOR(j,first(i),last(i)) if (mark[i][j] == 0) {
        ++now;
        mark[i][j] = now;
        cnt[now] = isCorner(i,j) + isEdge(i,j);
        if (cnt[now] > 1) cnt[now] = 1;
        int x = getRoot(now);
        REP(dir,6) {
            int ii = i + di[dir], jj = j + dj[dir];
            if (mark[ii][jj] > 0) {
                int y = getRoot(mark[ii][jj]);
                if (x != y) {
                    int sum = cnt[x] + cnt[y]; if (sum > 1) sum = 1;
                    merge(x, y);
                    x = getRoot(x);
                    cnt[x] = sum;
                }
            }
        }
    }
    
    FORD(i,q,1) {
        int u = a[i].F, v = a[i].S;
        ++now; mark[u][v] = now;
        if (isCorner(u,v) || isEdge(u,v)) cnt[now] = 1;
        int x = getRoot(mark[u][v]);
        REP(dir,6) {
            int uu = u + di[dir], vv = v + dj[dir];
            if (mark[uu][vv] > 0) tmp[dir] = cnt[getRoot(mark[uu][vv])];
        }
        
        REP(dir,6) {
            int uu = u + di[dir], vv = v + dj[dir];
            if (mark[uu][vv] > 0) {
                int y = getRoot(mark[uu][vv]);
                if (x != y) {
                    int sum = cnt[x] + cnt[y]; if (sum > 10) sum = 10;
                    merge(x, y);
                    x = getRoot(x);
                    cnt[x] = sum;
                }
            }
        }
        
        REP(dir,6) {
            int uu = u + di[dir], vv = v + dj[dir];
            if (mark[uu][vv] > 0) {
                if (tmp[dir] == 0) {
                    int y = getRoot(mark[uu][vv]);
                    if (cnt[y]) {
//                        cout << i << ' ' << u << ' ' << v << ' ' << uu << ' ' << vv << endl;
                        isRing[i] = true;
                        break;
                    }
                }
            }
        }
    }
}

void init() {
    REP(S,TWO(6)) {
        nBit[S] = 0;
        REP(i,6) if (CONTAIN(S,i)) nBit[S]++;
    }
}

int main() {
    freopen("B32.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    init();
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        cerr << test << endl;
        printf("Case #%d: ", test);
        scanf("%d%d", &s, &q);
//        cout << s << ' ' << q << endl;
        FOR(i,1,q) scanf("%d%d", &a[i].F, &a[i].S);
//        FOR(i,1,q) cout << a[i].F << ' ' << a[i].S << endl;
//        if (s <= 5) puts("HERE");
        
        bridge();
        fork();
        ring();
        
        bool ok = false;
        FOR(i,1,q) {
            if (isBridge[i] || isFork[i] || isRing[i]) ok = true;
            if (isBridge[i] && isFork[i] && isRing[i]) {
                printf("bridge-fork-ring in move %d\n", i);
                break;
            }
            else if (isFork[i] && isRing[i]) {
                printf("fork-ring in move %d\n", i);
                break;
            }
            else if (isBridge[i] && isRing[i]) {
                printf("bridge-ring in move %d\n", i);
                break;
            }
            else if (isBridge[i] && isFork[i]) {
                printf("bridge-fork in move %d\n", i);
                break;
            }
            else if (isRing[i]) {
                printf("ring in move %d\n", i);
                break;
            }
            else if (isFork[i]) {
                printf("fork in move %d\n", i);
                break;
            }
            else if (isBridge[i]) {
                printf("bridge in move %d\n", i);
                break;
            }
        }
        if (!ok) puts("none");
    }
    return 0;
}
