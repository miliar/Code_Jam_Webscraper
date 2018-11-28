// author: amit
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

#define SORT(x) sort(x.begin(), x.end())
#define SS {int t; scanf("%d", &t), t}
//

int r, c;

bool valid(int i, int j) {
    return (i>=0) && (i<r) && (j<c) && (j>=0);
}

char grid[100][100];
char ans[4] = {'/', '\\', '\\', '/'};
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);

    for(int testcase = 1; testcase <= t; testcase++) {

        scanf("%d%d", &r, &c);

        REP(i, r) scanf("%s", grid[i]);

        REP(i, r) REP(j, c) grid[i][j]=(grid[i][j]=='#')?1:grid[i][j];

        REP(i, r) REP(j, c) {
            if(grid[i][j]==1) {
                bool ok = true;
                REPSE(k, i, i+2) REPSE(l, j, j+2) {
                    if(!valid(k, l) || grid[k][l]=='.') ok = false;
                }
                if(ok) {
                    int cnt = 0;
                    REPSE(k, i, i+2) REPSE(l, j, j+2) {
                        grid[k][l] = ans[cnt++];
                    }
                }
            }
        }

        bool fine = true;
        REP(i, r) REP(j ,c) if(grid[i][j]==1) {
            fine = false;
        }

        printf("Case #%d:\n", testcase);
        if(fine) {
            REP(i, r) printf("%s\n", grid[i]);
        } else {
            printf("Impossible\n");
        }

    }
}
