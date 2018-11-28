#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string.h>
#include <string>

#define PI 3.14159265358979
#define PB(x) push_back(x)
using namespace std;
typedef long long LL;

const int N= 110;

int g[N][N];
char g2[N][N];

int row,column;

int fx[]={0,-1,1,0};
int fy[]={-1,0,0,1};
char outch;
char nowch;

    void inputing()
    {
        int i,j;
        scanf("%d%d",&row,&column);
        memset(g,0,sizeof(g));
        for (i=0;i<row;i++)
            for (j=0;j<column ; j++)
            scanf("%d",&g[i][j]);
        memset(g2,0,sizeof(g2));

    }

    void dfs(int x,int y)
    {
        int xx,yy;
        int i;
        int j;
        int min2 = 1<<27;
        j = -1;

        if (g2[y][x] !=0)
        {
            outch = g2[y][x];
//            printf("break at ( %d , %d ) colour is %c\n",x,y,outch);//debug
            return ;
        }
//        printf("now at  ( %d , %d )\n",x,y);//debug

        for (i=0;i<4;i++)
        {
            xx = x + fx[i];
            yy = y + fy[i];
            if (xx<0 || xx>=column || yy<0 || yy >=row) continue;
            if (g[y][x] <= g[yy][xx] ) continue;
            if (g[yy][xx] < min2 )
            {
                j = i;
                min2 = g[yy][xx];
            }
        }
        if (j!=-1)
        dfs(x + fx[j],y + fy[j]);
        else //无路可走 就是山谷
        {
            outch = nowch++;
//            printf(" new area at ( %d , %d )  %c\n",x,y,outch);//debug
        }
        g2[y][x] = outch;
    }

    void work()
    {
        int i,j;
        nowch = 'a';
        for (i=0;i<row;i++)
            for (j=0;j<column;j++)
            if (g2[i][j] == 0)
            dfs(j,i);
    }

    void outputing()
    {
        int i,j;
        for (i=0;i<row;i++)
        {
            printf("%c",g2[i][0]);
            for (j=1;j<column;j++)
            printf(" %c",g2[i][j]);
            printf("\n");
        }
    }


int main()
{
//    freopen("inputing","r",stdin);
//    freopen("outputing","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int i=1;i<=cas;i++)
    {
        printf("Case #%d:\n",i);
        inputing();
        work();
        outputing();
    }

    return 0;
}


