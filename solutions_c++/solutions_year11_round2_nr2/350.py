#include <iostream>
#include <cmath>
using namespace std;

int tp[300],c[300];
double p[300];
int n,d;

int main()
{
    freopen("b2.in","r",stdin);
    freopen("b2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&n,&d);
        int sum=0;
        for (int i=1;i<=n;i++)
        {
            scanf("%d%d",tp+i,c+i);
            sum+=c[i];
        }
        for (int i=1;i<=n;i++) p[i]=tp[i];
        double L=0,R=double(sum)*double(d);
        int run=0;
        while (L+1e-3<=R)
        {
              run++;
             double mid=(L+R)/2;
             double st;
             bool ok=1;
             for (int i=1;i<=n;i++)
             {
                 double t;
                 if (i>1) t=max(st+d,p[i]-mid);
                 else t=p[i]-mid;
                 t=t+double(c[i]-1)*double(d);
                 if (t>p[i]+mid)
                 {
                     ok=0;
                     break;
                 }
                 st=t;
             }
             if (ok) R=mid;
             else L=mid;
        }
        printf("Case #%d: %.7lf\n",cas,floor(L*2+0.1)/2);
    }       
}
                         
                         
        
