#include <stdio.h>
#include <string.h>

int k, tc;
int a[512][512];
int c[512];

/*
int scan_line(int y) {
	int r = 9999999;
	// odd
	for (int j = 1; j <= c[i]; j++) {
		for (int v = c; v > 0; v--) {
			if (a[y][v] != a[y][
		}
	}
}

int scan_lines() {
	int ret = 0; // max
	for (int i = 1; i < 2 * k; i++) {
		bool b = true;
		int p = 0; // should plus how many
		do {
			for (int j = 1; j <= c[i]; j++) {
				if (a[i][j] != a[i][c[i] + 1 - j]) {
					b = false;
					break;
				}
			}
			p ++;
		} while (b == false);
	}
	return ret;
}
*/
bool equal_a(int x1, int y1, int x2, int y2) {
	if (x1 >= 512 || y1 >= 512 || x1 < 0 || y1 < 0) return true;
	if (x2 >= 512 || y2 >= 512 || x2 < 0 || y2 < 0) return true;
	if (a[x1][y1] == -1) return true;
	if (a[x2][y2] == -1) return true;
	return (a[x1][y1] == a[x2][y2]);
}
bool check_x(int x, int y) { // x fixed(changed) var y
	int cd = (k - 1)*2 + 1;
	for (int t = 0; t < cd; ++t)
		if (!equal_a(x, y - t, x, y + t)) return false;	
	return true;
}
bool check_y(int x, int y) {
	int cd = (k - 1)*2 + 1;
	for (int t = 0; t < cd; ++t)
		if (!equal_a(x - t, y, x + t, y)) return false;	
	return true;
}
bool check(int x, int y) {
	// center x, y check deapth: (k - 1) * 2 all
	int cd = (k - 1)*2 + 1;
	for (int xi = x -  cd; xi <= x+cd;xi++)
		if (!check_x(xi,y)) return false;
	for (int yi = y -  cd; yi <= y+cd;yi++)
		if (!check_y(x,yi)) return false;
	return true;
}
int main(int argc, char const* argv[]) {
	scanf("%d", &tc);
	for (int ti = 0; ti < tc; ti++) {
		memset(a, -1, sizeof(a));

		scanf("%d", &k);

		for (int i = 1; i < 2 * k; i++) {
			int i_s = (i <= k) ? (i) : (2 * k - i);
			c[i] = i_s;
			int s_c = (i <= k) ? k - i : i - k;
			for (int j = 1; j <= i_s; j++) {
				int t;
				scanf("%d", &t);
				a[i - 1][s_c+ (j - 1) * 2] = t;
			}
		}
		/*
		for (int y = 0; y < 10; y++) {
			for (int x = 0; x < 10; x++) {
				printf("%3d", a[y][x]);
			}
			printf("\n");
		}
		printf("-------------------\n");
*/
		int xc = k - 1, yc = k - 1, r = 0, rl = -1;
//		if (!check(xc, yc)) 
		for (r = 0; r < k * 2; r++) {
			int x, y;
			x = xc; y = yc - r;
			while (y <= yc) {
				if (check(x, y)) {rl = r;break;}
				y++, x--;
			}

			if (rl != -1) break;
			x = xc; y = yc - r;
			while (y <= yc) {
				if (check(x, y)) {rl = r;break;}
				y++, x++;
			}
			if (rl != -1) break;

			x = xc; y = yc + r;
			while (y >= yc) {
				if (check(x, y)) {rl = r;break;}
				y--, x--;
			}
			if (rl != -1) break;

			x = xc; y = yc + r;
			while (y >= yc) {
				if (check(x, y)) {rl = r;break;}
				y--, x++;
			}
			if (rl != -1) break;
		}
		printf("Case #%d: %lld\n", ti + 1, (long long)(k + rl) * (k + rl) - (long long) k * k);
	}
	return 0;
}
