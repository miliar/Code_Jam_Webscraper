#include<iostream>
using namespace std;
#define maxn 1100
long n,i,j,tst=1,tt,ans,t;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    for (scanf("%ld",&tt);tst<=tt;tst++)
    {
        scanf("%ld",&n);
        ans=0;
        for (i=1;i<=n;i++)
        {
            scanf("%ld",&t);
            if (t!=i) ans++;
        }
        printf("Case #%ld: %.6lf\n",tst,(double)ans);
    }
    return 0;
}
