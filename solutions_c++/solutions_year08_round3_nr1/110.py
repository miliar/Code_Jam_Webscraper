#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>

#define f(x,y) for(int x=0; x<(y); ++x)
using namespace std;

int comp(int a, int b){
  return (a>b);
}


int N, P, K, L, A[1003];
int main(){
  scanf("%d", &N);
  f(t, N){
    scanf("%d%d%d", &P, &K, &L);
    f(i, L)
      scanf("%d", &A[i]);
    sort(A, A+L, comp);
    long long int ans=0;
    for(int i=0; i<L; ++i){
      ans+=A[i]*(i/K+1);
    }
    printf("Case #%d: %lld\n", t+1, ans);
  }
  return 0;
}
