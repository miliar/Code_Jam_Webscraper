#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#define INF 100005

using namespace std;
char Maze[5][5];
int F[2][3][5];
int CHECK()
{
    int i,j,k;
    for (i=0;i<=4;i++)
        for (j=0;j<2;j++)
            for (k=0;k<2;k++)
                if (F[j][k][i]==4 || (F[j][k][i]==3 && F[j][2][i]==1)) {
                    if (k) puts("O won");
                    else puts("X won");
                    return 1;
                }
    return 0;
}
int main()
{
    int i,j,h,t,tab;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    for (h=scanf("%d",&t);h<=t;h++)
    {
        memset(F,tab=0,sizeof(F));
        for (i=0;i<4;i++)
            scanf("%s",Maze[i]);
        for (i=0;i<4;i++)
            for (j=0;j<4;j++)
            {
                if (Maze[i][j]=='.') tab=1;
                if (Maze[i][j]=='T') {
                    F[0][2][i]++,F[1][2][j]++;
                    if (i==j)   F[0][2][4]++;
                    if (i==3-j) F[1][2][4]++;
                }
                if (Maze[i][j]=='X') {
                    F[0][0][i]++,F[1][0][j]++;
                    if (i==j)   F[0][0][4]++;
                    if (i==3-j) F[1][0][4]++;
                }
                if (Maze[i][j]=='O') {
                    F[0][1][i]++,F[1][1][j]++;
                    if (i==j)   F[0][1][4]++;
                    if (i==3-j) F[1][1][4]++;
                }
            }
        printf("Case #%d: ",h);
        if (CHECK()==0) {
            if (tab) puts("Game has not completed");
            else puts("Draw");
        }
    }
    return 0;
}
