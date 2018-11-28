#include<cstdio>
#include<algorithm>
#include<vector>
#include<numeric>
#include<map>
#include<set>
#include<cstdlib>
#include<string>
#include<cassert>
#include<iostream>
using namespace std;
typedef vector<int> vi;
typedef long long int64;
#define FOR(i,n)for(int i=0;i<(int)(n);i++)
char t[510][510];
int R,C;
int64 val[510][510],valX[510][510],valY[510][510],sumX[510][510],sumY[510][510],sum[510][510];
bool check(int K){
  for(int i=0;i+K<=R;i++)for(int j=0;j+K<=C;j++){
    int64 tX=sumX[i][j]-sumX[i+K][j]-sumX[i][j+K]+sumX[i+K][j+K];
    int64 tY=sumY[i][j]-sumY[i+K][j]-sumY[i][j+K]+sumY[i+K][j+K];
    tX-=valX[i][j]+valX[i+K-1][j]+valX[i][j+K-1]+valX[i+K-1][j+K-1];
    tY-=valY[i][j]+valY[i+K-1][j]+valY[i][j+K-1]+valY[i+K-1][j+K-1];
    int64 t=sum[i][j]-sum[i+K][j]-sum[i][j+K]+sum[i+K][j+K];
    t-=val[i][j]+val[i+K-1][j]+val[i][j+K-1]+val[i+K-1][j+K-1];
    int64 dX=2*i+K-1,dY=2*j+K-1;
//cout<<i<<" "<<j<<" "<<tX<<" "<<tY<<" "<<t<<" "<<dX<<" "<<dY<<endl;
    if(tX==t*dX&&tY==t*dY)return true;
  }
  return false;
}
void solve(){
  scanf("%d %d %*d",&R,&C);
  FOR(i,R)scanf(" %s",t[i]);
  memset(sumX,0,sizeof(sumX));
  memset(sumY,0,sizeof(sumY));
  memset(sum,0,sizeof(sum));
  for(int i=R-1;i>=0;i--)for(int j=C-1;j>=0;j--){
    int add=t[i][j]-'0';
    valX[i][j]=add*2*i;
    valY[i][j]=add*2*j;
    val[i][j]=add;
    sum[i][j]=sum[i+1][j]+sum[i][j+1]-sum[i+1][j+1]+val[i][j];
    sumX[i][j]=sumX[i+1][j]+sumX[i][j+1]-sumX[i+1][j+1]+valX[i][j];
    sumY[i][j]=sumY[i+1][j]+sumY[i][j+1]-sumY[i+1][j+1]+valY[i][j];
  }
  int K=500;
  while(K>=3&&!check(K))K--;
  if(K<3)puts("IMPOSSIBLE");else printf("%d\n",K);
}
main(){
  char in[100],out[100],*pos;
  strcpy(in,__FILE__);
  strcpy(out,__FILE__);
  pos=in;
  while(*pos!='.')pos++;
  strcpy(pos,".in");
  pos=out;
  while(*pos!='.')pos++;
  strcpy(pos,".out");
  freopen(in,"r",stdin);
  freopen(out,"w",stdout);
  int t;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    fprintf(stderr,"processing case %d\n",tt);
    printf("Case #%d: ",tt);
    solve();
    fflush(stdout);
  }
  freopen(out,"r",stdin);
  char c;while((c=getc(stdin))!=EOF)putc(c,stderr);
}
