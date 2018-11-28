#include <cstdio>
#include <map>

using std::map;

int area[102][102];
int res[102][102];
int reduceMap[10003];

void unite(int a, int b) {
	if (reduceMap[a] >= reduceMap[b])
		reduceMap[a] = reduceMap[b];
	else
		reduceMap[b] = reduceMap[a];
}

void volna(int i, int j, int h, int w) {
	int x = i;
	int y = j;
	int lab = res[i][j];
	int mini, minj;
	do {
		mini = 0;
		minj = 0;
		int minv = area[x][y];
		for (int i = -1; i <= 1; i++)
			for (int j = -1; j <= 1; j++)
				if (i * i + j * j == 1) {
					int newx = x + i;
					int newy = y + j;
					if (newx >= 0 && newx < h && newy >= 0 && newy < w && area[newx][newy] < minv) {
						mini = i;
						minj = j;
						minv = area[newx][newy];
					}
				}
		x += mini;
		y += minj;
		if (res[x][y] && res[x][y] != lab) {
			unite(lab, res[x][y]);
			break;
		}
		res[x][y] = lab;
	} while (mini || minj);
}

void doIt(int h, int w) {
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
			res[i][j] = 0;
	int ind = 1;
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
			if (!res[i][j]) {
				reduceMap[ind] = ind;
				res[i][j] = ind++;
				volna(i, j, h, w);
			}
	char nextL = 'a';
	for (int i = 1; i < ind; i++)
		reduceMap[i] = reduceMap[reduceMap[i]];
	map<int, char> mm;
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++) {
			int cur = reduceMap[res[i][j]];
			if (mm.find(cur) == mm.end()) {
				mm[cur] = nextL++;
			}
			res[i][j] = mm[cur];
		}
}

int main(int argc, char **argv) {
	FILE *in = fopen(argv[1], "r");
	FILE *out = fopen("B-out.out", "w");
	int T;
	fscanf(in, "%d", &T);
	for (int i = 0; i < T; i++) {
		fprintf(out, "Case #%d:\n", i + 1);
		int H, W;
		fscanf(in, "%d%d", &H, &W);
		for (int j = 0; j < H; j++)
			for (int k = 0; k < W; k++)
				fscanf(in, "%d", &area[j][k]);
		doIt(H, W);
		for (int j = 0; j < H; j++) {
			for (int k = 0; k < W; k++)
				fprintf(out, "%c ", res[j][k]);
			fprintf(out, "\n");
		}
	}
	fclose(out);
	fclose(in);
}
