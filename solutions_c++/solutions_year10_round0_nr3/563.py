#include <cstdlib>
#include <iostream>

using namespace std;

int t,r,k,n;
   
int gs[1024];
int next[1024];
long long sums[1024];

void make_cycles()
{
   long long ps=0;
   int j=0;
   for(int i=0;i<n;i++)
   {
      while(j<n&&ps<=k)
         ps+=(long long)gs[j++];
      if(j==n) j=0;
      while(j<i&&ps<=k)
         ps+=(long long)gs[j++];
      if(j>0&&ps>k)
         ps-=(long long)gs[--j];
      else if(j==0&&ps>k)
         {
            j=n-1;
            ps-=(long long)gs[j];
         }
      next[i]=j;
      sums[i]=ps;
      ps-=gs[i];
   }
}


int main()
{

   scanf("%d",&t);
   for(int p=0;p<t;p++)
   {
      scanf("%d%d%d",&r,&k,&n);
      for(int i=0;i<n;i++)
         scanf("%d",&gs[i]);

      make_cycles();
      long long ret=0;
      int j=0;
      for(int i=0;i<r;i++)
      {
         ret+=(long long)sums[j];
         j=next[j];
      }
      printf("Case #%d: %lld\n",p+1,ret);


   }

   return 0;
}
