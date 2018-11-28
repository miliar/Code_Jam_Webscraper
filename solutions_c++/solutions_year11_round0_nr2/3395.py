#include <stdio.h>
#include <vector>

#define FORab(i,a,b) for(int i = (a); i < (b); i++)
#define FORn(i,n) FORab(i,0,n)

#define MAXC 36
#define MAXD 28
#define MAXN 100

#define BI(c) baseIdx[c-'A']
#define BIs(i) BI(str[i])

#define DBG(args...) /*fprintf(stderr, args)*/

int main() {
	char base[] = "QWERASDF";
	int baseIdx[26];
	char combine[8][8];
	bool oppose[8][8];
	char str[MAXN+1], buf[MAXN+1];
	int counts[26];

	FORn(i,26) baseIdx[i] = -1;
	FORn(i,8) baseIdx[base[i]-'A'] = i;

	int T; scanf("%d", &T);

	for(int caseno = 1; caseno <= T; caseno++) {
		int C, D, N;

		// init
		FORn(i,8) FORn(j,8) {
			combine[i][j] = 0;
			oppose[i][j] = false;
		}
		FORn(i,26) counts[i] = 0;

		// combine
		scanf("%d", &C);
		FORn(i,C) {
			scanf("%s", str);
			int ai = BI(str[0]), bi = BI(str[1]);
			combine[ai][bi] = combine[bi][ai] = str[2];
		}

		FORn(i,8) FORn(j,8) {
			if(combine[i][j]) {
				DBG("%c + %c -> %c\n", base[i], base[j], combine[i][j]);
			}
		}

		// oppose
		scanf("%d", &D);
		FORn(i,D) {
			scanf("%s", str);
			int ai = BI(str[0]), bi = BI(str[1]);
			oppose[ai][bi] = oppose[bi][ai] = true;
		}

		FORn(i,8) FORn(j,8) {
			if(oppose[i][j]) {
				DBG("%c & %c oppose\n", base[i], base[j]);
			}
		}

		scanf("%d", &N);
		scanf("%s", str);
		int l = 0;

		// main logic
		FORn(i,N) {
			char c = str[i];
			buf[l++] = c;
			counts[c-'A']++;

			DBG("buf: ");
			FORn(j,l) DBG("%c", buf[j]);
			DBG("\n");

			FORn(j,26)
				if(counts[j]) DBG("%c: %d ", 'A'+j, counts[j]);
			DBG("\n");

			// Keep combining
			if(l > 1) {
				int ai = BI(buf[l-1]), bi = BI(buf[l-2]);
				while(ai != -1 && bi != -1 && combine[ai][bi]) {
					DBG("Combining ");
					FORn(j,l) DBG("%c", buf[j]);

					counts[buf[l-1]-'A']--;
					counts[buf[l-2]-'A']--;
					l--;
					buf[l-1] = combine[ai][bi];
					counts[combine[ai][bi]-'A']++;

					DBG(" -> ");
					FORn(j,l) DBG("%c", buf[j]);
					DBG("\n");

					if(l > 1) {
						ai = BI(buf[l-1]);
						bi = BI(buf[l-2]);
					} else {
						break;
					}
				}
			}

			// Check for opposing elements
			if(l > 1) {
				FORn(j,8) FORab(k,j,8) {
					if(oppose[j][k] && counts[base[j]-'A'] && counts[base[k]-'A']) {
						buf[l] = (char)NULL;
						DBG("Clearing %s due to %c & %c\n", buf, base[j], base[k]);
						l = 0;
						j = k = 26;
						FORn(j,26) counts[j] = 0;
					}
				}
			}
		}

		printf("Case #%d: [", caseno);
		FORn(i,l) {
			printf("%c", buf[i]);
			if(i < l-1) printf(", ");
		}
		printf("]\n");

		buf[l] = (char)NULL;
	}

	return 0;
}
