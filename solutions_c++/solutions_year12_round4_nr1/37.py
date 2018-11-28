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
#define MAX 10100
#define INF 2000000000
int n,d[MAX],len[MAX],D,best[MAX];
void solve(){
  scanf("%d",&n);
  for(int i=0;i<n;i++)scanf("%d %d",&d[i],&len[i]);
  scanf("%d",&D);
  for(int i=0;i<n;i++)best[i]=-INF;
  best[0]=d[0];
  for(int i=0;i<n;i++)if(best[i]>0){
    for(int j=i+1;j<n&&d[j]<=d[i]+best[i];j++){
      best[j]=max(best[j],min(len[j],d[j]-d[i]));
    }
  }
  bool ok=false;
  for(int i=0;i<n;i++)if(d[i]+best[i]>=D)ok=true;
  printf(ok?"YES\n":"NO\n");
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

