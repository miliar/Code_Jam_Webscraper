#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<cctype>
using namespace std;

typedef long long int64;
const int maxn=1<<11;
int m[maxn],p[maxn],a[12][maxn];
int vis[maxn];
int i,l,tt,n,k,ans;

void init()
  {
   scanf("%d",&n);
   for (int i=1;i<=1<<n;i++) {p[i]=i;scanf("%d",&m[i]);}
   k=(1<<n)/2;
   for (int i=0;i<n;i++)
     {
      for (int j=1;j<=k;j++)
        scanf("%d",&ans);
      k/=2;
     }
  }
  
bool cmp(const int &x,const int &y)
  {
   return m[x]<m[y];
  }
  
void solve()
  {
   sort(p+1,p+(1<<n)+1,cmp);
   memset(vis,0,sizeof(vis));
   ans=0;
   for (int j=1;j<=(1<<n);j++)
     {
      i=p[j];
      m[i]=n-m[i];
      k=((1<<n)+i-1)/2;l=0;
      while (k>0)
        {
         if (vis[k]) m[i]--; else l++; 
         k/=2;
        }
      if (m[i]<=0) continue;
      k=((1<<n)+i-1)/2;l-=m[i];
      while (k>0 && m[i])
        {
         if (!vis[k]) 
           {
            if (l<=0) {m[i]--;vis[k]=1;ans++;} else l--;
           } 
         k/=2;
        }
     }
  }
  
int main()
  {
   //freopen("match.in","r",stdin);
   //freopen("match.out","w",stdout);
   scanf("%d",&tt);
   for (int tot=1;tot<=tt;tot++)
     {
      init();
      solve();
      printf("Case #%d: %d\n",tot,ans);
     }
   return 0;
  }
