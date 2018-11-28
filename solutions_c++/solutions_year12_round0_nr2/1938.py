#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
long n,i,j,a,b,tst,k,t,ans;
long t2;
long s[300];
int main()
{
    freopen("Bin.txt","r",stdin);
    freopen("Bout.txt","w",stdout);
    for (scanf("%ld",&tst),k=1;  k<=tst;  k++)
    {
        scanf("%ld%ld%ld",&n, &a, &b);
        for (i=0;i<n;i++)
        {
            scanf("%ld",&s[i]);
        }
        sort(s,s+n);
        if (b==0) t=0;
        if (b==1) t=1;
        if (b>1) t=b+b+b-2;
        t2=t;
        if (b<=2) t=2;
           else t=b*3-4;
        ans=0;
        for (i=0;i<n;i++)
        {
            if (a>0)
            {
               if (s[i]>=t) ans++,a--;
               else if (s[i]>=t2) ans++;
            }
              else
            {
                if  (s[i]>=t2) ans++;
            }
        }
        printf("Case #%ld: %ld\n",k,ans);
    }
     return 0;
}
