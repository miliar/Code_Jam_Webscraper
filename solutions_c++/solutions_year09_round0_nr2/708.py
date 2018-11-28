#include <cstdio>
#include <algorithm>

#define MAX_ALT 999999
#define MAX_DIM 300

int H, W, nBasins;
int map[MAX_DIM][MAX_DIM];
int ans[MAX_DIM][MAX_DIM];

using namespace std;

int d[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int dfs(int r, int c) {
	if (ans[r][c] != -1) {return ans[r][c];}
	int bestv = map[r][c], bestr, bestc;
	for (int dir = 0; dir < 4; dir++) {
		if (map[r+d[dir][0]][c+d[dir][1]] < bestv) {
			bestv = map[r+d[dir][0]][c+d[dir][1]];
			bestr = r+d[dir][0];
			bestc = c+d[dir][1];
		}
	}
	if (bestv == map[r][c]) {
		ans[r][c] = nBasins++;
	} else {
		ans[r][c] = dfs(bestr,bestc);
	}
	return ans[r][c];
}

int main() {
	int nCases;
	scanf("%d ",&nCases);
	for (int caseid = 1; caseid <= nCases; caseid++) {
		scanf("%d%d",&H,&W);
		for (int i = 0; i <= H+1; i++) {
			for (int j = 0; j <= W+1; j++) {
				map[i][j] = MAX_ALT;
				ans[i][j] = -1;
			}
		}
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				scanf("%d",&map[i+1][j+1]);
			}
		}
		nBasins = 0;
		printf("Case #%d:\n",caseid);
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				printf("%c%s",dfs(i+1,j+1)+'a',j==W-1?"\n":" ");
			}
		}
	}
}