#include<iostream>
using namespace std;

typedef long long int64;
const int maxn=1010;
int64 s[maxn];
int g[maxn],a[maxn];
int n,t,k,m,tt,l,r,mid,x;
int64 ans,res,tot;

int64 solve()
  {
   memset(g,255,sizeof(g));
   tot=0;a[g[1]=0]=0;
   for (int i=1;i<=t;i++)
     {
      if (s[n]-s[x-1]>=k)
        {
         l=x;r=n;
         while (l<=r)
           {
            mid=(l+r)/2;
            if (s[mid]-s[x-1]>k) r=mid-1; else l=mid+1;
           }
         m=s[r]-s[x-1];
         x=r;
        }
      else 
        {
         m=s[n]-s[x-1];
         l=1;r=x-1;
         while (l<=r)
           {
            mid=(l+r)/2;
            if (m+s[mid]>k) r=mid-1; else l=mid+1;
           }
         m+=s[r];
         x=r;
        }
      if (x==n) x=1; else x++;
      a[i]=m;
      if (g[x]!=-1) 
        {
         l=i-g[x];
         for (int j=1;j<=g[x];j++) ans+=a[j];
         res=0;for (int j=g[x]+1;j<=i;j++) res+=a[j];
         r=t-g[x];ans+=res*(r/l);
         r%=l;
         for (int j=g[x]+1;j<=g[x]+r;j++) ans+=a[j];
         return ans;
        } 
      g[x]=i;
      tot+=m;
     }      
   return tot; 
  }
  
int main()
  {
   //freopen("park.in","r",stdin);
   //freopen("park.out","w",stdout);
   scanf("%d",&tt);
   for (int ii=1;ii<=tt;ii++)
     {
      scanf("%d%d%d",&t,&k,&n);
      ans=s[0]=0;x=1;
      for (int i=1;i<=n;i++)
        {
         scanf("%d",&m);
         s[i]=s[i-1]+m;
        }
      printf("Case #%d: %I64d\n",ii,solve());
     }
   return 0;
  }
