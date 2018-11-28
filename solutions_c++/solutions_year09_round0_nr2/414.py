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
int N, M;
int height[105][105];
int next[105][105];
int color[105][105];
char out[105][105];
int ch[105];
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
int s;
#define OK(a, b) ((a) >= 0 && (b) >= 0 && (a) < N && (b) < M)
int solve(int x, int y) {
   if (color[x][y] != -1)
      return color[x][y];
   if (next[x][y] == -1)
      return (color[x][y] = s ++);
   return (color[x][y] = solve(x + dx[next[x][y]], y + dy[next[x][y]]));
}
int main() {
   int i, j, k, Case = 1;
   scanf("%d", &T);
   while (T --) {
      scanf("%d%d", &N, &M);
      for (i = 0; i < N; i ++)
	 for (j = 0; j < M; j ++)
	    scanf("%d", &height[i][j]);
      for (i = 0; i < N; i ++)
	 for (j = 0; j < M; j ++) {
	    int mini, minin = height[i][j] + 5;
	    for (k = 0; k < 4; k ++)
	       if (OK(i + dx[k], j + dy[k]) && height[i + dx[k]][j + dy[k]] < minin) {
		  minin = height[i + dx[k]][j + dy[k]];
		  mini = k;
	       }
	    if (minin < height[i][j])
	       next[i][j] = mini;
	    else
	       next[i][j] = -1;
	 }
      memset(color, -1, sizeof(color));
      s = 0;
      for (i = 0; i < N; i ++)
	 for (j = 0; j < M; j ++)
	    solve(i, j);
      s = 'a';
      memset(ch, -1, sizeof(ch));
      for (i = 0; i < N; i ++)
	 for (j = 0; j < M; j ++)
	    if (ch[color[i][j]] == -1)
	       ch[color[i][j]] = s ++;
      printf("Case #%d:\n", Case ++);
      for (i = 0; i < N; i ++)
	 for (j = 0; j < M; j ++) {
	    printf("%c", ch[color[i][j]]);
	    if (j + 1 == M)
	       printf("\n");
	    else
	       printf(" ");
	 }
   }
   return 0;
}

