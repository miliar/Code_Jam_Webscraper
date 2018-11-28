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
#include <cassert>
#include <complex>
using namespace std;
#define PI 3.14159265358979323846264338327950288
int T;
int main() {
   int N;
   int i, j, Case = 1;
   scanf("%d", &T);
   int all[1005];
   while (T --) {
      scanf("%d", &N);
      int tmp = 0, sum = 0, m = 1000000000;
      for (i = 0; i < N; i ++) {
	 scanf("%d", &all[i]);
	 tmp ^= all[i];
	 sum += all[i];
	 m = min(m, all[i]);
      }
      if (tmp != 0)
	 printf("Case #%d: NO\n", Case ++);
      else {
	 printf("Case #%d: %d\n", Case ++, sum - m);
      }
   }
   return 0;
}


