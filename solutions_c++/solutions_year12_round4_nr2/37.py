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
double draw(){
  return (double)rand()/RAND_MAX;
}
double sqr(double x){
  return x*x;
}
int n,r[1010],W,L,p[1010];
double x[1010],y[1010];
void solve(){
  scanf("%d %d %d",&n,&W,&L);
  for(int i=0;i<n;i++)scanf("%d",&r[i]);
  double sum=0;
  for(int i=0;i<n;i++)sum+=sqr(r[i]);
  fprintf(stderr,"%.6lf >= %.6lf\n",(double)W*L,5*M_PI*sum);
  assert((double)W*L>=5*M_PI*sum);
  for(int i=0;i<n;i++)p[i]=i;
  while(1){
    random_shuffle(p,p+n);
    for(int i=0;i<n;i++){
      x[p[i]]=(double)draw()*W;
      y[p[i]]=0;
#define EPS 1e-9
      for(int j=0;j<i;j++){
        double tmp=sqr(r[p[i]]+r[p[j]])-sqr(x[p[i]]-x[p[j]]);
        if(tmp<EPS)continue;
        tmp=sqrt(tmp);
        y[p[i]]=max(y[p[i]],y[p[j]]+tmp+1e-3);
      }
      if(y[p[i]]>L)goto fail;
    }
    for(int i=0;i<n;i++)for(int j=0;j<i;j++){
      double dist=sqr(x[i]-x[j])+sqr(y[i]-y[j]);
      assert(dist>r[i]+r[j]);
    }
    for(int i=0;i<n;i++)printf("%.6lf %.6lf%c",x[i],y[i],i+1<n?' ':'\n');
    return;
fail:
    fprintf(stderr,"FAIL for n=%d\n",n);
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

