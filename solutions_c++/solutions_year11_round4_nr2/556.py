#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int r,c,d;
char str[515][515];
int map[515][515];
int xy_value[515][515],x_value[515][515],y_value[515][515];

bool isright(int x,int y,int size)
{
    double valuex ,valuey;
    double midx=x-(size-1)/2.0,midy=y-(size-1)/2.0;
    valuex = 0;valuey = 0;
    valuex=x_value[x][y]-x_value[x-size][y]-x_value[x][y-size]+x_value[x-size][y-size];
    valuex-=midx*(xy_value[x][y]-xy_value[x-size][y]-xy_value[x][y-size]+xy_value[x-size][y-size]);
    valuey=y_value[x][y]-y_value[x-size][y]-y_value[x][y-size]+y_value[x-size][y-size];
    valuey-=midy*(xy_value[x][y]-xy_value[x-size][y]-xy_value[x][y-size]+xy_value[x-size][y-size]);

    valuex-=(x-size+1-midx)*map[x-size+1][y-size+1];
    valuey-=(y-size+1-midy)*map[x-size+1][y-size+1];
    valuex-=(x-midx)*map[x][y],valuey-=(y-midy)*map[x][y];
    valuex-=(x-size+1-midx)*map[x-size+1][y];
    valuey-=(y-midy)*map[x-size+1][y];
    valuex-=(x-midx)*map[x][y-size+1];
    valuey-=(y-size+1-midy)*map[x][y-size+1];
    return (valuex==0&&valuey==0);
}

int doit()
{
    int ansk;
    int i,j;
    for(ansk=min(r,c);ansk>=3;ansk--)
    {
        for(i=ansk;i<=r;++i)
            for(j=ansk;j<=c;++j)
                if(isright(i,j,ansk))return ansk;
    }
    return -1;
}
int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);
    int t,cases=1;
    char ch;
    scanf("%d",&t);
    int i,j;
    for(cases=1;cases<=t;cases++)
    {
        scanf("%d%d%d",&r,&c,&d);
        for(i=1;i<=r;++i)
        {
            getchar();
            for(j=1;j<=c;++j)
            {
                scanf("%c",&ch);
                map[i][j] =ch - '0';
            }
        }
        memset(xy_value,0,sizeof(xy_value));
        memset(x_value,0,sizeof(x_value));
        memset(y_value,0,sizeof(y_value));
        for(i=1;i<=r;++i)
            for(j=1;j<=c;++j)
            {
                xy_value[i][j]+=xy_value[i-1][j]+xy_value[i][j-1]-xy_value[i-1][j-1]+map[i][j];
                x_value[i][j]+=x_value[i-1][j]+x_value[i][j-1]-x_value[i-1][j-1]+i*map[i][j];
                y_value[i][j]+=y_value[i-1][j]+y_value[i][j-1]-y_value[i-1][j-1]+j*map[i][j];
            }
        int tem=doit();
        if(tem==-1)printf("Case #%d: IMPOSSIBLE\n",cases);
        else printf("Case #%d: %d\n",cases,tem);
    }
    return 0;
}
