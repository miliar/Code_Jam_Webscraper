#include <iostream>
#include <cmath>

using namespace std;

typedef struct{double x,y,r;}around;

int t,n,i;
around a[4];

double dis(int x,int y)
{
       return (sqrt((a[x].x-a[y].x)*(a[x].x-a[y].x)+(a[x].y-a[y].y)*(a[x].y-a[y].y)));
}

double work()
{
       cin>>n;
       for (i=1;i<=n;i++)
       {
           cin>>a[i].x>>a[i].y>>a[i].r;
       }
       if (n==1)
       {
                return a[1].r*2;
       }
       if (n==2)
       {
                double d=dis(1,2);
                return (2*max(a[1].r,a[2].r));
       }
       if (n==3)
       {
                double d=dis(1,2),ans=1e99;
                ans=max(d+max(a[1].r-d,a[2].r)+max(a[2].r-d,a[1].r),a[3].r);
                d=dis(1,3);
                ans=min(ans,max(d+max(a[1].r-d,a[3].r)+max(a[3].r-d,a[1].r),a[2].r));
                d=dis(2,3);
                ans=min(ans,max(d+max(a[2].r-d,a[3].r)+max(a[3].r-d,a[2].r),a[1].r));
                return ans;
       }
}
                

int main()
{
    freopen("gcj4.in","r",stdin);
    freopen("gcj4.out","w",stdout);
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        double temp=work();
        printf("%.6lf\n",temp/2);
    }
    return 0;
}
