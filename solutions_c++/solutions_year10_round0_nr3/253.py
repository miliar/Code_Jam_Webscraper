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
long long T, N, K, R;
long long num[1005];
long long next[1005];
long long val[1005];
long long mark[1005];
long long mark2[1005];
int main() {
   long long i, j, Case = 1, k, l;
   scanf("%lld", &T);
   while (T --) {
      scanf("%lld%lld%lld", &R, &K, &N);
      for (i = 0; i < N; i ++)
	 scanf("%lld", &num[i]);
      for (i = 0; i < N; i ++) {
	 if (num[i] > K) {
	    next[i] = i;
	    val[i] = 0;
	    continue;
	 }
	 k = num[i];
	 for (j = (i + 1) % N; j != i && k + num[j] <= K; j = (j + 1) % N)
	    k += num[j];
	 next[i] = j;
	 val[i] = k;
      }
      memset(mark, -1, sizeof(mark));
      k = 0;
      long long ans = 0;
      for (i = 0; i < R; i ++) {
	 if (mark[k] != -1 && R - i >= N + 5) {
	    j = i - mark[k];
	    l = ans - mark2[k];
	    long long delta = (R - i) / j;
	    i += delta * j;
	    ans += delta * l;
	    i --;
	    continue;
	 }
	 mark[k] = i;
	 mark2[k] = ans;
	 ans += val[k];
	 k = next[k];
      }
      printf("Case #%lld: %lld\n", Case ++, ans);
   }
   return 0;
}

