#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

//二分图最大匹配,hungary 算法,邻接表形式,邻接阵接口,复杂度 O(m*e)s
//返回最大匹配数,传入二分图大小 m,n 和邻接阵
//match1,match2 返回一个最大匹配,未匹配顶点 match 值为-1
const int MAXN = 310;
#define _clr(x) memset(x, 0xff, sizeof(int) * MAXN)

int match1[MAXN], match2[MAXN];

int hungary(int m, int n, const bool mat[][MAXN]) {
    int s[MAXN + 1], t[MAXN], p, q, ret = 0, i, j, k, r;
    vector <int> e[MAXN];
    //生成邻接表(只需一边)
    for (i = 0; i < m; ++i) {
        for (j = 0; j < n; ++j) {
            if (mat[i][j]) {
              e[i].push_back(j);
          }
      }
  }
  _clr(match1);
  _clr(match2);
  for ( i = 0; i < m; ret += (match1[i++] >= 0)) {
      _clr(t);
      for (s[p = q = 0] = i; p <= q && match1[i] < 0; p++) {
          for (r = 0, k = s[p]; r < (int)e[k].size() && match1[i] < 0; ++r) {
              if (t[j = e[k][r]] < 0) {
                  s[++q] = match2[j];
                  t[j] = k;
                  if (s[q] < 0) {
                      for (p = j; p >= 0; j = p) {
                          match2[j] = k = t[j];
                          p = match1[k];
                          match1[k] = j;
                      }
                  }
              }
          }
      }
  }
  return ret;
}

inline int sign(int x) {
	if (x == 0) return 0;
	if (x > 0) return 1;
	return -1;
}

bool mat[MAXN][MAXN];
int p[MAXN][MAXN];

void solve() {

	int n, K;
	scanf("%d %d", &n, &K);
	for (int i = 0; i < n; i++) 
		for (int j = 0; j < K; j++)
			scanf("%d", &p[i][j]);
	memset(mat, false, sizeof(mat));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			bool yes = false;
			for (int k = 0; k < K - 1; k++)
				if (sign(p[i][k] - p[j][k]) * sign(p[i][k + 1] - p[j][k + 1]) <= 0) {
					yes = true;
					break;
				}
			if (!yes && p[i][0] > p[j][0]) mat[i][j] = true;
		}
	for (int i = 0; i < n; i++) mat[i][i] = false;
		
/*	printf("\n");
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			printf("%d ", mat[i][j]);
		printf("\n");	
	}
*/			
	
	printf("%d\n", n - hungary(n, n, mat));
}

int main() {
	int test;
	scanf("%d", &test);
	for (int i = 1; i <= test; i++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}

