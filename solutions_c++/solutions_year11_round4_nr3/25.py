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
vector<int> t;
#define MAX 1100000
bool p[MAX];
void pre(){
  for(int i=2;i<MAX;i++)p[i]=true;
  for(int i=2;i<MAX;i++)if(p[i]){t.push_back(i);for(int j=2*i;j<MAX;j+=i)p[j]=false;}
}
void solve(){
  int64 n;
  scanf("%lld",&n);
  int ans=n>1;
  for(int i=0;i<t.size();i++){
    int64 tmp=t[i];
    while(tmp<=n/t[i]){
      ++ans;
      tmp*=t[i];
    }
  }
  printf("%d\n",ans);
}
main(){
  pre();
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
