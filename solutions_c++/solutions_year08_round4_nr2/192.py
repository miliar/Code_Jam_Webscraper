#include <stdio.h>

int c, n, m, a;

int main() {
	FILE * fin = fopen("triangle.in", "r"), * fout = fopen("triangle.out", "w");
	int i, X, Y, x, y;
	fscanf(fin, "%d", &c);
	for (i = 1; i <= c; ++i) {
		fscanf(fin, "%d%d%d", &n, &m, &a);
		for (X = n; X > 0; --X) {
			for (Y = m; X * Y > a; --Y) {
				y = Y;
				for (x = 1; x <= X && y > 0; ++x) {
					for ( ; y > 0; --y) {
						if (X * Y - x * y >= a) {
							break;
						}
					}
					if (X * Y - x * y == a) {
						break;
					}
				}
				if (x <= X && y > 0) {
					break;
				}
			}
			if (X * Y >= a) {
				if (X * Y == a) {
					x = X;
					y = 0;
				}
				break;
			}
		}
		if (X > 0) {
			fprintf(fout, "Case #%d: 0 0 %d %d %d %d\n", i, X, y, x, Y);
		} else {
			for (X = n; X > 0; --X) {
				for (Y = m; X * Y > a; --Y) {
					y = Y;
					for (x = 1; x <= X && y > 0; ++x) {
						for ( ; y > 0; --y) {
							if (X * Y - X * y - x * Y >= a) {
								break;
							}
						}
						if (X * Y - X * y - x * Y == a) {
							break;
						}
					}
					if (x <= X && y > 0) {
						break;
					}
				}
				if (X * Y > a) {
					break;
				}
			}
			if (X > 0) {
				fprintf(fout, "Case #%d: 0 0 %d %d %d %d\n", i, x, Y - y, X, Y);
			} else {
				fprintf(fout, "Case #%d: IMPOSSIBLE\n", i);
			}
		}
	}
	return 0;
}
