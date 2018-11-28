#include <cstdio>

int an(int n, int pd, int pg) {
	if (n < 2) {
		if (pd % 100) {
			return 0;
		}
	} else if (n < 4) {
		if (pd % 50) {
			return 0;
		}
	} else if (n < 5) {
		if (pd % 25) {
			return 0;
		}
	} else if (n < 10) {
		if ((pd % 20) && (pd % 25)) {
			return 0;
		}
	} else if (n < 20) {
		if ((pd % 10) && (pd % 25)) {
			return 0;
		}
	} else if (n < 25) {
		if (pd % 5) {
			return 0;
		}
	} else if (n < 50) {
		if ((pd % 4) && (pd % 5)) {
			return 0;
		}
	} else if (n < 100) {
		if ((pd % 2) && (pd % 5)) {
			return 0;
		}
	}
	if (pg % 100) {
		return 1;
	}
	if (pd != pg) {
		return 0;
	}
	return 1;
}

int main() {
	FILE * fin = fopen("freecell.in", "r"), * fout = fopen("freecell.out", "w");
	int T, n, pd, pg, i;
	fscanf(fin, "%d", &T);
	for (i = 1; i <= T; ++i) {
		fscanf(fin, "%d %d %d", &n, &pd, &pg);
		if (an(n, pd, pg)) {
			fprintf(fout, "Case #%d: Possible\n", i);
		} else {
			fprintf(fout, "Case #%d: Broken\n", i);
		}
	}
	return 0;
}