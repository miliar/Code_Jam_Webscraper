#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;
typedef long long ll;
int a[1000010];
bool f[1000010];
int main()
{
   for (int i=2;i<=1000;i++)
   {
      if (f[i])
         continue;
      for (int j=i;i*j<=1000000;j++)
         f[i*j]=true;
   }
   for (int i=2;i<=1000000;i++)
      if (!f[i])
         a[++a[0]]=i;
   int T;
   scanf("%d",&T);
   while (T--)
   {
      ll n,ans=0;
      cin>>n;
      for (int i=1;i<=a[0];i++)
      {
         if (ll(a[i])*a[i]>n)
            break;
         ll now=a[i];
         for (int j=1;;j++)
         {
            now*=a[i];
            if (now>n)
            {
               ans+=j-1;
               break;
            }
         }
      }
      if (n>1)
         ans++;
      static int id=0;
      printf("Case #%d: ",++id);
      cout<<ans<<endl;
   }
   return(0);
}
