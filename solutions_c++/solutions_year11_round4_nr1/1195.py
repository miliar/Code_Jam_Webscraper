/*

*/
#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
int x,s,r,n,num,run[3010];
double t;
struct data{
    int x,y,w;
} p[1010],q[3010];
bool cmp(const data &r1,const data &r2) {
    if (r1.x==r2.x) return r1.y<r2.y;
    return r1.x<r2.x;
}
bool cmp2(const data &r1,const data &r2) {
    return r1.w<r2.w;
}
int dcmp(double x)
{
    if (fabs(x)<1e-7) return 0;
    return x>0?1:-1;
}
void display()
{
    int Case;
    scanf("%d",&Case);
    for (int ca=1;ca<=Case;ca++) {
        printf("Case #%d: ",ca);
        scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
        for (int i=1;i<=n;i++)
            scanf("%d%d%d",&p[i].x,&p[i].y,&p[i].w);
        sort(p+1,p+n+1,cmp);
        num=0;
        int start=0,end=p[1].x;
        for (int i=1;i<=n;i++) {
            q[++num].x=start;
            q[num].y=end;
            q[num].w=s;

            q[++num].x=p[i].x;
            q[num].y=p[i].y;
            q[num].w=s+p[i].w;

            start=p[i].y;
            end=p[i+1].x;
        }
        q[++num].x=start;
        q[num].y=x;
        q[num].w=s;
        sort(q+1,q+num+1,cmp2);
        
        double ans=0;
        for (int i=1;i<=num;i++) {
            int l=q[i].y-q[i].x;
            if (l==0) continue;
            if (dcmp(t)==0) {
                ans+=double(l)/double(q[i].w);
                continue;
            }
            double need=double(l)/double(q[i].w+(r-s));
            if (dcmp(t-need)>=0) {
                t-=need;
                ans+=need;
            }
            else {
                double run=(q[i].w+(r-s))*t;
                double lost=l-run;
                ans+=(lost/double(q[i].w))+t;
                t=0;
            }
        }
        printf("%.7f\n",ans);
    } 
}
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    display();
    return 0;
}

