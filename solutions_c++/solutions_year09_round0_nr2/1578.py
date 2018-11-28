#include <limits.h>
#include <stdio.h>
#include <map>
using std::map;

const int MAX = 105;

int memo[MAX][MAX];
int heights[MAX][MAX];

int dy[] = {-1,0,0,1};
int dx[] = {0,-1,1,0};
int w,h,sinkid;

int getsink (int y, int x) {

	if (memo[y][x] != -1)
		return memo[y][x];

	int best = -1;
	int min_h = INT_MAX;
	for (int i = 0; i < 4; i++) {
		int new_y = y+dy[i];
		int new_x = x+dx[i];

		if (new_y >= 0 && new_y < h && new_x >= 0 && new_x < w) {
			if (heights[new_y][new_x] < min_h) {
				min_h = heights[new_y][new_x];	
				best = i;
			}
		}
	}
	if (min_h >= heights[y][x]) { 
		return memo[y][x] = sinkid++;
	}
	return memo[y][x] = getsink(y+dy[best],x+dx[best]);
}

int main () {
	int cases;
	scanf ("%d",&cases);

	for (int tt = 0; tt < cases; tt++) {
		scanf ("%d %d",&h,&w);
		sinkid = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				memo[i][j] = -1;
				scanf ("%d",&heights[i][j]);
			}
		}
		map<int,char> mapping;
		char cnt = 'a';
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (!mapping[getsink(i,j)])
					mapping[getsink(i,j)] = cnt++;
			}
		}
		printf ("Case #%d:\n",tt+1);
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (j != 0) printf (" ");
				printf ("%c",mapping[memo[i][j]]);
			}
			printf ("\n");
		}
	}

	return 0;
}
