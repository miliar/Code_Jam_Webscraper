#include <algorithm>
#include <vector>
#include <stdio.h>
#include <string.h>

#define MAX_N ((long long)10000)
#define MAX_WORD 10

char dict[MAX_N][MAX_WORD + 1];
int word_len[MAX_N];
std::vector<bool> compatible(26LL * MAX_N * MAX_N);
int wrong[MAX_N];
bool has_char[26][MAX_N];

int main() {
	int T = 0;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		std::fill(compatible.begin(), compatible.end(), false);
		memset(has_char, 0, sizeof has_char);
		int N, M;
		scanf("%d %d", &N, &M);
		for (int n = 0; n < N; ++n) {
			scanf(" %s", dict[n]);
			word_len[n] = strlen(dict[n]);
			for (int c = 'a'; c <= 'z'; ++c)
				for (int i = 0; i < word_len[n]; ++i)
					if (dict[n][i] == c) has_char[c-'a'][n] = true;
		}
		printf("Case #%d:", t + 1);
		for (int m = 0; m < M; ++m) {
			char order[27];
			scanf(" %s", order);
			for (int c = 'a'; c <= 'z'; ++c) {
				for (int i = 0; i < N; ++i) {
					for (int j = 0; j < N; ++j) {
						if (word_len[i] != word_len[j]) continue;
						bool ok = true;
						for (int p = 0; p < word_len[i]; ++p) {
							if ((dict[i][p] == c) != (dict[j][p] == c)) {
								ok = false;
								break;
							}
						}
						if (ok) compatible[((c-'a') * MAX_N + i) * MAX_N + j] = true;
					}
				}
			}
			int best = -1;
			int solution = -1;
			//fprintf(stderr, "> order = %s\n", order);
			for (int n = 0; n < N; ++n) {
				fprintf(stderr, "> word = %s\n", dict[n]);
				memset(wrong, 0, sizeof wrong);
				int lost_points = 0;
				for (int n2 = 0; n2 < N; ++n2) wrong[n2] = word_len[n] != word_len[n2];
				int last_guess = 0;
				for (int g = 0; g < 26; ++g) if (has_char[order[g]-'a'][n]) last_guess = g;
				fprintf(stderr, "> last_guess = %d (%c)\n", last_guess, order[last_guess]);
				for (int g = 0; g <= last_guess; ++g) {
					fprintf(stderr, "> g = %d\n", g);
					bool needed = false;
					for (int n2 = 0; n2 < N; ++n2) {
						if (!wrong[n2] && has_char[order[g]-'a'][n2]) {
							needed = true;
							break;
						}
					}
					fprintf(stderr, "> guess '%c' needed = %d\n", order[g], needed);
					if (needed) {
						//fprintf(stderr, "> accessing compatible[%lld]\n", 
						for (int n2 = 0; n2 < N; ++n2) wrong[n2] = wrong[n2] || !compatible[((order[g]-'a') * MAX_N + n) * MAX_N + n2];
						if (!has_char[order[g]-'a'][n]) ++lost_points;
					}
					fprintf(stderr, "> next g...\n");
				}
				fprintf(stderr, "> lost_points = %d, word = %s\n", lost_points, dict[n]);
				if (lost_points > best) {
					best = lost_points;
					solution = n;
				}
			}
			printf(" %s", dict[solution]);
		}
		printf("\n");
	}
}
