#include <iostream>
using namespace std;

const int MAX_N = 128 * 128;
const int DX[] = {0, -1, 1, 0};
const int DY[] = {-1, 0, 0, 1};

int f[MAX_N];
char l[MAX_N];
int a[MAX_N];
int cx, cy;
int t;

int id(int x, int y) {
	return x * cy + y;
}

void make_set(int i) {
	f[i] = i;
}

int find_set(int i) {
	if (f[i] == i)
		return i;
	else
		return f[i] = find_set(f[i]);
}

void merge_set(int x, int y) {
	x = find_set(x);
	y = find_set(y);
	f[y] = x;
}

bool valid(int x, int y) {
	return 0 <= x && x < cx && 0 <= y && y < cy;
}

int main() {
	cin >> t;
	for (int ti = 0; ti < t; ti++) {
		cin >> cy >> cx;
		for (int y = 0; y < cy; y++)
			for (int x = 0; x < cx; x++) {
				cin >> a[id(x, y)];
				make_set(id(x,y));
			}
		for (int x = 0; x < cx; x++)
			for (int y = 0; y < cy; y++) {
				int i = id(x, y);
				int m = 100000;
				int mi = -1;
				int mx, my;

				for (int d = 0; d < 4; d++) {
					int nx = x + DX[d];
					int ny = y + DY[d];
					if (!valid(nx,ny)) continue;
					int ni = id(nx, ny);
					if (a[i] <= a[ni]) continue;
					if (m > a[ni]) {
						m = a[ni];
						mi = ni;
						mx = nx;
						my = ny;
					}
				}

				if (mi >= 0) {
					merge_set(i, mi);
					// printf("merge (%d,%d) and (%d,%d)\n", x, y, mx, my);
					// printf("%d, %d\n", f[i], f[mi]);
					// printf("%d, %d\n", a[i], a[mi]);
				}
			}
		
		printf("Case #%d:\n", ti + 1);
		memset(l, 0, sizeof(l));
		char c = 'a';
		for (int y = 0; y < cy; y++)
			for (int x = 0; x < cx; x++) {
				int j = id(x, y);
				int i = find_set(j);
				// printf("i = %d, j = %d\n", i, j);
				if (l[i] == 0)
					l[i] = c++;
				printf("%c%c", l[i], x==cx-1 ? '\n' : ' ');
			}
	}
}

