#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
using namespace std;

int t, n, m;
char word[10005][15], list[105][30];
int main() {
	FILE *fin = fopen("B.in", "r");
	FILE *fout = fopen("B.out", "w");

	fscanf(fin, "%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		fscanf(fin, "%d %d\n", &n, &m);
		for (int i = 0; i < n; i++) fgets(word[i], 15, fin);
		for (int i = 0; i < m; i++) fgets(list[i], 30, fin);


		//bool exist[30];
		//memset(exist, 0, sizeof(exist));
		//for (int i = 0; i < n; i++) for (int j = 0; j < 15; j++) if ((word[i][j] >= 'a') && (word[i][j] <= 'z')) exist[word[i][j]-'a'] = true;

		printf("Case #%d:", cas);
		fprintf(fout, "Case #%d:", cas);
		//printf("%d\n", cas);

		for (int j = 0; j < m; j++) {
			// using list j
			
			int ans = -1, sol;
			for (int i = 0; i < n; i++) {
				// using word i
				bool ok[10005];
				memset(ok, 1, sizeof(ok));

				int guess = 0, numleft = n;

				for (int k = 0; k < n; k++) if (strlen(word[k]) != strlen(word[i])) {
					//printf("%s bad\n", word[k]);
					ok[k] = false;
					numleft--;
				}

				for (int l = 0; l < 26; l++) {
					char c = list[j][l];

					bool exist = false;
					for (int k = 0; k < n; k++) if (ok[k]) for (int x = 0; word[k][x] >= 'a' && word[k][x] <= 'z'; x++) if (word[k][x] == c) exist = true;
					if (!exist || numleft == 1) continue;

					//printf("guessing %c\n", c);
					exist = false;
					for (int x = 0; word[i][x] >= 'a' && word[i][x] <= 'z'; x++) if (word[i][x] == c) exist = true;
					if (!exist) guess++;
					for (int k = 0; k < n; k++) {
						for (int d = 0; word[k][d] != '\0'; d++) {
							if ((word[k][d] == c && word[i][d] != c) || (word[k][d] != c && word[i][d] == c)) {
								if (ok[k] == true) {
									ok[k] = false;
									numleft--;
								}
							}
						}
					}
				}

				//printf("guess %d\n", guess);

				if (guess > ans) {
					ans = guess;
					sol = i;
				}

			}
			//printf("sol %d\n", sol);
			printf(" ");
			fprintf(fout, " ");
			for (int i = 0; word[sol][i] >= 'a' && word[sol][i] <= 'z'; i++) printf("%c", word[sol][i]);
			for (int i = 0; word[sol][i] >= 'a' && word[sol][i] <= 'z'; i++) fprintf(fout, "%c", word[sol][i]);
			
		}
		printf("\n");
		fprintf(fout, "\n");
	}

	return 0;
}
