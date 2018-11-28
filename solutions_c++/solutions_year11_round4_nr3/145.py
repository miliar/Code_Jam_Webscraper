#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

typedef long long ll;

bool notprime[1000001];

int main() {
  notprime[0] = 1;
  notprime[1] = 1;
  for(int i = 2; i <= 1000000; i++) if(!notprime[i])
    for(int j = i+i; j <= 1000000; j += i)
      notprime[j] = 1;

  int T;
  scanf("%d", &T);
  for(int tid = 1; tid <= T; tid++) {
    ll N;
    scanf("%lld", &N);
    ll max = 1, min = 0;
    for(int i = 2; i < 1000000 && i <= N; i++) {
      if(!notprime[i]) {
        min++;
        int alpha = 0;
        long long pp = i;
        while(pp <= N) alpha++, pp *= i;
//        fprintf(stderr, "prime %d has alpha %d\n", i, alpha);
        max += alpha;
      }
    }
//    fprintf(stderr, "max=%lld min=%lld\n", max, min);
    if(N == 1) max = min = 0;
    printf("Case #%d: %lld\n", tid, max - min);
  }
  return 0;
}

