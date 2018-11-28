#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define M 10007
//2x+y = a
//x+2y = b
//x = (2a-b)/3
//y = (2b-a)/3

int w, h, r, rx[10], ry[10];
int map[100][100];
int main()
{
	int t, index;
	int i, j;
	scanf("%d", &t);
	for(index = 1; index <= t; index++) {
		scanf("%d%d%d", &h, &w, &r);
		memset(map, -1, sizeof(map));
		map[0][0] = 1;
		for(i = 0; i < r; i++) {
			scanf("%d%d", &rx[i], &ry[i]);
			map[rx[i]-1][ry[i]-1] = 0;
		}
		for(i = 0; i < h; i++)
			for(j = 0; j < w; j++) {
				if(map[i][j] >= 0)continue;
				map[i][j] = 0;
				if(i >= 2 && j >= 1)
					map[i][j] += map[i-2][j-1];
				if(i >= 1 && j >= 2)
					map[i][j] += map[i-1][j-2];
 				map[i][j] %= M;
			}
		printf("Case #%d: %d\n", index, map[h-1][w-1]);
	}
	return 0;
}

