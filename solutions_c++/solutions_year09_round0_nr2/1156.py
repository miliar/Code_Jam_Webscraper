#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <cctype>
#include <cmath>

using namespace std;

const int M = 111;
const int INT_MAX = 123456;
int tab[M][M];
int out[M][M];
bool mark[M][M];

inline int mabs(int a) {
    if (a<0) return -a;
    return a;
}
 
int gid;

int dfs(int a,int b) {
    if (mark[a][b])
        return out[a][b];
    mark[a][b] = true;
    int mini = INT_MAX;

    for (int i=-1;i<=1;i++)
        for (int j=-1;j<=1;j++) {
            if (mabs(i) + mabs(j) == 1) {
                int at = a+i;
                int bt = b+j;
                mini = min(mini, tab[at][bt]);
            }
    }
    if (tab[a][b] <= mini)
        return out[a][b] = gid++;
    for (int i=-1;i<=1;i++)
        for (int j=-1;j<=1;j++) {
            if (mabs(i) + mabs(j) == 1) {
                int at = a+i;
                int bt = b+j;

                if (tab[at][bt] == mini) {
                    return out[a][b] = dfs(at, bt);
                }
            }
        }
    return -1;
}

int main() {
    int lw;
    scanf("%d",&lw);
    for (int L=1;L<=lw;++L) {
        int n,m;
        scanf("%d%d",&n,&m);

        for (int i=0;i<=n+1;i++)
            tab[i][0] = tab[i][m+1] = INT_MAX;

        for (int j=0;j<=m+1;j++)
            tab[0][j] = tab[n+1][j] = INT_MAX;

        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++) {
                scanf("%d",&tab[i][j]);
                mark[i][j] = false;
            }

        gid = 1;
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++)
                if (!mark[i][j]) {
                    dfs(i,j);
                }

        printf("Case #%d:\n",L);

        map<int, char> odw;
        char akt = 'a';
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++) {
                int id = out[i][j];
                if (odw.find(id) == odw.end()) {
                    odw[id] = akt++;
                }
                char res = odw[id];
                printf( (j==m)?("%c\n"):("%c "), res);
            }
    }

    return 0;
}
