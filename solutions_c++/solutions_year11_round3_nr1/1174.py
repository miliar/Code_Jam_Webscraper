#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
 
#define PB        push_back
#define ALL(v)      (v).begin() , (v).end()
#define SZ(v)      ( (int) v.size() )
#define FOR(i, a, b)  for (int i = (a); i < b ; i++)

using namespace std;

int r, c, C, n_blue, T;
char grid[100][100];
bool vis[100][100], SOLVED;

bool place(int x, int y) {
	if (!(x+1 < c && y+1 < r))
		return false;
//	printf("%c %c %c %c\n", grid[y][x], grid[y+1][x], grid[y][x+1], grid[y+1][x+1]);
	if (!(grid[y][x] == grid[y+1][x] && grid[y][x] == grid[y][x+1] && grid[y][x] == grid[y+1][x+1] && grid[y][x] == '#'))
		return false;
	grid[y][x] = '/';
	grid[y+1][x] = '\\';
	grid[y][x+1] = '\\';
	grid[y+1][x+1] = '/';
	return true;
}

void output() {
	printf("Case #%d:\n", C+1);
	FOR(i,0,r)
		printf("%s\n", grid[i]);
}
/*
void dfs(int x, int y, int depth) {
	if (SOLVED) return;
	if (depth == n_blue)
		output();
	if (place(x,y)) {
		FOR(i,y,r)
			FOR(j,x,c) {
				if (SOLVED) return;
				if (grid[i][j] == '#')
					dfs(j,i,depth+1);
			}
	}
}*/

int main() {
	scanf("%d", &T);
	FOR(i,0,T) {
		n_blue = 0; C = i; SOLVED = false;
		scanf("%d %d", &r, &c);
		FOR(j,0,r)
			scanf("%s", grid[j]);
		FOR(j,0,r)
			FOR(k,0,c)
				if (grid[j][k] == '#')
					n_blue++;
		if (n_blue && n_blue%4 == 0) {
			FOR(j,0,r)
				FOR(k,0,c)
					if (grid[j][k] == '#') {
						if (!place(k,j))
							j = r, k = c;
						n_blue -= 4;
					}
			if (n_blue == 0)
				output();
			else
				printf("Case #%d:\nImpossible\n", i+1);	
		}
		else
			output();
	}

	return 0;
}