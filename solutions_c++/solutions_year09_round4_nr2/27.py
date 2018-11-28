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
#define oo 1000000000
int N, M;
int F, T;
char mat[55][55];
int drop[55][55];
int getInt[55][55][55][2];
int dist[55][55][55];
int main() {
   int i, j, k, Case = 1, l, m;
   scanf("%d", &T);
   while (T --) {
      scanf("%d%d%d", &N, &M, &F);
      for (i = 0; i < N; i ++)
	 scanf("%s", mat[i]);
      for (i = 0; i < N; i ++)
	 for (j = 0; j < M; j ++) {
	    for (k = i + 2; k < N; k ++)
	       if (mat[k][j] == '#')
		  break;
	    if (k - i - 1 > F)
	       drop[i][j] = -1;
	    else
	       drop[i][j] = k - 1;
	 }
      memset(getInt, 0, sizeof(getInt));
      for (i = 0; i < N - 1; i ++)
	 for (j = 0; j < M; j ++)
	    for (k = 0; k < M; k ++) {
	       for (l = k + 1; l < M; l ++)
		  if (l > j && mat[i][l] == '#' || mat[i + 1][l] == '.')
		     break;
	       if (l < M && !(l > j && mat[i][l] == '#'))
		  getInt[i][j][k][1] = l;
	       else
		  getInt[i][j][k][1] = l - 1;
	       for (l = k - 1; l >= 0; l --)
		  if (l < j && mat[i][l] == '#' || mat[i + 1][l] == '.')
		     break;
	       if (l >= 0 && !(l < j && mat[i][l] == '#'))
		  getInt[i][j][k][0] = l;
	       else
		  getInt[i][j][k][0] = l + 1;
	    }
      for (i = 0; i < N; i ++)
	 for (j = 0; j < M; j ++)
	    for (k = 0; k < M; k ++)
	       dist[i][j][k] = oo;
      for (i = N - 1; i >= 0; i --)
	 for (j = 0; j < M; j ++)
	    for (k = j; k < M; k ++)
	       if (i == N - 1)
		  dist[i][j][k] = 0;
	       else {
		  for (l = j + 1; l <= k - 1; l ++)
		     if (mat[i + 1][l] == '.')
			break;
		  if (l <= k - 1)
		     continue;
		  for (l = j; l < k; l ++)
		     for (m = l; m < k; m ++) {
			if (m == k - 1 && mat[i + 1][k] == '.' || drop[i][m] == -1)
			   continue;
			int ni, nj;
			if (drop[i][m] > i + 1) {
			   ni = getInt[drop[i][m]][m][m][0];
			   nj = getInt[drop[i][m]][m][m][1];
			}
			else {
			   ni = getInt[i + 1][l][m][0];
			   nj = getInt[i + 1][l][m][1];
			}
			dist[i][j][k] = min(dist[i][j][k], dist[drop[i][m]][ni][nj] + (l == j && mat[i + 1][j] == '.' ? m - l : m - l + 1));
		     }
		  for (l = k; l > j; l --)
		     for (m = l; m > j; m --) {
			if (m == j + 1 && mat[i + 1][j] == '.' || drop[i][m] == -1)
			   continue;
			int ni, nj;
			if (drop[i][m] > i + 1) {
			   ni = getInt[drop[i][m]][m][m][0];
			   nj = getInt[drop[i][m]][m][m][1];
			}
			else {
			   ni = getInt[i + 1][l][m][0];
			   nj = getInt[i + 1][l][m][1];
			}
			dist[i][j][k] = min(dist[i][j][k], dist[drop[i][m]][ni][nj] + (l == k && mat[i + 1][k] == '.' ? l - m : l - m + 1));
		     }
	       }
      i = getInt[0][0][0][0];
      j = getInt[0][0][0][1];
      k = dist[0][i][j];
      if (k == oo)
	 printf("Case #%d: No\n", Case ++);
      else
	 printf("Case #%d: Yes %d\n", Case ++, k);
   }
   return 0;
}

