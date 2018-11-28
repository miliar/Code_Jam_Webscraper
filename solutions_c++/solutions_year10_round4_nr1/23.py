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
int T, N;
int len[1005][1005];
int input[1005][1005];
int cnt[1005][1005];
#define same(a, b) ((a) == (b) || (a) == -1 || (b) == -1)
int check(int s) {
   int x, y;
   int i, j;
   for (x = 0; x < 2 * s - 1; x ++)
      for (y = s - len[s][x]; y <= s + len[s][x] - 2; y += 2)
	 if (x + 2 * N - 2 < 2 * s - 1 && y >= s - len[s][x + 2 * N - 2] && y <= s + len[s][x + 2 * N - 2] - 2) {
	    for (i = 0; i < 2 * s - 1; i ++)
	       for (j = s - len[s][i]; j <= s + len[s][i] - 2; j += 2)
		  cnt[i][j] = -1;
	    for (i = 0; i < 2 * N - 1; i ++)
	       for (j = N - len[N][i]; j <= N + len[N][i] - 2; j += 2)
		  cnt[x + i][y + j - (N - 1)] = input[i][j];
	    int ok = 1;
	    for (i = 0; i < 2 * s - 1 && ok; i ++)
	       for (j = s - len[s][i]; j <= s + len[s][i] - 2 && ok; j += 2)
		  if (!same(cnt[i][j], cnt[2 * s - 2 - i][j]) || !same(cnt[i][j], cnt[i][2 * s - 2 - j]))
		     ok = 0;
	    if (ok)
	       return 1;
	 }
   return 0;
}
int main() {
   int i, j;
   int Case = 1;
   for (i = 1; i < 500; i ++) {
      for (j = 0; j < i; j ++)
	 len[i][j] = j + 1;
      for (; j < 2 * i - 1; j ++)
	 len[i][j] = len[i][j - 1] - 1;
   }
   scanf("%d", &T);
   while (T --) {
      scanf("%d", &N);
      memset(input, -1, sizeof(input));
      for (i = 0; i < 2 * N - 1; i ++)
	 for (j = 0; j < len[N][i]; j ++)
	    scanf("%d", &input[i][N - len[N][i] + 2 * j]);
      int k;
      for (k = N; !check(k); k ++);
      printf("Case #%d: %d\n", Case ++, k * k - N * N);
   }
   return 0;
}

