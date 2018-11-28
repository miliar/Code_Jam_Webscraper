#include <iostream>

using namespace std;

#define MAXN 55

int nTests, test;
int i, j, k;
int N,K,B,T,S,ans;
int X[MAXN], V[MAXN];
bool arrives[MAXN];
bool canArrive[MAXN];
int cnt,nSwaps;

int main() {
  scanf("%d", &nTests);
  for (test = 1; test <= nTests; ++test) {
    scanf("%d %d %d %d", &N, &K, &B, &T);
    for (i = 0; i < N; ++i) {
      scanf("%d", &X[i]);
    }
    for (i = 0; i < N; ++i) {
      scanf("%d", &V[i]);
      canArrive[i] = (B-X[i] <= V[i] * T);
    }
    for (i = N-1; i >= 0; --i) {
      if (canArrive[i] && K) {
        arrives[i] = true;
        --K;
      } else {
        arrives[i]= false;
      }
    }
    ans = - 1;
    cnt = 0;
    if (!K) {
      ans = 0;
      for (i = 0; i < N; ++i) {
        if (!arrives[i]) {
          ans += cnt;
        } else {
          ++cnt;
        }
      }
    }
    printf("Case #%d: ",test);
    if (ans == -1) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n",ans);
    }
  }
  return 0;
}
