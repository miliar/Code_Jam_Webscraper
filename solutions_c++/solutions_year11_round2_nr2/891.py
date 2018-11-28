/*

*/
#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
int Case,n;
double d,Max;
struct data {
    int v;
    double s,l,r,len;
} p[310];
bool flag;
int dcmp(double x)
{
    if (fabs(x)<1e-7) return 0;
    return x>0?1:-1;
}
void display()
{
    scanf("%d",&Case);
    for (int ca=1;ca<=Case;ca++) {
        printf("Case #%d: ",ca);
        scanf("%d%lf",&n,&d);
        for (int i=1;i<=n;i++) {
            scanf("%lf%d",&p[i].s,&p[i].v);
            int t=p[i].v/2;
            if (p[i].v%2==0) {
                p[i].l=p[i].s-((t-1)*d+d/2);
                p[i].r=p[i].s+((t-1)*d+d/2);
            }
            else {
                p[i].l=p[i].s-(t*d);
                p[i].r=p[i].s+(t*d);
            }
            p[i].len=(p[i].v-1)*d;
        }
        while (1) {
            flag=false;
            //for (int i=1;i<=n;i++)
                //printf("(%.2f,%.2f,%.2f) ",p[i].s,p[i].l,p[i].r);
            //printf("%.2f\n",d);
            //int t=10000;
            //while (t--);
            for (int i=1;i<=n;i++) {
                if (flag) break;
                for (int j=i+1;j<=n;j++) {
                    double D=0;
                    for (int k=i+1;k<j;k++)
                        D+=d*(p[k].v);
                    D+=d;
                    double l=p[j].l-p[i].r,llen,rlen;
                    if (dcmp(l-D)>=0) continue;
                    l=D-l;
                    llen=p[i].s-p[i].l;
                    rlen=p[j].r-p[j].s;
                    if (dcmp(llen-rlen)<0) {
                        llen+=l;
                        if (dcmp(llen-rlen)>0) {
                            l=(llen-rlen);
                            llen=rlen;
                            llen+=l/2.0;
                            rlen+=l/2.0;
                        }
                    }
                    else {
                        rlen+=l;
                        if (dcmp(rlen-llen)>0) {
                            l=(rlen-llen);
                            rlen=llen;
                            llen+=l/2.0;
                            rlen+=l/2.0;
                        }
                    }
                    p[i].l=p[i].s-llen;
                    p[i].r=p[i].s+(p[i].len-llen);
                    p[j].r=p[j].s+rlen;
                    p[j].l=p[j].s-(p[j].len-rlen);
                    flag=true;
                    break;
                }
            }
            if (!flag) break;
        }
        double Max=0;
        for (int i=1;i<=n;i++)
            Max=max(Max,max(p[i].s-p[i].l,p[i].r-p[i].s));
        printf("%.6f\n",Max);
    }
}
int main()
{
    //freopen("b.in","r",stdin);
    //freopen("B-small-attempt2.in","r",stdin);
    //freopen("B-small-attempt2.out","w",stdout);
    display();
    return 0;
}

