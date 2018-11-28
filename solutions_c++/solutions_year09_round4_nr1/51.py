#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

//二分图最佳匹配,kuhn munkras 算法,邻接阵形式,复杂度 O(m*m*n)
//返回最佳匹配值,传入二分图大小 m,n 和邻接阵 mat,表示权值
//match1,match2 返回一个最佳匹配,未匹配顶点 match 值为-1
//一定注意 m<=n,否则循环无法终止
//最小权匹配可将权值取相反数

const int MAXN = 310;

char map[MAXN][MAXN];
int last[MAXN];

void solve() {

	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%s", map[i]);

	for (int i = 0; i < n; i++) {
		last[i] = n - 1;
		while (last[i] && map[i][last[i]] == '0') last[i]--; 
	}

	int ret = 0;
	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < n; j++) printf("%d ", last[j]);
//		printf("\n");
		for (int j = i; j < n; j++)
			if (last[j] <= i) {
				for (int k = j; k > i; k--) {
					ret++;
					swap(last[k], last[k - 1]);
				}
				break;
			}
	}
	printf("%d\n", ret);


/*	for (int i = 0; i < n; i++) 
		for (int j = 0; j < n; j++)
			mat[i][j] = -INF;
	for (int i = 0; i < n; i++) {
		int last = n - 1;
		while (last && map[i][last] == '0') last--; 
		for (int j = last; j < n; j++) mat[i][j] = -ABS(j - i);
	}
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			printf("%d ", mat[i][j]);
		printf("\n");
	}
	
	printf("%d\n", (-kuhnMunkras(n, n, mat)) / 2);*/
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

