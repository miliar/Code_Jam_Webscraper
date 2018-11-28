#include <iostream>
#include <cstring>
#define maxn 500000000
#define N 2048
  using namespace std;
  int pw[]={1,2,4,8,16,32,64,128,256,512,1024};
  int n,a[11][N],g[N],f[11][N][11],ans,p;
int dp(int dep,int x,int zt){
  if(f[dep][x][zt]>=0){
    return f[dep][x][zt];
    };
  int i,j,k,y;
  i=dp(dep+1,x+x,zt)+dp(dep+1,x+x+1,zt)+a[dep][x];
  k=dp(dep+1,x+x,zt+1)+dp(dep+1,x+x+1,zt+1);
  if(k>maxn)k=maxn;
  if(k>i)k=i;
  return f[dep][x][zt]=k;
};
int main(){
  freopen("b.in","r",stdin);freopen("b.out","w",stdout);
  int i,j,k,x,y,tst,tt;
  scanf("%d\n",&tst);
  for(tt=1;tt<=tst;tt++){
    printf("Case #%d: ",tt);
    scanf("%d\n",&p);
    n=pw[p];
    for(i=0;i<n;i++)scanf("%d",&g[i]);
    k=0;
    for(i=p-1;i>=0;i--)
    for(j=0;j<pw[i];j++){scanf("%d",&a[i][j]);k+=a[i][j];};
    memset(f,255,sizeof(f));
    for(i=0;i<n;i++)
    for(j=0;j<=p;j++){
      if(j>g[i])f[p][i][j]=maxn;
      else f[p][i][j]=0;
      };
    k=dp(0,0,0);
    cout<<k<<endl;
    };
  return 0;
};
  
