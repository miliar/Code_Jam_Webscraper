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
int N, C, D;
char comb[300][300];
char op[300][300];
int main() {
   int i, j, Case = 1;
   scanf("%d", &T);
   while (T --) {
      memset(comb, 0, sizeof(comb));
      memset(op, 0, sizeof(op));
      char tmp[205];
      scanf("%d", &C);
      while (C --) {
	 scanf("%s", tmp);
	 comb[tmp[0]][tmp[1]] = comb[tmp[1]][tmp[0]] = tmp[2];
      }
      scanf("%d", &D);
      while (D --) {
	 scanf("%s", tmp);
	 op[tmp[0]][tmp[1]] = op[tmp[1]][tmp[0]] = 1;
      }
      scanf("%d", &N);
      scanf("%s", tmp);
      char cnt[105];
      int M = 0;
      for (i = 0; i < N; i ++) {
	 cnt[M ++] = tmp[i];
	 if (M >= 2 && comb[cnt[M - 1]][cnt[M - 2]]) {
	    cnt[M - 2] = comb[cnt[M - 1]][cnt[M - 2]];
	    M --;
	 }
	 else
	    for (j = 0; j < M - 1; j ++)
	       if (op[cnt[j]][cnt[M - 1]])
		  M = 0;
      }
      printf("Case #%d: [", Case ++);
      for (i = 0; i < M; i ++) {
	 putchar(cnt[i]);
	 if (i < M - 1)
	    printf(", ");
      }
      printf("]\n");
   }
   return 0;
}

