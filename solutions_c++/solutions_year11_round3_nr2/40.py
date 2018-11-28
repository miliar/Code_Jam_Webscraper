#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
int a[1000010],b[1000010];
int main()
{
   int T;
   scanf("%d",&T);
   while (T--)
   {
      int L,n,C;
      ll t;
      cin>>L>>t>>n>>C;
      for (int i=1;i<=C;i++)
         scanf("%d",&a[i]);
      for (int i=C+1;i<=n;i++)
         a[i]=a[i-C];
      ll s=t>>1,sum=0;
      int k=-1;
      for (int i=1;i<=n;i++)
      {
         sum+=a[i];
         if (sum>s)
         {
            k=i;
            break;
         }
      }
      static int id=0;
      printf("Case #%d: ",++id);
      if (k==-1)
         cout<<(sum<<1)<<endl;
      else
      {
         int m=0;
         for (int i=k+1;i<=n;i++)
            b[++m]=a[i];
         b[++m]=sum-s;
         sort(b+1,b+m+1);
         reverse(b+1,b+m+1);
         int now=0;
         ll ans=t;
         for (int i=1;i<=m;i++)
         {
            now++;
            int p=now<=L?1:2;
            ans+=b[i]*p;
         }
         cout<<ans<<endl;
      }
   }
   return(0);
}
