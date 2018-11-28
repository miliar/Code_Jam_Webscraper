#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 50+5;

int n, k;
char g[MAXN][MAXN];

char* result[] = {"Neither", "Red", "Blue", "Both"};
int dx[] = {0, 1, 1, 1};
int dy[] = {1, 1, 0, -1};

bool go(int x, int y, char what, int dir, int count = 0) {
	if(count == k) return true;
	if(g[x][y] != what) return false;
	return go(x+dx[dir], y+dy[dir], what, dir, count+1);
}


char* solve() {
	scanf("%d %d", &n, &k);
	for(int i = 0; i <= n+1; i++) g[0][i] = g[n+1][i] = 0;
	for(int i = 1; i <= n; i++) {
		g[i][0] = 0;
		scanf("%s", &g[i][1]);
		g[i][n+1] = 0;
	}

	for(int i = 1; i <= n; i++) {
		int first = n;
		for(int j = n; j >= 1; j--) {
			if(g[i][j] == '.') continue;
			swap(g[i][j], g[i][first]);
			first--;
		}
	}


	/*
	for(int i = 0; i <= n+1; i++) {
		for(int j = 0; j <= n+1; j++) {
			printf("%c", g[i][j]);
		}
		printf("\n");
	}
*/
	bool isR = false;
	bool isB = false;


	for(int i = 1; i <= n; i++) {
		for(int j = 1; j <= n; j++) {
			for(int k = 0; k <= 3; k++) {
				isR |= go(i, j, 'R', k);		
				isB |= go(i, j, 'B', k);
			}
		}
	}


	return result[isR + 2*isB];




}


int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) printf("Case #%d: %s\n", i, solve()); 

}