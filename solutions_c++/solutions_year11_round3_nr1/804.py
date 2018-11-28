#include <cstdio>


int main() {
	FILE *fin = fopen("A-large.in", "rt");
	FILE *fout = fopen("out.txt", "wt");
	int T;

	fscanf(fin, "%d", &T);

	for (int t = 1; t <= T; ++t) {
		fprintf(fout, "Case #%d:\n", t);

		int n, m;
		int num = 0;
		bool ok = true;
		char A[100][100];

		fscanf(fin, "%d %d\n", &n, &m);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				fscanf(fin, "%c", &A[i][j]);
				if (A[i][j] == '#') ++num;
			}
			fscanf(fin, "\n");
		}
		while (num) {
			ok = false;
			for (int i = 0; i < n - 1; ++i) {
				for (int j = 0; j < m - 1; ++j) {
					if (A[i][j] == '#' && A[i + 1][j] == '#' && A[i][j + 1] == '#' && A[i + 1][j + 1] == '#') {
						A[i][j] = '/';
						A[i + 1][j] = '\\';
						A[i][j + 1] = '\\';
						A[i + 1][j + 1] = '/';
						num -= 4;
						ok = true;
						break;
					}
				}
				if (ok) break;
			}
			if (ok == false) break;
		}

		if (num == 0) {
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < m; ++j) {
					fprintf(fout, "%c", A[i][j]);
				}
				fprintf(fout, "\n");
			}
		} else {
			fprintf(fout, "Impossible\n");
		}
	}
	fclose(fout);
	return 0;
}