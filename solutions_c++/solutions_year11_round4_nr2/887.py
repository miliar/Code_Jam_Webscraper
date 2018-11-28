// BEGIN CUT HERE

// END CUT HERE
// Mini Template
#include <cstdio>
#include <iostream>
#include <cmath>
#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define TR(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define REP(i, n) for(int i = 0; i<(n); i++)
#define REPSE(i, s, e) for(int i = s; i <(e); i++)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define FILL(x, c) memset(x, c, sizeof(x))
#define ALL(x) x.begin(), x.end()
#define FIN(x, c) (x.find(c)!=x.end())
#define IN(x, c) (find(x.begin(), x.end(), c)!=x.end())
// Template Ends
//hihihihihihi

char grid[100][100];
const double EPS = 1e-9;
int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int ts;
    scanf("%d", &ts);

    for(int testcase = 1; testcase <= ts; testcase++) {
        int r, c, d;
        scanf("%d%d%d", &r, &c, &d);

        REP(i, r) scanf("%s", grid[i]);

        REP(i, r) REP(j, c) grid[i][j] -= '0';

        int ans = -1;
        REP(i, r) REP(j, c) {
            //i = 1;
            //j = 1;
            REPSE(k, 3, 11) {
                //k = 5;
                //printf("i = %d j = %d\n", i, j);
                //printf("k = %d\n", k);
                double x, y;
                    x = (double)k/2;
                    y = (double)k/2;
                //printf("x = %lf y = %lf\n", x, y);
                ////getchar();
                double tx, ty;
                tx = ty = 0;
                bool ok = 1;
                for(int m = i; m < i+k; m++) {
                    if(m >= r) {
                        ok = false;
                        goto out;
                    }
                    for(int n = j; n < j+k; n++) {
                        if(n>=c) {
                            ok = false;
                            goto out;
                        }
                        if(m==i && n==j) continue;
                        if(m==i && (n==(j+k)-1)) continue;
                        if((m==i+k-1) && (n==j)) continue;
                        if((m==i+k-1) && (n==(j+k)-1)) continue;

                        double cx, cy;
                        cx = x-((m-i)+0.5);
                        cy = y-((n-j)+0.5);
//
                       // printf("cx = %lf cy = %lf\n", cx, cy);
                        tx += cx*(d+grid[n][m]);
                        ty += cy*(d+grid[n][m]);
                    }
                }
                out:
                ;
                if(ok) {
                    //printf("tx = %lf ty = %lf\n", tx, ty);
                    //printf("x = %lf y = %lf\n", x, y);
                    //getchar();
                    if((fabs(tx)<EPS) && (fabs(ty)<EPS)) {
                        ans = max(ans, k);
                    }
                }
            }
            ////while(1);
        }

        if(ans==-1)
             printf("Case #%d: IMPOSSIBLE\n", testcase);
        else
        printf("Case #%d: %d\n", testcase, ans);
    }
}
