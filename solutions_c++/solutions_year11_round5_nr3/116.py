#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 6;
char buf[MAXN][MAXN];
int R, C;

const int dir[][2] = {{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1}};
int ch[300][2];
int ans = 0;
int ind[MAXN][MAXN];
int d[MAXN][MAXN];

int check() {
    int i, j, tx, ty;
    memset(ind, 0, sizeof(ind));
    for (i = 0 ; i < R ; i++)
        for (j = 0 ; j < C ; j++) {
            tx = i + dir[d[i][j]][0];
            ty = j + dir[d[i][j]][1];
            if (tx < 0) tx += R;
            if (tx >= R) tx -= R;
            if (ty < 0) ty += C;
            if (ty >= C) ty -= C;
            if (++ind[tx][ty] > 1) return 0;
        }
    return 1;
}

int solve(int p) {
    if (p == R * C) {
        ans += check();
        return 0;
    }
    int r = p / C;
    int c = p % C;
    d[r][c] = ch[buf[r][c]][0];
    solve(p+1);
    d[r][c] = ch[buf[r][c]][1];
    solve(p+1);
}

int main() {
    freopen("c-small-0.in","r",stdin);
    freopen("c-small-0.out","w",stdout);
    ch['-'][0] = 2;
    ch['-'][1] = 6;
    ch['|'][0] = 0;
    ch['|'][1] = 4;
    ch['/'][0] = 1;
    ch['/'][1] = 5;
    ch['\\'][0] = 3;
    ch['\\'][1] = 7;
    int T, ca, i;
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%d%d",&R,&C);
        for (i = 0 ; i < R ; i++)
            scanf("%s",buf[i]);
        ans = 0;
        solve(0);
        printf("Case #%d: ",ca);
        printf("%d\n",ans % 1000003);
    }
    return 0;
}
/*
3
3 3
|-/
|||
--|
3 4
----
||||
\\//
4 4
|---
\-\|
\|||
|--\
*/
