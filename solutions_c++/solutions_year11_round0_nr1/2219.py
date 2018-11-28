#include<iostream>
#include<cstring>
using namespace std;

const int maxn=111;
char c[maxn];
int a[maxn];
int tt,n,m,x,y,k,d,f,ans;

void init()
  {
   scanf("%d",&n);
   for (int i=0;i<n;i++)
     {
      scanf("%c",&c[i]);scanf("%c",&c[i]);
      scanf("%d",&a[i]);
     }
   scanf("\n");
  }
  
void solve()
  {
   x=y=1;
   d=f=ans=0;
   for (int i=0;i<n;i++) if (c[i]=='O') {d=a[i];break;}  
   for (int i=0;i<n;i++) if (c[i]=='B') {f=a[i];break;}  
   for (int i=0;i<n;i++)
     {
      if (c[i]=='O')
        {
         k=abs(a[i]-x)+1;
         ans+=abs(a[i]-x)+1;
         x=a[i];
         d=0;for (int j=i+1;j<n;j++) if (c[j]=='O') {d=a[j];break;}
         if (!f) continue;
         if (abs(y-f)<=k) y=f; else y+=((y>f)?-1:1)*k;
        }
      else
        {
         k=abs(a[i]-y)+1;
         ans+=abs(a[i]-y)+1;
         y=a[i];
         f=0;for (int j=i+1;j<n;j++) if (c[j]=='B') {f=a[j];break;}
         if (!d) continue;
         if (abs(x-d)<=k) x=d; else x+=((x>d)?-1:1)*k;
        }
     }
  }
  
int main()
  {
   freopen("A.in","r",stdin);
   freopen("A.out","w",stdout);
   scanf("%d\n",&tt);
   for (int t=1;t<=tt;t++)
     {
      init();
      solve();
      printf("Case #%d: %d\n",t,ans);
     }
   return 0;
  }
