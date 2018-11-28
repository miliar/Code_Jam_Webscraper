#include <cstdio>
#include <cstring>
#define Min(a,b) ((a)<(b)?(a):(b))
using namespace std;
int d[100005]={0},L[100005]={0};
int z[100005]={0};
int h,t;
int main()
{int n,m,i,j,k,l,T,tt,D;
 freopen("A.in","r",stdin);
 freopen("A.out","w",stdout);
 scanf("%d",&T);
 tt=0;
 while(T--)
 {h=0;t=0;tt++;
  scanf("%d",&n);
  for(i=1;i<=n;i++)
  {scanf("%d%d",&d[i],&L[i]);
  }
  scanf("%d",&D);
  d[n+1]=D;L[n+1]=0;
  t=1;
  z[1]=d[1];
  for(i=1;i<=n+1;i++)
  if(i<=t)
  {while(t<=n&&d[t+1]-d[i]<=z[i])
   {t++;
    z[t]=Min(d[t]-d[i],L[t]);
   }
  }else break;
  printf("Case #%d: ",tt);
  if(i<=n+1)printf("NO\n");
  else printf("YES\n");
 }
 return 0;
}
