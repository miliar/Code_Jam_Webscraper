#include<iostream>
#include<cstring>
using namespace std;

typedef long long int64;

const int maxn=1010;
int64 a[maxn],s[maxn];
int b[maxn];
bool vis[maxn];
int64 sum,ans;
int n,c,L,k,T;
int64 t;

void init()
  {
   scanf("%d%I64d%d%d",&L,&t,&n,&c);
   sum=0;for (int i=1;i<=c;i++) {scanf("%I64d",&a[i]);a[i]=a[i]*2;s[i]=s[i-1]+a[i];sum+=a[i];}
  }
  
int64 calc(int t)
  {
   return sum*(t/c)+s[t%c];
  }
  
void solve()
  {
   int l=1,r=n,mid;
   for (;l<=r;mid=(l+r)/2,calc(mid)<=t?l=mid+1:r=mid-1);
   ans=calc(r);
   for (int i=1;i<=c;i++) {b[i]=n/c;if (n%c>=i) b[i]++;b[i]-=r/c;if (r%c>=i) b[i]--;}
   if (r+1<=n)
     {
      k=(r+1)%c;if (!k) k=c;
      b[k]--;
      b[++c]=1;a[c]=a[k]-t+ans;
      ans=t;
     }
   for (int i=1;i<=c;i++) ans+=int64(b[i])*a[i];
   memset(vis,0,sizeof(vis));
   while (L)
     {
      k=0;
      for (int i=1;i<=c;i++) if (!vis[i] && (!k || a[i]>a[k])) k=i;
      if (!k) break;
      vis[k]=true;
      ans-=int64(a[k])/2*(L-max(L-b[k],0));
      L=max(L-b[k],0);
     }
  }
  
int main()
  {
   freopen("B.in","r",stdin);
   freopen("B.out","w",stdout);
   scanf("%d",&T);
   for (int tt=1;tt<=T;tt++)
     {
      init();
      solve();
      printf("Case #%d: %I64d\n",tt,ans);
     }
   return 0;
  }
