#include <iostream>

using namespace std;

#define huge long long
#define MAXN 1123

int nTests,test;
int R,k,N,i;
huge groupSize[MAXN];
int groupsTaken[MAXN];
huge peopleTaken[MAXN];
huge sum,ans;
int first;

int main() {
  scanf("%d",&nTests);
  for (test = 1; test <= nTests; ++test) {
    scanf("%d %d %d",&R,&k,&N);
    for (i = 0; i < N; ++i) {
      scanf("%lld",&groupSize[i]);
    }
    for (i = 0; i < N; ++i) {
      groupsTaken[i] = 0;
      peopleTaken[i] = 0;
      while (groupsTaken[i] < N && peopleTaken[i] + groupSize[(i + groupsTaken[i]) % N] <= k)
        peopleTaken[i] += groupSize[(i + groupsTaken[i]++) % N];
    }
    ans = 0;
    first = 0;
    for (i = 1; i <= R; ++i) {
      ans += peopleTaken[first];
      first = (first + groupsTaken[first]) % N;
    }
    printf("Case #%d: %lld\n",test,ans);
  }
  return 0;
}
