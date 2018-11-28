#include<iostream>
#include<map>
using namespace std;
#define maxn 2000
map<long,long>s;
map<long,long>::iterator t;
long n,x,i,j,l,r,p;
long a[maxn],ans;
long cas,tst;
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.txt","w",stdout);
    for (scanf("%ld",&cas),tst=1;tst<=cas;tst++)
    {
        ans=0x7fffffff;
        s.clear();
        scanf("%ld",&n);
        for (i=0;i<n;i++)
        {
            scanf("%ld",&x);
            s[x]++;
        }
        l=r=0;
        p=0x7fffffff;
        s[p]++;
        for (t=s.begin();t!=s.end();t++)
        {
            if (t->first==p+1)
            {
               for (i=r-1,x=0;i>=l && x<(t->second);i--,x++) a[i]++;
               if (i>=l && ans>a[i]) ans=a[i];
               l=i+1;
               while (x<(t->second))
               {
                  a[r]=1;
                  r++;
                  x++;
               }
            }
            else
            {
               i=r-1;
               if (i>=l && ans>a[i]) ans=a[i];
               l=r;
               x=0;
               while (x<(t->second))
               {
                  a[r]=1;
                  r++;
                  x++;
               }
            }
            p=t->first;
        }
        if (n==0) ans=0;
        printf("Case #%ld: %ld\n",tst,ans);
    }
//    system("PAUSE");
    return 0;
}
