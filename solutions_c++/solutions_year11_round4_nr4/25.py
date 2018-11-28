#include<cstdio>
#include<algorithm>
#include<vector>
#include<numeric>
#include<map>
#include<set>
#include<cstdlib>
#include<string>
#include<cassert>
using namespace std;
typedef vector<int> vi;
typedef long long int64;
#define FOR(i,n)for(int i=0;i<(int)(n);i++)
int n,m,d[410][410],t[410][410];
bool e[410][410];
vi s[410];
#define INF 1000000000
int calc(int prev,int cur){//fprintf(stderr,"%d %d (%d %d)\n",prev,cur,d[0][prev],d[0][cur]);
  if(t[prev][cur]<INF)return t[prev][cur];
  if(e[cur][1])return 0;
  int ans=-INF;
  FOR(i,s[cur].size()){
    int next=s[cur][i];
    if(d[next][1]!=d[cur][1]-1)continue;
    int tmp=calc(cur,next)-1;
    FOR(k,n)tmp+=k!=prev&&k!=cur&&k!=next&&(!e[prev][k]&&!e[cur][k]&&e[next][k]); 
    ans=max(ans,tmp);
  }
  return t[prev][cur]=ans;
}
void solve(){
  scanf("%d %d",&n,&m);
  memset(e,0,sizeof(e));
  FOR(i,n)s[i].clear();
  FOR(i,m){
    int x,y;
    scanf("%d,%d",&x,&y);
    s[x].push_back(y);
    s[y].push_back(x);
    e[x][y]=e[y][x]=true;
  }
  FOR(i,n)FOR(j,n)d[i][j]=i==j?0:e[i][j]?1:INF;
  FOR(k,n)FOR(i,n)FOR(j,n)d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
  if(d[0][1]==1){
    printf("%d %d\n",0,(int)s[0].size());
    return;
  }
  FOR(i,n)FOR(j,n)t[i][j]=INF;
  int ans=0;
  for(int i=2;i<n;i++)if(e[0][i]&&d[0][1]==d[0][i]+d[i][1]){
    int cur=calc(0,i);
    FOR(k,n)cur+=k&&k!=i&&(e[0][k]||e[i][k]);
    ans=max(ans,cur);
  }
  printf("%d %d\n",d[0][1]-1,ans);
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
