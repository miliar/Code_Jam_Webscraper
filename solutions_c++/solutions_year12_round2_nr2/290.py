#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
using namespace std;
double use[110][110];
int c[110][110],f[110][110];
struct node
{
    int x,y,down;
    double t;
};
queue <node> q;
int wayx[10]={-1,0,0,1};
int wayy[10]={0,-1,1,0};
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        int h,n,m;
        scanf("%d%d%d",&h,&n,&m);
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                scanf("%d",&c[i][j]);
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                scanf("%d",&f[i][j]);
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                use[i][j]=-10000;
        while (!q.empty()) q.pop();
        node hh;
        hh.x=0; hh.y=0; hh.t=0; hh.down=0;
        use[0][0]=0;
        q.push(hh);
        while (!q.empty())
        {
            node hh=q.front();
            q.pop();
            int water=(h-hh.down>=0?h-hh.down:0);
            //printf("%d %d %lf %d\n",hh.x,hh.y,hh.t,water);
            int fnow=f[hh.x][hh.y];
            int cnow=c[hh.x][hh.y];
            for (int i=0;i<4;i++)
            {
                int tx=hh.x+wayx[i];
                int ty=hh.y+wayy[i];
                if (tx<0||tx>=n) continue;
                if (ty<0||ty>=m) continue;
                int fadj=f[tx][ty];
                int cadj=c[tx][ty];
                if (cadj-fadj<50||cadj-fnow<50) continue;
                if (cnow-fadj<50) continue;
                int towait=(cadj-water>=50?0:50-(cadj-water));
                if (water>=fnow&&water-towait<fnow) continue;
                double time=hh.t+towait/10.0;
                double tdown=hh.down+towait;
                if (water-towait<h)
                {
                    if (water-towait-fnow>=20)
                    {
                        time+=1;
                        tdown+=10;
                    }
                    else
                    {
                        time+=10;
                        tdown+=100;
                    }
                }
                if (use[tx][ty]<-100||use[tx][ty]>time)
                {
                    use[tx][ty]=time;
                    node next;
                    next.x=tx; next.y=ty; next.t=time; next.down=tdown;
                    q.push(next);
                }
            }
        }
        printf("Case #%d: %.1f\n",ii,use[n-1][m-1]);
    }
    return 0;
}
