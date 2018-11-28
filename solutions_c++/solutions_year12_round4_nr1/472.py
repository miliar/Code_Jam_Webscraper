#include <cstdio>
#include <cstring>

#include <algorithm>

using namespace std;

#define MAXN 10004

typedef long long llong;

int N;
llong D[MAXN], L[MAXN];
llong dist;

llong DP[MAXN];

bool solve() {
   memset(DP, -1, sizeof(DP[0])*(N+1));
   DP[0] = D[0];
   for (int i = 0; i < N; ++i) {
      if (DP[i] < 0) continue;
      if (D[i] + DP[i] >= dist)
         return true;
      for (int j = i+1; j < N; ++j) {
         llong d = D[j] - D[i];
         if (d > DP[i]) break;
         llong m = min(d, L[j]);
         if (DP[j] < m)
            DP[j] = m;
      }
   }
   return false;
}

int main(int argc, char* argv[]) {
   int TC;
   scanf("%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      scanf("%d", &N);
      for (int i = 0; i < N; ++i)
         scanf("%lld %lld", D+i, L+i);
      scanf("%lld", &dist);
      bool res = solve();
      printf("Case #%d: %s\n", tc, res ? "YES" : "NO");
   }
   return 0;
}
