#include <cstdio>
#include <cstring>

const int dire[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
const int maxn = 100000;

int father[maxn], height[maxn];
char color[maxn];
int H, W;

int Find_Father(int v) {
	return father[v] == v ? v : father[v] = Find_Father(father[v]);
}

void Merge(int a, int b) {
	father[Find_Father(a)] = Find_Father(b);
}

bool Outside(int x, int y) {
	return x < 0 || y < 0 || x >= H || y >= W;
}

int Code(int x, int y) {
	return x * W + y;
}

void Solve() {
	scanf("%d %d", &H, &W);
	int i, j, d, x, y, _x, _y, hh;
	for (i = 0; i < H * W; i++)
	    father[i] = i;
	for (i = 0; i < H * W; i++)
		scanf("%d", &height[i]);
	for (i = 0; i < H; i++)
		for (j = 0; j < W; j++) {
            //printf(" %d : ", height[i * W + j]);
			hh = height[Code(i, j)];
			for (d = 0; d < 4; d++) {
				x = i + dire[d][0];
				y = j + dire[d][1];
				if (Outside(x, y)) continue;
				if (height[Code(x, y)] < hh) {
					hh = height[Code(x, y)];
					_x = x;
					_y = y;
				}
			}
			if (hh == height[Code(i, j)]) continue;
			Merge(Code(i, j), Code(_x, _y));
		}
	for (i = 0; i < H * W; i++)
		color[i] = -1;
	char ch = 'a';
	for (i = 0; i < H * W; i++) {
		int f = Find_Father(i);
		if (color[f] == -1) color[f] = ch++;
	}
	for (i = 0; i < H; i++) {
		for (j = 0; j < W; j++) {
			if (j) printf(" ");
			printf("%c", color[Find_Father(Code(i, j))]);
		}
		printf("\n");
	}
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		printf("Case #%d:\n", i + 1);
		Solve();
	}
	return 0;
}
