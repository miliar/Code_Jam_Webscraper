#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>

#define REP(i, to) for(int i=0; i<to; i++)

using namespace std;
typedef unsigned int uInt;
typedef long long int llInt;

llInt F[10047];

int main()
{
  int T;
  scanf("%d", &T);
  REP(t, T){
    int N;
    llInt L, H;
    scanf("%d%lld%lld", &N, &L, &H);
    REP(i, N) scanf("%lld", &F[i]);
    
    llInt result = -1;
    for(llInt a=L; a<=H; a++){
      bool ok=true;
      REP(i, N) if(a % F[i] != 0 && F[i] % a != 0) ok=false;
      
      if(ok) {
        result = a;
        break;
      }
    }
    
    printf("Case #%d: ", t+1);
    if(result > 0) printf("%lld\n", result);
    else printf("NO\n");
  }
  return 0;
}
