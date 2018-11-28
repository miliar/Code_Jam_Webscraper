#include <cstdio>

using namespace std;

int main () {
	int T, C, D, N;
	char combine[26][26];
	char oppose[26];
	char groups[3], s[169], r[169];
	int r_l;

	scanf("%i", &T);
	for (int t = 1; t <= T; ++t) {
		for (int x = 0; x < 26; ++x) {
			for (int y = 0; y < 26; ++y) {
				combine[x][y] = 0;
			}
		}
		for (int x = 0; x < 26; ++x) {
			oppose[x] = 0;
		}
		scanf("%i ", &C);
		for (int c = 0; c < C; ++c) {
			scanf("%s ", groups);
			combine[groups[0] - 'A'][groups[1] - 'A'] = groups[2];
			combine[groups[1] - 'A'][groups[0] - 'A'] = groups[2];
		}
		scanf("%i ", &D);
		for (int d = 0; d < D; ++d) {
			scanf("%s ", groups);
			oppose[groups[0] - 'A'] = groups[1];
			oppose[groups[1] - 'A'] = groups[0];
		}
		scanf("%i %s", &N, s);
		r_l = 0;
		for (int n = 0; n < N; ++n) {
			r[r_l++] = s[n] - 'A';
			if (r_l > 1) {
				if (combine[r[r_l - 2]][r[r_l - 1]]) {
					r[r_l - 2] = combine[r[r_l - 2]][r[r_l - 1]] - 'A';
					--r_l;
				} else {
					for (int r_p = 0; r_p < r_l - 1; ++r_p) {
						if (oppose[r[r_l - 1]] == r[r_p] + 'A') {
							r_l = 0;
							break;
						}
					}
				}
			}
		}
		printf("Case #%i: [", t);
		for (int r_p = 0; r_p < r_l - 1; ++r_p) {
			printf("%c, ", r[r_p] + 'A');
		}
		if (r_l > 0) {
			printf("%c", r[r_l - 1] + 'A');
		}
		printf("]\n");
	}
}

