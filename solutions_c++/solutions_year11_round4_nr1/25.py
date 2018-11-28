#include<iostream>
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
void solve(){
  int X,S,R,N,B[1010],E[1010],len[1010],w[1010];
  double t;
  scanf("%d %d %d %lf %d",&X,&S,&R,&t,&N);
  FOR(i,N)scanf("%d %d %d",&B[i],&E[i],&w[i]);
  FOR(i,N)X-=E[i]-B[i];
  FOR(i,N)len[i]=E[i]-B[i],w[i]+=S;
  len[N]=X;w[N]=S;
  R-=S;
  ++N;
  FOR(i,N)for(int j=i+1;j<N;j++)if(w[j]<w[i]){
    swap(w[i],w[j]);
    swap(len[i],len[j]);
  }
  double ans=0;
  FOR(i,N){
    double from=0,to=len[i];
    FOR(z,200){
      double middle=(from+to)/2;
      double tmp=middle/(w[i]+R);
      if(tmp<=t)from=middle;else to=middle;
    }
    t-=from/(w[i]+R);
    ans+=from/(w[i]+R);
    ans+=(len[i]-from)/w[i];
  }
  printf("%.8lf\n",ans);
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
