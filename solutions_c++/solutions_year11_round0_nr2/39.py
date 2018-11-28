#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

bool opp[26][26];
char conv[26][26];


int main() {
	FILE *f = fopen("B.in", "r");
	FILE *fout = fopen("B.out", "w");

	int test; fscanf(f, "%d", &test);
	for (int tt = 1; tt <= test; tt++) {
		for (int i = 0; i < 26; i++)
			for (int j = 0; j < 26; j++) {
				opp[i][j] = false;
				conv[i][j] = '?';
			}

		int c; fscanf(f, "%d", &c);
		for (int i = 0; i < c; i++) {
			char line[10];
			fscanf(f, " %s", line);
			int c1 = (int)(line[0] - 'A');
			int c2 = (int)(line[1] - 'A');
			conv[c1][c2] = line[2];
			conv[c2][c1] = line[2];
		}

		int d; fscanf(f, "%d", &d);
		for (int i = 0; i < d; i++) {
			char line[10];
			fscanf(f, " %s", line);
			int c1 = (int)(line[0] - 'A');
			int c2 = (int)(line[1] - 'A');

			opp[c1][c2] = true;
			opp[c2][c1] = true;
		}

		int n;
		char line[200];
		fscanf(f, "%d %s", &n, line);

		char sol[200];
		int solCnt = 0;
		for (int i = 0; i < n; i++) {
			int cNov = (int)(line[i] - 'A');
			if (solCnt > 0 && conv[cNov][(int)(sol[solCnt-1] - 'A')] != '?') {
				sol[solCnt - 1] = conv[cNov][(int)(sol[solCnt-1] - 'A')];
			}
			else {
				bool opa = false;
				for (int j = 0; j < solCnt; j++){
					if (opp[(int)(sol[j] - 'A')][cNov]){
						opa = true;
						break;
					}
				}

				if (opa) solCnt = 0;
				else sol[solCnt++] = line[i];
			}
		}

		fprintf(fout, "Case #%d: [", tt);
		for (int i = 0; i < solCnt; i++) {
			if (i > 0) fprintf(fout, ", ");
			fprintf(fout, "%c", sol[i]);
		}
		fprintf(fout, "]\n");
	}

	fclose(f);
	fclose(fout);

	return 0;
}
