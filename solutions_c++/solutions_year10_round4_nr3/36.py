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
int T;
int N;
int mat[105][105];
#define get(a, b) ((a) < 0 || (b) < 0 ? 0 : mat[a][b])
int main() {
   int i, j;
   int Case = 1;
   scanf("%d", &T);
   while (T --) {
      scanf("%d", &N);
      memset(mat, 0, sizeof(mat));
      while (N --) {
	 int X1, Y1, X2, Y2;
	 scanf("%d%d%d%d", &X1, &Y1, &X2, &Y2);
	 for (i = X1 - 1; i < X2; i ++)
	    for (j = Y1 - 1; j < Y2; j ++)
	       mat[i][j] = 1;
      }
      int ret = 0;
      while (1) {
	 ret ++;
	 int tmp[105][105];
	 int sum = 0;
	 for (i = 0; i < 100; i ++)
	    for (j = 0; j < 100; j ++) {
	       if (get(i, j) + get(i - 1, j) + get(i, j - 1) >= 2)
		  tmp[i][j] = 1;
	       else
		  tmp[i][j] = 0;
	       sum += tmp[i][j];
	    }
	 memcpy(mat, tmp, sizeof(tmp));
	 if (sum == 0)
	    break;
      }
      printf("Case #%d: %d\n", Case ++, ret);
   }
   return 0;
}

