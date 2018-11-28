#include<cstdio>

using namespace std;

#define FOR(i,N) for(int i = 0; i < (N); ++i)

int main() {

  long long int N, K, T;

  long long int L[31];

  FOR(i,30) L[i+1] = 1<<(i+1);
 
  scanf("%lld", &T);

  FOR(i,T) {
    scanf("%lld %lld", &N, &K);

    ++K;

    printf("Case #%d: ", i+1);

    if((K%L[N])==0 && K != 1) printf("ON\n"); else printf("OFF\n");

  }
  
  return(0);
      
}
