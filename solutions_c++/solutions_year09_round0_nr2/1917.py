#include <stdio.h>
#include <string.h>

int i, j, k, T, W, H;
int map[100][100];
int foundAllocatedSink;
char output[100][100];
int direction[4][2] = {0, -1, -1, 0, 1, 0, 0, 1};

void flow(int y, int x, int alpha) {
	int tx, ty;
	int i, j, dir, alt;
	char oldalpha;
	while (1) {
		output[y][x] = alpha;
		alt			 = 0x7FFFFFFF;
		dir			 = -1;
		for (i = 0; i < 4; i++) {
			tx = x + direction[i][0];
			ty = y + direction[i][1];
			if (tx < 0 || ty < 0 || tx >= W || ty >= H) continue;
			if (map[ty][tx] < map[y][x] && alt > map[ty][tx]) {
				dir = i;
				alt = map[ty][tx];
			}
		}
		if (dir == -1) { // sink
			break;
		}
		x += direction[dir][0];
		y += direction[dir][1];
		if (output[y][x] != 0) {
			foundAllocatedSink = 1;
			oldalpha = output[y][x];
			break;
		}
	}
	if (foundAllocatedSink) {
		for (i = 0; i < H; i++) {
			for (j = 0; j < W; j++) {
				if (output[i][j] == alpha) {
					output[i][j] = oldalpha;
				}
			}
		}
	}
}
void doProcess(FILE *fout, int index) {
	int i, j;
	char alpha = 'a';
	for (i = 0; i < H; i++) {
		for (j = 0; j < W; j++) {
			output[i][j] = 0;
		}
	}
	for (i = 0; i < H; i++) {
		for (j = 0; j < W; j++) {
			if (output[i][j] == 0) {
				foundAllocatedSink = 0;
				flow(i, j, alpha);
				if (!foundAllocatedSink) {
					alpha++;
				}
			}
		}
	}
	fprintf(fout, "Case #%d:\n", index);
	for (i = 0; i < H; i++) {
		for (j = 0; j < W; j++) {
			fprintf(fout, "%c ", output[i][j]);
		}
		fprintf(fout, "\n");
	}
}
void main() {
	char str[1024];
	int i, j, k;

	FILE *fp;
	FILE *fout;
	printf("input> ");
	gets(str);
	fp = fopen(str, "r");
	fout = fopen("out.txt", "w+");

	fscanf(fp, "%d\n", &T);
	for (i = 0; i < T; i++) {
		fscanf(fp, "%d %d\n", &H, &W);
		for (j = 0; j < H; j++) {
			for (k = 0; k < W; k++) {
				fscanf(fp, "%d", &map[j][k]);
			}
		}
		doProcess(fout, i + 1);
	}

	fclose(fp);
	fclose(fout);
}
