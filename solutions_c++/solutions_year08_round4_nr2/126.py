#include <iostream>
#include <cstdlib>

using namespace std;

void solve(int caseno){
  int N,M,A;
  cin >> N >> M >> A;
  if(N*M < A){
    printf("Case #%d: IMPOSSIBLE\n", caseno);
    return;
  }

  int a = N;
  int d = M;
  
  int lo = 0;
  while(lo + 1 < a){
    int m = (lo + a)/2;
    if(m*d < A){
      lo = m;
    }
    else
      a = m;
  }
  // binary searches to find lowest possible a

  lo = 0;
  while(lo + 1 < d){
    int m = (lo + d)/2;
    if(a*m < A){
      lo = m;
    }
    else
      d = m;
  }

  // now a*d < A + N, set c = N, b =1
  int b = 1, c=a*d-A;
  
  printf("Case #%d: 0 0 %d %d %d %d\n", caseno, a,b,c,d);
}

int main(){
  int n;
  cin >> n;
  for (int i=0; i<n; ++i){
    solve(i+1);
  }
  return 0;
}
