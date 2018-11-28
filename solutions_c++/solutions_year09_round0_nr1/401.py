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
using namespace std;
#define PI 3.14159265358979323846264338327950288
int L, D, N;
char all[5005][20];
char cnt[1000];
set <char> pat[20];
int main() {
   int i, j, Case = 1, k;
   scanf("%d%d%d", &L, &D, &N);
   for (i = 0; i < D; i ++)
      scanf("%s", all[i]);
   while (N --) {
      scanf("%s", cnt);
      int len = strlen(cnt);
      j = 0;
      k = 0;
      pat[0].clear();
      for (i = 0; i < len; i ++)
	 if (cnt[i] == ')') {
	    j ++;
	    pat[j].clear();
	    k = 0;
	 }
	 else
	    if (cnt[i] == '(')
	       k = 1;
	    else {
	       pat[j].insert(cnt[i]);
	       if (!k) {
		  j ++;
		  pat[j].clear();
	       }
	    }
      assert(j == L);
      k = 0;
      for (i = 0; i < D; i ++) {
	 for (j = 0; j < L; j ++)
	    if (pat[j].find(all[i][j]) == pat[j].end())
	       break;
	 if (j >= L)
	    k ++;
      }
      printf("Case #%d: %d\n", Case ++, k);
   }
   return 0;
}

