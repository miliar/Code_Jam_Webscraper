#include <stdio.h>
double w,l;
struct point
{
    double x,y;
    point(): x(0),y(0) {};
    point(double a,double b): x(a),y(b) {};
};
point p[100010],tp[100010];
double r[100010];
double EPS = 0.1;
bool ok(point p,int cnt,double tr)
{
    double tx=p.x,ty=p.y;
    if (tx<0||tx>w) return false;
    if (ty<0||ty>l) return false;
    for (int i=0;i<cnt;i++)
    {
        double ll=tp[i].x-r[i]-tr,rr=tp[i].x+r[i]+tr;
        double uu=tp[i].y-r[i]-tr,dd=tp[i].y+r[i]+tr;
        if (p.x>ll&&p.x<rr&&p.y>uu&&p.y<dd) return false;
    }
    return true;
}
double tx[100010],ty[100010];
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1; ii<=T; ii++)
    {
        int n;
        scanf("%d%lf%lf",&n,&w,&l);
        tx[0]=0; tx[1]=w;
        ty[0]=0; ty[1]=l;
        for (int i=0; i<n; i++)
        {
            scanf("%lf",&r[i]);
            tx[0]=0; tx[1]=w;
            ty[0]=0; ty[1]=l;
            int cnt=2;
            for (int j=0;j<i;j++)
            {
                tx[cnt]=tp[j].x-r[j]-r[i];
                ty[cnt++]=tp[j].y-r[j]-r[i];
                tx[cnt]=tp[j].x+r[j]+r[i];
                ty[cnt++]=tp[j].y+r[j]+r[i];
            }
            bool okk=false;
            for (int j=0;j<cnt&&!okk;j++)
                for (int k=0;k<cnt&&!okk;k++)
                {
                    point pp=point(tx[j],ty[k]);
                    if (ok(pp,i,r[i]))
                    {
                        okk=true;
                        //printf("hhh");
                        tp[i]=pp;
                        break;
                    }
                }
        }
        printf("Case #%d:",ii);
        for (int i=0; i<n; i++)
            printf(" %f %f",tp[i].x,tp[i].y);
        puts("");
    }
    return 0;
}
