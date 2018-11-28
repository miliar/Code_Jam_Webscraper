#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

#define PB push_back
#define PII pair<int, int>
#define SZ(x) ((int)((x).size()))
#define OUT(x) printf(#x" %d\n", x)
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)

const int maxn = 500 + 10;
const int inf = (-1u) >> 1;

int Case = 1;
int r, c, d;
char s[maxn][maxn];
int g[maxn][maxn][3];

void init() {
    scanf ("%d%d%d", &r, &c, &d);
    REP(i,r) {
        scanf ("%s", s[i]);
    }
    memset (g, 0, sizeof(g));
    FOR(i,1,r) FOR(j,1,c) {
        int tg = s[i-1][j-1] - '0';
        //g[i][j] = g[i-1][j]+g[i][j-1]-g[i-1][j-1]+tg;
        g[i][j][0] = g[i-1][j][0]+g[i][j-1][0]-g[i-1][j-1][0]+tg*i;
        g[i][j][1] = g[i-1][j][1]+g[i][j-1][1]-g[i-1][j-1][1]+tg*j;
        g[i][j][2] = g[i-1][j][2]+g[i][j-1][2]-g[i-1][j-1][2]+tg;
    }
}

int get(int xa, int ya, int xb, int yb, int id) {
    //printf ("get %d %d %d %d -> %d\n", xa, ya, xb, yb, g[xa][ya][id] + g[xb-1][yb-1][id]
        //-g[xa][yb-1][id] - g[xb-1][ya][id]);
    return g[xa][ya][id] + g[xb-1][yb-1][id]
        -g[xa][yb-1][id] - g[xb-1][ya][id];
}

int get(int xa, int ya, int id) {
    //printf ("get %d %d %d -> %d\n", xa, ya, id, (s[xa-1][ya-1] - '0') * (id == 0? xa : ya));
    return (s[xa-1][ya-1] - '0') * (id == 0? xa : (id == 1? ya : 1));
}

bool check(int x, int y, int len) {
    int tx = get(x+len-1, y+len-1, x, y, 0);
    int ty = get(x+len-1, y+len-1, x, y, 1);
    tx -= get(x, y, 0) + get(x+len-1, y, 0) + get(x, y+len-1, 0)
        + get(x+len-1, y+len-1, 0);
    ty -= get(x, y, 1) + get(x+len-1, y, 1) + get(x, y+len-1, 1)
        + get(x+len-1, y+len-1, 1);
    int num = get(x+len-1, y+len-1, x, y, 2);
    num -= get(x, y, 2) + get(x+len-1, y, 2) + get(x, y+len-1, 2)
        + get(x+len-1, y+len-1, 2);
    int cx = 2*x + (len-1);
    int cy = 2*y + (len-1);
    //printf ("chech %d %d %d -> %d %d %d\n", x, y, len, cx, num, tx);
    return cx*num == 2*tx && cy*num == 2*ty;
    //if (len & 1) {
        //int hlen = len >> 1;
        //return get(x+hlen-1, y+len-1, x, y) - get(x, y) - get(x, y+len-1) ==
            //get(x+len-1, y+len-1, x+hlen+1, y) - get(x+len-1, y) - get(x+len-1, y+len-1) &&
            //get(x+len-1, y+hlen-1, x, y) - get(x, y) - get(x+len-1, y) ==
            //get(x+len-1, y+len-1, x, y+hlen+1) - get(x, y+len-1) - get(x+len-1, y+len-1);
    //} else {
        //int hlen = len >> 1;
        //return get(x+hlen-1, y+len-1, x, y) - get(x, y) - get(x, y+len-1) ==
            //get(x+len-1, y+len-1, x+hlen, y) - get(x+len-1, y) - get(x+len-1, y+len-1) &&
            //get(x+len-1, y+hlen-1, x, y) - get(x, y) - get(x+len-1, y) ==
            //get(x+len-1, y+len-1, x, y+hlen) - get(x, y+len-1) - get(x+len-1, y+len-1);
    //}
}

void solve() {
    printf ("Case #%d: ", Case++);
    int ans = -1;
    FOR(i,1,r) FOR(j,1,c) {
        for (int k = 3; i+k-1 <= r && j+k-1 <= c; ++k) {
            if (check(i,j,k)) {
                //printf ("yes %d %d %d\n", i, j, k);
                ans = max(ans, k);
            }
        }
    }
    if (ans == -1) {
        puts ("IMPOSSIBLE");
    } else {
        printf ("%d\n", ans);
    }
}

//#define SMALL
#define LARGE

int main() {
    string name = "B";
    #ifdef SMALL
    freopen ((name + "-small-attempt1.in").c_str(), "r", stdin);
    freopen ((name + "-small.out").c_str(), "w", stdout);
    #endif
    #ifdef LARGE
    freopen ((name + "-large.in").c_str(), "r", stdin);
    freopen ((name + "-large.out").c_str(), "w", stdout);
    #endif
    
    int testCase;
    scanf ("%d\n", &testCase);
    while (testCase--) {
        init();
        solve();
    }
    
    return 0;
}

