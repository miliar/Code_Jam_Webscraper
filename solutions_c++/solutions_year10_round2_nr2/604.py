#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <string.h>
#include <map>
#include <set>


using namespace std;
#define MAX 10000

long long swaps;
long long cando[MAX],pos[MAX],v[MAX];
long long swap(long long a, long long b) {
  long long o = cando[a];
  long long c = cando[b];
  cando[a] = c;
  cando[b] = o;
}
long long solve (long long cur, long long R) {
  if (R == 0)
    return true;
  if (cur < 0)
    return false;
  if (cando[cur] == 1)
    return solve(cur-1,R-1);
  else {
    long long i,j, swapping = cur-1;
    for ( i = swapping ; i >= 0 ; i--) {
      // prlong longf("Cando[%d] = %d\n",i,cando[i]);
      if (cando[i] == 1)
	break;
     
    }
    swapping = i;
    if (i < 0)
      return false;
    //prlong longf("%d %d\n",swapping,cur);
    for (j = swapping ; j < cur ; j++)
      swap(j,j+1);
    //  prlong longf("Estava em cur(%d) achei um possivel em %d\n",cur,swapping);
    swaps += (cur-swapping);
    return solve(cur-1,R-1);
  }
}

int main() {
  long long N,M,K,T,B,i,cases=0;
  scanf("%lld",&N);
  while (N--) {
    scanf("%lld %lld %lld %lld",&M,&K,&B,&T);
    for (i = 0 ; i < M ; i++)
      scanf("%lld",&pos[i]);
    for (i = 0 ; i < M ; i++)
      scanf("%lld",&v[i]);
    for (i = 0 ; i < M ; i++) {
      if (pos[i] + v[i]*T >= B)
	cando[i] = 1;
      else 
	cando[i] = 0;
      //  prlong longf("Cando[%d] = %d\n",i,cando[i]);
    }
    swaps = 0;
    printf("Case #%lld: ",++cases);
    if (solve(M-1,K))
      printf("%lld\n",swaps);
    else
      printf("IMPOSSIBLE\n");
    
  }
  return 0;
}
