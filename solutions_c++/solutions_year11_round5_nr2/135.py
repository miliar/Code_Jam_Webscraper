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

#define MAX 41000
int N,t[MAX],sum[MAX],cur[MAX];
bool ok(int b){
  FOR(i,MAX)cur[i]=0;
  int finished=0;
  FOR(i,MAX){
    finished+=cur[0];
    FOR(j,b-1)cur[j]=cur[j+1];
    int total=0;FOR(j,b-1)total+=cur[j];
    if(total>sum[i])return false;
    int need=sum[i]-total;
    finished=min(finished,need);
    cur[b-1]=need-finished; 
  }
  return true;
}
void solve(){
  scanf("%d",&N);
  FOR(i,N)scanf("%d",&t[i]);
  if(!N){puts("0");return;}
  FOR(i,MAX)sum[i]=0;
  FOR(i,N)++sum[t[i]];
  int from=1,to=10100;
  assert(ok(1));
  while(from+1<to){
    int middle=(from+to)/2;
    if(ok(middle))from=middle;else to=middle;
  }
  printf("%d\n",from);
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
