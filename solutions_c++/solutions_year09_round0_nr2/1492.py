#include <cstdio>
#include <cstdlib>

#define INF 1000000000
#define MAX 100

int map[MAX+2][MAX+2];
char basin[MAX+2][MAX+2];
int h,w;
char freebasin = 'a';

char dfs(int x, int y) {
	// if already done
	if(basin[x][y] != 0)
		return basin[x][y];
	// if sink
	if(map[x+1][y] >= map[x][y] && map[x-1][y] >= map[x][y] &&
				map[x][y+1] >= map[x][y] && map[x][y-1] >= map[x][y]) {
		basin[x][y] = freebasin;
		freebasin++;
		return basin[x][y];
	}
	// else which way it flows..
	int lowest = map[x][y];
	if(map[x][y-1] < lowest) lowest = map[x][y-1]; // NORTH
	if(map[x-1][y] < lowest) lowest = map[x-1][y]; // WEST
	if(map[x+1][y] < lowest) lowest = map[x+1][y]; // EAST
	if(map[x][y+1] < lowest) lowest = map[x][y+1]; // SOUTH
	
	if(map[x][y-1] == lowest) { basin[x][y] = dfs(x,y-1); return basin[x][y]; } // NORTH
	if(map[x-1][y] == lowest) { basin[x][y] = dfs(x-1,y); return basin[x][y]; } // WEST
	if(map[x+1][y] == lowest) { basin[x][y] = dfs(x+1,y); return basin[x][y]; } // EAST
	if(map[x][y+1] == lowest) { basin[x][y] = dfs(x,y+1); return basin[x][y]; } // SOUTH
}

int solve(int nr) {
	freebasin = 'a';
	scanf("%d %d", &h, &w);
	for(int y = 0; y < h; y++)
		for(int x = 0; x < w; x++) {
			scanf("%d", &map[x+1][y+1]);
			basin[x+1][y+1] = 0;
		}
		for(int y = 0; y <= h+1; y++)
			map[0][y] = map[w+1][y] = INF;
		for(int x = 0; x <= w+1; x++)
			map[x][0] = map[x][h+1] = INF;
		
		for(int y = 1; y <= h; y++)
			for(int x = 1; x <= w; x++)
				if(basin[x][y] == 0)
					dfs(x,y);
	
	printf("Case #%d:\n", nr);
	for(int y = 1; y <= h; y++) {
		for(int x = 1; x <= w; x++)
			printf("%c ", basin[x][y]);
		printf("\n");
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
		solve(i);
}