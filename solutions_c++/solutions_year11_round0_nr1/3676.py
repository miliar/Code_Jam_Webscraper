#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <algorithm>
#include <cmath>

#define FOR(i,n) for(i=0;i<n;i++)
#define MAXN 111

using namespace std;

int o[MAXN],oi[MAXN],O,b[MAXN],bi[MAXN],B;

int main(int argc, char *argv[]){
  int t,T,i,ii,x,oo,bb,op,bp,tmp,N;
  char c[5];
  scanf("%d",&T);
  FOR(t,T){
    scanf("%d",&N);
    O=0; B=0;
    FOR(i,N){
      scanf("%s %d",c,&x);
      if(c[0]=='O'){ oi[O]=i; o[O++]=x; }
      else{ bi[B]=i; b[B++]=x; }
    }
    for(i=0,ii=0,oo=0,bb=0,op=1,bp=1;ii!=N;i++){
      tmp=0;
      if(oo<O){
        if(oi[oo]==ii&&op==o[oo]){ oo++; tmp++;}
        else{
          if(o[oo]>op) op++;
          if(o[oo]<op) op--;
        }
      }
      if(bb<B){
        if(bi[bb]==ii&&bp==b[bb]){ bb++; tmp++;}
        else{
          if(b[bb]>bp) bp++;
          if(b[bb]<bp) bp--;
        }
      }
      ii+=tmp;
    }
    printf("Case #%d: %d\n",t+1,i);
  }
  return 0;
}
