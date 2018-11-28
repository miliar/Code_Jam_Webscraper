#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
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
int n,next[2010],y[2010];
#define INF 1000000000
void go(int from,int to,int level=0){
  if(from==to)return;
  vector<int> t;
  int tmp=from;
  do{
    t.push_back(tmp);
    tmp=next[tmp];
  }while(tmp!=to);
  t.push_back(to);
  for(int i=1;i<t.size();i++)for(int j=t[i-1]+1;j<t[i];j++)if(next[j]>t[i])throw 0xdead;
  y[from]=y[to]-level*(to-from);
  for(int i=1;i<t.size();i++){
    y[t[i]]=y[to]-level*(to-t[i]);
    go(t[i-1]+1,t[i],level+1);
  }
}
void solve(){
  scanf("%d",&n);
  for(int i=1;i<n;i++){
    scanf("%d",&next[i]);
    assert(next[i]>i&&next[i]<=n);
  }
  y[n]=INF;
  try{
  go(1,n);
  for(int i=1;i<n;i++){
    for(int j=i+1;j<next[i];j++)assert((int64)y[j]*(next[i]-i)<(int64)y[i]*(next[i]-j)+(int64)y[next[i]]*(j-i));
    //for(int j=next[i]+1;j<=n;j++)assert((int64)y[j]*(next[i]-i)<=(int64)y[i]*(next[i]-j)+(int64)y[next[i]]*(j-i));
  }
  for(int i=1;i<=n;i++)assert(y[i]>1000000); 
  for(int i=1;i<n;i++)printf("%d ",y[i]);
  printf("%d\n",y[n]);
  }catch(...){
    printf("Impossible\n");
  }
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

