#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int p[1000001],q[1000001];

int main()
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	
   int T;
   
   scanf("%d",&T);
   while (T--)
   {
      int L,n,C;
      long long t;
      
      cin>>L>>t>>n>>C;
      for (int i=1;i<=C;i++)
         scanf("%d",&p[i]);
      for (int i=C+1;i<=n;i++)
         p[i]=p[i-C];
        
      long long s=t>>1,all=0;
      
      int k=-1;
      
      for (int i=1;i<=n;i++)
      {
         all+=p[i];
         if (all>s)
         {
            k=i;
            break;
         }
      }
      
      static int id=0;
      
      printf("Case #%d: ",++id);
      if (k==-1)
         cout<<(all<<1)<<endl;
      else
      {
         int m=0;
         
         for (int i=k+1;i<=n;i++)
            q[++m]=p[i];
         q[++m]=all-s;
         sort(q+1,q+m+1);
         reverse(q+1,q+m+1);
         
         int now=0;
         long long ans=t;
         
         for (int i=1;i<=m;i++)
         {
            now++;
            int p=now<=L?1:2;
            ans+=q[i]*p;
         }
         cout<<ans<<endl;
      }
   }
   return 0;
}
