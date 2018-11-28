#include <stdio.h>
#include <stdlib.h>
#include <cstring>

int m[105][105],res[105][105],h,w,sum,cur=1,cas=1;
bool vst[105][105];
int dix[4][2]={ {-1,0},{0,-1},{0,1},{1,0} };

void dfs(int x,int y)
{
    int min=1000000000,i,j,mini;
    vst[x][y]=true;
    sum++;
    for (i=0;i<4;i++)
    {
        int tmpx=x+dix[i][0],tmpy=y+dix[i][1];
        if (tmpx>=0&&tmpx<h&&tmpy>=0&&tmpy<w&&m[tmpx][tmpy]<min)
        {
            min=m[tmpx][tmpy];
            mini=i;
        }
    }
    if (min>=m[x][y]) res[x][y]=cur++;
    else
    {
        int tmpx=x+dix[mini][0],tmpy=y+dix[mini][1];
        if (vst[tmpx][tmpy]) res[x][y]=res[tmpx][tmpy];
        else
        {
            dfs(tmpx,tmpy);
            res[x][y]=res[tmpx][tmpy];
        }
    }
}

int main()
{
    int i,j,T;
    
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d%d",&h,&w);
        for (i=0;i<h;i++)
        {
            for (j=0;j<w;j++)
            {
                scanf("%d",&m[i][j]);
            }
        }
        memset(vst,0,sizeof(vst));
        memset(res,0,sizeof(res));
        cur=1;
        for (i=0;i<h;i++)
        {
            for (j=0;j<w;j++)
            {
                if (!vst[i][j]) dfs(i,j);
            }
        }
        printf("Case #%d:\n",cas++);
        for (i=0;i<h;i++)
        {
            for (j=0;j<w-1;j++)
            {
                printf("%c ",(char)('a'+res[i][j]-1));
            }
            printf("%c\n",(char)('a'+res[i][j]-1));
        }
    }
    //system("pause");
    return 0;
}
