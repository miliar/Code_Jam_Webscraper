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
int maxir[45];
int T, N;
char mat[45][45];
int main() {
   int i, j, Case = 1, k;
   scanf("%d", &T);
   while (T --) {
      scanf("%d", &N);
      for (i = 0; i < N; i ++)
	 scanf("%s", mat[i]);
      memset(maxir, 0, sizeof(maxir));
      for (i = 0; i < N; i ++)
	 for (j = 0; j < N; j ++)
	    if (mat[i][j] == '1')
	       maxir[i] = j;
      int ret = 0;
      for (i = 0; i < N; i ++) {
	 for (j = i; j < N; j ++)
	    if (maxir[j] <= i)
	       break;
	 for (k = j; k > i; k --) {
	    maxir[k] = maxir[k - 1];
	    ret ++;
	 }
      }
      printf("Case #%d: %d\n", Case ++, ret);
   }
   return 0;
}

