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

#define MAXN 2222
int N, x[MAXN], h[MAXN];

bool go(int left, int right, int depth){
//  printf("left:%d right:%d depth:%d\n",left,right,depth);
  if(left == right) return true;
  if(x[right - 1] != right) return false;
  int last = right - 1;
  h[last] = h[right] - depth - 1;
  for(int i = right - 2; i >= left; i--){
    if(x[i] == right){
      if(!go(i+1, last, depth+1)) return false;
      last = i;
      h[last] = h[right] - 1 - (right - i) * depth;
    }
    else if(x[i] > last || x[i] <= i) return false;
  }
  if(!go(left, last, depth+1)) return false;
  return true;
}

bool solve(){
  REP(i,N) h[i] = -1;
  h[N-1] = 1000000000;
  return go(0, N-1, 0);
}

bool check(){
  REP(i,N-1){
    int best = i+1;
    FOR(j,i+1,N-1) if((long long)(h[j] - h[i]) * (best - i) > (long long)(h[best] - h[i]) * (j - i)) best = j;
    if(best != x[i]) return false;
  }
  return true;
}

int main(int argc, char *argv[]){
  int T; 
  scanf("%d",&T);
  REP(t,T){
    printf("Case #%d:",t+1);
    scanf("%d",&N);
    REP(i,N-1){ scanf("%d",x+i); x[i]--; }
    if(solve()){
      if(!check()) printf("BUUGGGGGGGGGGGGGG\n");
      REP(i,N) printf(" %d",h[i]);
    }
    else printf(" Impossible");
    printf("\n");
  }
  return 0;
}
