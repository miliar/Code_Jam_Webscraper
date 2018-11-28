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
int cntTime[2];
int cntpos[2];
int main() {
   int i, j, Case = 1;
   scanf("%d", &T);
   for (Case = 1; Case <= T; Case ++) {
      scanf("%d", &N);
      cntTime[0] = cntTime[1] = 0;
      cntpos[0] = cntpos[1] = 1;
      for (i = 0; i < N; i ++) {
	 char tmp[3];
	 int tmp2, id;
	 scanf("%s%d", tmp, &tmp2);
	 id = (tmp[0] == 'O' ? 0 : 1);
	 cntTime[id] += abs(tmp2 - cntpos[id]);
	 cntpos[id] = tmp2;
	 cntTime[id] = max(cntTime[0], cntTime[1]);
	 cntTime[id] ++;
      }
      printf("Case #%d: %d\n", Case, max(cntTime[0], cntTime[1]));
   }
   return 0;
}

