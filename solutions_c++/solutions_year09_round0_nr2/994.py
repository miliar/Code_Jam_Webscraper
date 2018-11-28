#include <stdio.h>
#include <stdlib.h>

int input[105][105];
int map[105][105];

int current;
int T,H,W;
int dx[4][2] = {
	{ -1, 0 },
	{ 0, -1 },
	{ 0, 1 },
	{ 1, 0 }
};

int rek( int y, int x ) {
	int res;
	int new_y, new_x;
	int best_y, best_x;
	int found = 0;
	int min;
	int d;

	if ( map[y][x] != -1 ) {
		return map[y][x];
	}

	min = input[y][x];
	for (d=0; d<4; d++) {
		new_y = y + dx[d][0];
		new_x = x + dx[d][1];
		if ( new_y < 0 ) continue;
		if ( new_x < 0 ) continue;
		if ( new_y == H ) continue;
		if ( new_x == W ) continue;
		if ( input[new_y][new_x] < min ) {
			min = input[new_y][new_x]; 
			best_y = new_y;
			best_x = new_x;
			found = 1;
		}
	}

	if ( !found ) {
		res = current++;
	} else {
		res = rek( best_y, best_x );
	}

	return map[y][x] = res;
}

int main ( int argc, char ** argv ) {
	int x,y,casenr;
	scanf("%d", &T);
	for (casenr=0; casenr<T; casenr++) {
		scanf("%d %d", &H, &W);
		for (y=0; y<H; y++) {
			for (x=0; x<W; x++) {
				scanf("%d", &input[y][x]);
				map[y][x] = -1;
			}
		}
		current = 0;
		for (y=0; y<H; y++) {
			for (x=0; x<W; x++) {
				rek( y, x );
			}
		}


		printf("Case #%d:\n", casenr+1);
		for (y=0; y<H; y++) {
			for (x=0; x<W; x++) {
				if ( x ) printf(" ");
				printf("%c", map[y][x]+'a');
			}
			printf("\n");
		}

	}

	return 0;
}

