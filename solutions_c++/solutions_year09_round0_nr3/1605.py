#include <cstdio>
#include <cstring>
int N, ans;
const char *goal = "welcome to code jam";
char line[501];
int mtx[501][20];
void BT(int m, int n){
	if(!n){
		++ans;
		return;
	}
	if(!m) return;
	if(line[m-1] == goal[n-1]) BT(m-1, n-1);
	if(mtx[m-1][n] <= mtx[m][n]) BT(m-1, n);
}
void LCS(void){
	memset(mtx, 0, sizeof(mtx));
	int n = 19, m = strlen(line);
	for(int i = 1; i <= m; ++i){
		for(int j = 1; j <= n; ++j){
			if(line[i-1] == goal[j-1]){
				mtx[i][j] = mtx[i-1][j-1]+1;
			}
			else mtx[i][j] = mtx[i-1][j];
		}
	}
	ans = 0;
	if(mtx[m][n] < 19) return;
	/*
	for(int i = 0; i <= m; ++i){
		for(int j = 0; j <= n; ++j){
			printf(" %2d", mtx[i][j]);
		}
		putchar('\n');
	}*/
	BT(m, n);
}
int main(void){
	scanf("%d ", &N);
	for(int i = 1; i <= N; ++i){
		gets(line);
		LCS();
		printf("Case #%d: %04d\n", i, ans);
	}
}
