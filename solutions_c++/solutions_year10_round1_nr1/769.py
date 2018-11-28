#include <cstdio>
#include <cstdlib>
#define input "A-large.in"
#define output "A.out"
using namespace std;

const int dy[4] = {-1, 0, -1, -1};
const int dx[4] = {0, -1, -1, 1};

int main()
{
	int cases, t;
	int i, j, k, l, n;
	FILE *fin = fopen(input, "r");
	FILE *fout = fopen(output, "w");

	fscanf(fin, "%d\n", &t);
	for (cases = 1; cases <= t; cases++) {
		char map[51][51] = {'\0', }, map2[51][51] = {'\0', };
		int cr[4][51][51] = {0, }, cb[4][51][51] = {0, };

		fscanf(fin, "%d %d\n", &n, &k);
		for (i = 0; i < n; i++) fscanf(fin, "%s", map[i]);

		for (i = 0; i < n; i++) {
			for (j = n - 1; j >= 0; j--) {
				if (map[i][j] == '.') {
					for (l = j - 1; l >= 0; l--) {
						if (map[i][l] != '.') {
							map[i][j] = map[i][l];
							map[i][l] = '.';
							break;
						}
					}
				}
			}
		}

		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				map2[i][j] = map[i][j];
			}
		}

		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				map[i][j] = map2[n - j - 1][i];
			}
		}


		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				for (l = 0; l < 4; l++) {
					if (map[i][j] == 'R') {
						if ((0 <= i + dy[l] && i + dy[l] < n && 0 <= j + dx[l] && j + dx[l] < n))
							cr[l][i][j] = cr[l][i + dy[l]][j + dx[l]] + 1;
						else 
							cr[l][i][j] = 1;
					}
					if (map[i][j] == 'B') {
						if ((0 <= i + dy[l] && i + dy[l] < n && 0 <= j + dx[l] && j + dx[l] < n))
							cb[l][i][j] = cb[l][i + dy[l]][j + dx[l]] + 1;
						else 
							cb[l][i][j] = 1;
					}
				}
			}
		}

		bool ib = false, ir = false;
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				for (l = 0; l < 4; l++) {
					if (cr[l][i][j] == k) {
						ir = true;
						/*
						if ((0 <= i - dy[l] && i - dy[l] < n && 0 <= j - dx[l] && j - dx[l] < n))
							if (cr[l][i - dy[l]][j - dx[l]] > k) ir = false; else ir = true;
						else ir = true;*/

					}
					
					if (cb[l][i][j] == k) {
						ib = true;
						/*
						if ((0 <= i - dy[l] && i - dy[l] < n && 0 <= j - dx[l] && j - dx[l] < n))
							if (cb[l][i - dy[l]][j - dx[l]] > k) ib = false; else ib = true;
						else ib = true;*/
					}
					
				}
			}
		}
/*
		printf("%d\n", k);
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				printf("%c", map[i][j]);
			}
			printf("\n");
		}
	
		printf("Case #%d: ", cases);
		if (ir && ib) printf("Both\n");
		if (ir && !ib) printf("Red\n");
		if (!ir && ib) printf("Blue\n");
		if (!ir && !ib) printf("Neither\n");
*/
		fprintf(fout, "Case #%d: ", cases);
		if (ir && ib) fprintf(fout, "Both\n");
		if (ir && !ib) fprintf(fout, "Red\n");
		if (!ir && ib) fprintf(fout, "Blue\n");
		if (!ir && !ib) fprintf(fout, "Neither\n");
//		getchar();

	}

	fclose(fout);
	fclose(fin);

	return 0;
}