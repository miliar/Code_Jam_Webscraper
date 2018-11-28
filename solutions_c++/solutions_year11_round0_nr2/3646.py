#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 110;
const int SIGMA = 256;
const int BASE_CHARS[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

int tests, n, len;
int combinations, oppositions;
char comb[SIGMA][SIGMA];
int opp[SIGMA][SIGMA];
char charList[MAXN]; int isInList[SIGMA];

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	scanf("%d ", &tests);
	for (int t = 1; t <= tests; ++t) {
		memset(comb, 0, sizeof(comb));
		memset(opp, 0, sizeof(opp));
		memset(isInList, 0, sizeof(isInList));

		scanf("%d ", &combinations);
		for (int i = 1; i <= combinations; ++i) {
			char x, y, z;
			scanf("%c%c%c ", &x, &y, &z);
			comb[(int) x][(int) y] = comb[(int) y][(int) x] = z;
		}

		scanf("%d ", &oppositions);
		for (int i = 1; i <= oppositions; ++i) {
			char x, y;
			scanf("%c%c ", &x, &y);
			opp[(int) x][(int) y] = opp[(int) y][(int) x] = 1;
		}

		scanf("%d ", &n);
		len = 0;
		for (int i = 1; i <= n; ++i) {
			char c;
			scanf("%c ", &c);
			if (len > 0 && comb[(int) charList[len]][(int) c] != 0) {
				--isInList[(int) charList[len]];
				charList[len] = comb[(int) charList[len]][(int) c];
				++isInList[(int) charList[len]];
			} else {
				int found = 0;

				for (int j = 0; j < 8; ++j)
					if (opp[(int) c][(int) BASE_CHARS[j]] && isInList[(int) BASE_CHARS[j]])
						found = 1;

				if (found) {
					len = 0;
					memset(isInList, 0, sizeof(isInList));
				} else {
					charList[++len] = c;
					++isInList[(int) c];
				}
			}
		}

		if (len == 0) {
			printf("Case #%d: []\n", t);
		} else {
			printf("Case #%d: [%c", t, charList[1]);
			for (int i = 2; i <= len; ++i)
				printf(", %c", charList[i]);
			printf("]\n");
		}
	}

	return 0;
}
