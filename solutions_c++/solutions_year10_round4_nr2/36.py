#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
#define PI 3.14159265358979323846264338327950288
#define oo 1000000000000LL
long long ans[15][1050][1050];
int mark[15][1050][1050];
int M[1050];
int price[1050][1050];
int T, N;
int tot0;
inline long long min(long long a, long long b) {
   return (a < b ? a : b);
}
long long solve(int tot, int l, int r) { 
   int m = (l + r) / 2;
   if (l == r) {
      if (tot < M[l])
	 return oo;
      return 0;
   }
   if (mark[tot][l][r] == tot0)
      return ans[tot][l][r];
   mark[tot][l][r] = tot0;
   ans[tot][l][r] = min(price[l][r] + solve(tot + 1, l, m) + solve(tot + 1, m + 1, r), solve(tot, l, m) + solve(tot, m + 1, r));
   return ans[tot][l][r];
}
int main() {
   int i, j;
   int Case = 1;
   memset(mark, -1, sizeof(mark));
   scanf("%d", &T);
   while (T --) {
      scanf("%d", &N);
      for (i = 0; i < (1 << N); i ++) {
	 scanf("%d", &M[i]);
	 M[i] = N - M[i];
      }
      for (i = 0; i < N; i ++)
	 for (j = 0; j < (1 << N - i - 1); j ++)
	    scanf("%d", &price[j << (i + 1)][((j + 1) << (i + 1)) - 1]);
      tot0 ++;
      printf("Case #%d: %lld\n", Case ++, solve(0, 0, (1 << N) - 1));
   }
   return 0;
}

