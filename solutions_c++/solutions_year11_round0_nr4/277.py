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
int T, N;
int main() {
   int i, j, Case = 1;
   int all[1005];
   scanf("%d", &T);
   while (T --) {
      scanf("%d", &N);
      int cnt = 0;
      for (i = 0; i < N; i ++) {
	 scanf("%d", &all[i]);
	 if (i + 1 != all[i])
	    cnt ++;
      }
      printf("Case #%d: %.6lf\n", Case ++, (double)cnt);
   }
   return 0;
}

