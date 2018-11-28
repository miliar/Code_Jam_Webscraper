#include <iostream>
#include <math.h>
using namespace std;

struct point
{
    double x,y,r;
}p[100];
int n,m,i,j,k,ncase,t;
double tempr,bestr;

double getans(int x, int y)
{
    double dx,dy,dis;
    dx = p[x].x-p[y].x;
    dy = p[x].y-p[y].y;
    dis = sqrt(dx*dx+dy*dy);
    return (dis+p[x].r+p[y].r)/2;
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    scanf("%d",&ncase);
    for (t=1; t<=ncase; t++)
    {
        scanf("%d",&n);
        for (i=0; i<n; i++)
            scanf("%lf%lf%lf",&p[i].x,&p[i].y,&p[i].r);
        if (n==1)
            printf("Case #%d: %lf\n",t,p[0].r);
        if (n==2)
            printf("Case #%d: %lf\n",t,max(p[0].r,p[1].r));
        if (n==3)
        {
            bestr = max(getans(0,1),p[2].r);
            bestr = min(bestr,max(getans(0,2),p[1].r));
            bestr = min(bestr,max(getans(1,2),p[0].r));
            printf("Case #%d: %lf\n",t,bestr);
        }
    }
    return 0;
}
