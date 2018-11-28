/* Writen by Filip Hlasek 2011 */
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
#define MAXN 1111

using namespace std;

typedef struct ww{
  int w;
  double len;
}WW;

WW W[MAXN];
int X,S,R,N,B,E;
double t;

bool mycompare(WW a, WW b){ return a.w<b.w; }

int main(int argc, char *argv[]){
  int T,i,TT;
  double result,run;
  scanf("%d",&T);
  FOR(TT,T){
    scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
    FOR(i,N){
      scanf("%d%d%d",&B,&E,&(W[i].w));
      W[i].len=E-B;
      X-=E-B;
    }
    W[N].w=0;
    W[N++].len=X;
    sort(W,W+N,mycompare);
    int i=0;
    result=0;
    while(i<N&&t>0){
      //printf("i:%d t:%lf result:%lf\n",i,t,result);
      run=W[i].len/(R+W[i].w);
      if(run<t){
        result+=run;
        t-=run;
        i++;
      }
      else{
        result+=t;
        W[i].len-=(R+W[i].w)*t;
        t=-1;
      }
    }
    //printf("i:%d t:%lf result:%lf len:%lf\n",i,t,result,W[i].len);
    for(;i<N;i++) result+=W[i].len/(S+W[i].w);
    printf("Case #%d: %.10lf\n",TT+1,result);
  }
  return 0;
}
