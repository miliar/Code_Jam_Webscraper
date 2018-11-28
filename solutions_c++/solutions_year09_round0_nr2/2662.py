#include<cstdio>
#define N 1
#define W 2
#define E 3
#define S 4
#define SINK 0

int map[100][100][3];
int out[26];
int h, w, t, c = 0;

void fill(int i, int j, int letter) {
	map[i][j][2] = letter;
	if(i > 0 && (map[i-1][j][1] == S) && map[i-1][j][2] == -1)
		fill(i-1, j, letter);
	if(j > 0 && (map[i][j-1][1] == E) && map[i][j-1][2] == -1)
		fill(i, j-1, letter);
	if(i < h-1 && (map[i+1][j][1] == N) && map[i+1][j][2] == -1)
		fill(i+1, j, letter);
	if(j < w - 1 && (map[i][j+1][1] == W) && map[i][j+1][2] == -1)
		fill(i, j+1, letter);
	return;
}

int main(void) {
	int i, j, alt, min, side;
	scanf("%d",&t);
	while(t--) {
		for(i = 0; i < 26; i++) out[i] = -1;
		scanf("%d %d",&h, &w);
		for(i = 0; i < h; i++)
			for(j = 0; j < w; j++)
				scanf("%d",&map[i][j][0]);
		for(i = 0; i < h; i++) {
			for(j  = 0; j < w; j++) {
				alt = min = map[i][j][0];
				side = SINK;
				if(i > 0 && map[i-1][j][0] < min) {
					min = map[i-1][j][0];
					side = N;
				}
				if(j > 0 && map[i][j-1][0] < min) {
					min = map[i][j-1][0];
					side = W;
				}
				if(j < w-1 && map[i][j+1][0] < min) {
					min = map[i][j+1][0];
					side = E;
				}
				if(i < h-1 && map[i+1][j][0] < min) {
					min = map[i+1][j][0];
					side = S;
				}
				map[i][j][1] = side;
				map[i][j][2] = -1;
			}
		}
		min = 0;
		for(i = 0; i < h; i++) {
			for(j = 0; j < w; j++) {
				if(map[i][j][1] == SINK && map[i][j][2] == -1)
					fill(i, j, min++);
			}
		}
		min = 0;
		printf("Case #%d:\n",++c);
		for(i = 0; i < h; i++) {
			for(j = 0; j < w; j++) {
				if(out[map[i][j][2]] == -1) {
					out[map[i][j][2]] = min++;
				}
				if(j) printf(" ");
				printf("%c",out[map[i][j][2]] + 'a');
			}
			printf("\n");
		}
	}
	return 0;
}
