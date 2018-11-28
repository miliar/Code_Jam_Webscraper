#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const int xmax=104;
int n,m,s;
int map[xmax][xmax];
int mark[xmax][xmax];
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};//North, West, East, South.

int dfs(int x, int y)
{
    //printf("%d %d %d %d\n", x, y, map[x][y], s);
    int nx=0,ny=0,nh=map[x][y];
    for(int i=0; i<4; ++i)
    {
        if(map[x+dir[i][0]][y+dir[i][1]]<nh) 
        {
            nh=map[x+dir[i][0]][y+dir[i][1]];
            nx=x+dir[i][0];
            ny=y+dir[i][1];
        }
    }
    if(nx==0 && ny==0)
    {
        if(mark[x][y]==-1) mark[x][y]=s,++s;
        return mark[x][y];
    }
    else 
    {
        mark[x][y]=dfs(nx,ny);
        return mark[x][y];
    }
}

void solve()
{
    int i,j;
    memset(mark, -1, sizeof(mark));
    s=0;
    for(i=1; i<=n; ++i)
        for(j=1; j<=m; ++j)
            if(mark[i][j]==-1) dfs(i,j);
}

int main()
{
    int caseid,casenum;
    freopen("G:\\Download\\B-large.in", "r", stdin);
    freopen("G:\\Download\\B-large.in.out", "w", stdout);
    scanf("%d", &casenum);
    for(caseid=1; caseid<=casenum; ++caseid)
    {
        memset(map, 127, sizeof(map));
        int i,j;
        scanf("%d %d", &n, &m);
        for(i=1; i<=n; ++i)
            for(j=1; j<=m; ++j)
                scanf("%d", &map[i][j]);
        solve();
        printf("Case #%d:\n", caseid);
        for(i=1; i<=n; ++i)
        {
            for(j=1; j<=m; ++j)
            {
                if(j>1) printf(" ");
                printf("%c", 'a'+mark[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
/*
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8
 */

