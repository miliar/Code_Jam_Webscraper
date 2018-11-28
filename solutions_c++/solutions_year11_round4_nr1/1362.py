#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

struct node
{
    int l,v;
}a[1005];
bool cmp(node u,node v)
{
    return u.v<v.v;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        int X,w,r,t,n;
        scanf("%d%d%d%d%d",&X,&w,&r,&t,&n);
        int tot=0;
        for (int i=1;i<=n;i++)
        {
            int x,y,z;
            scanf("%d%d%d",&x,&y,&z);
            a[i].l=y-x;a[i].v=z;
            tot+=y-x;
        }
        a[0].l=X-tot;a[0].v=0;
        sort(a,a+n+1,cmp);
        double now=(double)t;
        double sum=0;
        for (int i=0;i<=n;i++)
        {
            if (now>0 && now*(double)(r+a[i].v)>=(double)a[i].l)
            {
                now-=(double)a[i].l/(double)(r+a[i].v);
                sum+=(double)a[i].l/(double)(r+a[i].v);
            }
            else if (now>0 && now*(double)(r+a[i].v)<(double)a[i].l)
            {
                sum+=(double)(a[i].l-now*(r+a[i].v))/(double)(w+a[i].v);
                sum+=now;
                now=0;
            }
            else if (now<=0) sum+=(double)a[i].l/(double)(w+a[i].v);
        }
        printf("Case #%d: %.10lf\n",cas,sum);

    }
}
