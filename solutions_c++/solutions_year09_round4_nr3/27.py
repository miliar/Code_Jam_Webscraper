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
int N, K;
int data[105][25];
int mat[105][105];
int mark[105];
int o2[105];
int dfs(int x) {
   int i;
   mark[x] = 1;
   for (i = 0; i < N; i ++)
      if (mat[x][i] && (o2[i] == -1 || !mark[o2[i]] && dfs(o2[i]))) {
	 o2[i] = x;
	 return 1;
      }
   return 0;
}
int main() {
   int i, j, Case = 1, k;
   scanf("%d", &T);
   while (T --) {
      scanf("%d%d", &N, &K);
      for (i = 0; i < N; i ++)
	 for (j = 0; j < K; j ++)
	    scanf("%d", &data[i][j]);
      for (i = 0; i < N; i ++)
	 for (j = 0; j < N; j ++) {
	    for (k = 0; k < K; k ++)
	       if (data[i][k] <= data[j][k])
		  break;
	    if (k >= K)
	       mat[i][j] = 1;
	    else
	       mat[i][j] = 0;
	 }
      int ret = N;
      memset(o2, -1, sizeof(o2));
      for (i = 0; i < N; i ++) {
	 memset(mark, 0, sizeof(mark));
	 if (dfs(i))
	    ret --;
      }
      printf("Case #%d: %d\n", Case ++, ret);
   }
   return 0;
}

