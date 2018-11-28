#include<iostream>
using namespace std;
#define maxn 1100
long n,tst=1,tt;
long i,x;
long a[maxn];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    for (scanf("%ld",&tt);tst<=tt;tst++)
    {
        scanf("%ld",&n);
        x=0;
        for (i=0;i<n;i++)
        {
            scanf("%ld",&a[i]);
            x^=a[i];
        }
        printf("Case #%ld: ",tst);
        if (x!=0)
        {
           printf("NO\n");
           continue;
        }
        sort(a,a+n);
        x=0;
        for (i=1;i<n;i++) x+=a[i];
        printf("%ld\n",x);
    }
    return 0;
}
