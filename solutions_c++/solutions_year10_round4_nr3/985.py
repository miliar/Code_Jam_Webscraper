/*

*/
#include <iostream>
#include <cstring>
#include <cstdio>
#define maxv(a,b) (a>=b ? a : b)
#define minv(a,b) (a<=b ? a : b)
using namespace std;
bool g[110][110],g2[110][110];
int Case,r,x1,x2,y1,y2,tim,maxx,maxy,minx,miny,sum;
int cnt[3][3]={{0,-1},{-1,0}};
void work()
{
    while (sum) {
    tim++;
    for (int i=minx;i<=maxx;i++) 
        for (int j=miny;j<=maxy;j++)
            g2[i][j]=g[i][j];
    for (int i=minx;i<=maxx;i++) 
        for (int j=miny;j<=maxy;j++) {
            bool flag1=false,flag2=false;
            for (int k=0;k<2;k++) {
                int di=i+cnt[k][0],dj=j+cnt[k][1];
                if (di<minx||di>maxx||dj<miny||dj>maxy) continue;
                if (g[di][dj]) {
                    if (k==0) flag1=true;
                    if (k==1) flag2=true;
                    }
                }
            if (g[i][j]) {
                if (!flag1 && !flag2) {
                    g2[i][j]=false;
                    sum--;
                    }
                }
            else if (flag1 && flag2) {
                g2[i][j]=true;
                sum++;
                }
            }
    for (int i=minx;i<=maxx;i++) 
        for (int j=miny;j<=maxy;j++)
            g[i][j]=g2[i][j];
    }
}
void display()
{
    scanf("%d",&Case);
    for (int ca=1;ca<=Case;ca++) {
        printf("Case #%d: ",ca);
        scanf("%d",&r);
        memset(g,0,sizeof(g));
        maxx=maxy=0;
        minx=miny=0x7fffffff;
        while (r--) {
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            if (x1>x2) swap(x1,x2);
            if (y1>y2) swap(y1,y2);
            maxx=maxv(maxx,x2);
            maxy=maxv(maxy,y2);
            minx=minv(minx,x1);
            miny=minv(miny,y1);
            for (int i=x1;i<=x2;i++) 
                for (int j=y1;j<=y2;j++)
                    g[i][j]=true;
            }
        tim=sum=0;
        for (int i=minx;i<=maxx;i++) 
            for (int j=miny;j<=maxy;j++)
                if (g[i][j]) sum++;
        work();
        printf("%d\n",tim);
        }
        
}
int main()
{
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-small-attempt0.out","w",stdout);
    display();
    return 0;
}

