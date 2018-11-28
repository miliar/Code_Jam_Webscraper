#include <iostream>
using namespace std;
struct def{
    int a,b;
}f[1000];
bool cmp(def a,def b)
{
    return (a.a<b.a||(a.a==b.a&&a.b<b.b));
}
int main()
{
    freopen("C:/Users/FengJinwen/Desktop/A-large.in", "r", stdin);
    freopen("C:/Users/FengJinwen/Desktop/ans.txt", "w", stdout);
    int n,t,p;
    int i,j,ans;
    scanf("%d",&t);
    for (p=1;p<=t;p++)
    {
        ans=0;
        scanf("%d",&n);
        for (i=1;i<=n;i++)
            scanf("%d%d",&f[i].a,&f[i].b);
        sort(f+1,f+1+n,cmp);
        for (i=1;i<n;i++)
          for (j=i+1;j<=n;j++)
        {
            if (f[i].b>=f[j].b) ans++;
        }
        printf("Case #%d: %d\n",p,ans);
    }
}
