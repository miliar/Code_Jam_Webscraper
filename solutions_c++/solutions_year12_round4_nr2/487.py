#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int r[1005]={0};
struct point 
{int r,zx;}
zz[1005];
bool cmp(point a,point b)
{return a.r<b.r;}
int hash[1005]={0},H;
int n,X[1005]={0},Y[1005]={0};
int ansx[1005]={0},ansy[1005]={0};
void dfs(int W,int x0)
{int fl=0;
 int i,j,k;
 for(i=n;i>=1;i--)
  if(!hash[i])break;
 if(i<=0)return ;
 if(i==n)
 {X[i]=0;
  Y[i]=0;
  k=r[i];
  hash[i]=1;
  for(j=n;j>=1;j--)
   if(!hash[j]&&k+r[j]<=H)
   {Y[j]=k+r[j];
    X[j]=0;
    k+=2*r[j];
    hash[j]=1;
   }
  dfs(W,r[i]);
 }else
 {X[i]=x0+r[i];
  Y[i]=0;
  k=r[i];
  hash[i]=1;
  for(j=n;j>=1;j--)
   if(!hash[j]&&k+r[j]<=H)
   {Y[j]=k+r[j];
    X[j]=x0+r[i];
    k+=2*r[j];
    hash[j]=1;
   }
  dfs(W,x0+2*r[i]);
 }
 return ;
} 
int main()
{int m,i,j,k,l,T,tt,W;
 freopen("B.in","r",stdin);
 freopen("B.out","w",stdout);
 scanf("%d",&T);
 tt=0;
 while(T--)
 {tt++;
  scanf("%d%d%d",&n,&W,&H);
  for(i=1;i<=n;i++)
  {scanf("%d",&r[i]);
   zz[i].r=r[i];
   zz[i].zx=i;
  }
  sort(zz+1,zz+n+1,cmp);
  for(i=1;i<=n;i++)r[i]=zz[i].r;
  memset(hash,0,sizeof(hash));
  dfs(W,0);
  printf("Case #%d:",tt);
  for(i=1;i<=n;i++)
  {ansx[zz[i].zx]=X[i];ansy[zz[i].zx]=Y[i];}
  for(i=1;i<=n;i++)if(X[i]>=W)
  {printf("AA");}
  for(i=1;i<=n;i++)printf(" %d %d",ansx[i],ansy[i]);
  printf("\n");
 }
 return 0;
}
