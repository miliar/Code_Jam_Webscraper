#include<cstdio>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<string>
#include<utility>
using namespace std;

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

int main(){
  int i,j,k,l,m,n,q;
  char tmp[400]; string ss;
  int opt[2000], next[2000], mn;
  map<string,int> ind;

  int size,count=0;

  gets(tmp); size=atoi(tmp);
  while(size--){
    gets(tmp); n=atoi(tmp); ind.clear();
    rep(i,n) {gets(tmp); ss=tmp; ind[ss]=i;}
    rep(i,n) opt[i]=0;
    gets(tmp); q=atoi(tmp);
    while(q--){
      gets(tmp); ss=tmp; k=ind[ss];
      rep(i,n){
        next[i]=opt[i];
        rep(j,n) if(next[i]>opt[j]+1) next[i]=opt[j]+1;
      }
      next[k]=10000;
      rep(i,n) opt[i]=next[i];
    }
    mn=10000; rep(i,n) if(mn>opt[i]) mn=opt[i];
    printf("Case #%d: %d\n",++count,mn);
  }
  
  return 0;
}
