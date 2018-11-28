#include<iostream>
using namespace std;
int i,j,t,a[1005],now,now1,now2,r,k,n,ans;

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&t);
    for (i=1;i<=t;i++)
    {
        scanf("%d %d %d",&r,&k,&n);
        for (j=1;j<=n;j++) scanf("%d",&a[j]);
        now=1;ans=0;now1=a[1];now2=1;
        while (r)
        {
              now++;
              if (now>n) now=1;
              if (now1+a[now]<=k&&now!=now2) now1+=a[now];
              else {ans+=now1;now1=a[now];now2=now;r--;}
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
