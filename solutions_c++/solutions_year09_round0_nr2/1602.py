#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char basins[100][100];
char curbasin = 'a';

int map[100][100];
int W, H;

int di[] = {-1,  0, 0, 1};
int dj[] = { 0, -1, 1, 0};

char solve(int i, int j) {
	if(!basins[i][j]) {
		int min = 1<<15;
		int mink = -1;
		char basin;
		
		for(int k = 0; k < 4; k++) {
			if(i + di[k] < 0 || i + di[k] >= H) continue;
			if(j + dj[k] < 0 || j + dj[k] >= W) continue;
			
			if(map[i][j] > map[i + di[k]][j + dj[k]]) {
				// it flows!
				if(min > map[i + di[k]][j + dj[k]]) {
					min = map[i + di[k]][j + dj[k]];
					mink = k;
				}
			}
		}
		
		if(mink == -1) {
			basins[i][j] = curbasin++;
		} else {
			basins[i][j] = solve(i + di[mink], j + dj[mink]);
		}
	}
	
	return basins[i][j];
}

int main() {
	int T;
	
	scanf("%d\n", &T);
	
	for(int ti = 1; ti <= T; ti++) {
		scanf("%d %d\n", &H, &W);
		
		for(int i = 0; i < H; i++) {
			for(int j = 0; j < W; j++) {
				scanf("%d", &map[i][j]);
			}
		}
		
		curbasin = 'a';
		memset(basins, 0, sizeof(basins));
		printf("Case #%d:\n", ti);
		for(int i = 0; i < H; i++) {
			printf("%c", solve(i, 0));
			for(int j = 1; j < W; j++) {
				printf(" %c", solve(i, j));
			}
			printf("\n");
		}
	}
	
	
	return 0;
}
