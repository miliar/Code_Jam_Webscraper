/* Writen by Filip Hlasek 2012 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<b;i++)

using namespace std;

#define MAXN 1111
int x[MAXN], y[MAXN], r[MAXN], o[MAXN];
int W,L,N;

void place(int nn){
  int n = o[nn];
  while(true){
    x[n] = ((long long)rand() * rand()) % (W+1);
    y[n] = ((long long)rand() * rand()) % (L+1);
    bool ok = true;
    REP(ii,nn){
      int i = o[ii];
      if((long long)(x[i]-x[n])*(x[i]-x[n]) + (long long)(y[i]-y[n])*(y[i]-y[n]) < (long long)(r[i] + r[n]) * (r[i] + r[n])){
        ok = false;
        break;
      }
    }
    if(ok) break;
  }
}

bool cmp(int a, int b){ return r[a] > r[b]; }

int main(int argc, char *argv[]){
  srand(time(NULL));
  int T;
  scanf("%d",&T);
  REP(t,T){
    fprintf(stderr,"t:%d\n",t);
    printf("Case #%d:",t+1);
    scanf("%d%d%d",&N,&W,&L);
    REP(i,N) scanf("%d",r+i);
    REP(i,N) o[i] = i;
    sort(o, o + N, cmp);
    REP(i,N) place(i);
    REP(i,N) printf(" %d %d", x[i], y[i]);
    printf("\n");
  }
  return 0;
}
