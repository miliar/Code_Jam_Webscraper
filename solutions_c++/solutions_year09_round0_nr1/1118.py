#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

const int maxl = 100;
const int maxd = 6000;

char dict[maxd][maxl];
set<char> pattern[maxl];
int L, D, N;

int main() {
	scanf("%d %d %d", &L, &D, &N);
	int i, j, k;
	for (i = 0; i < D; i++)
		scanf("%s", dict[i]);
	for (i = 0; i < N; i++) {
		printf("Case #%d: ", i + 1);
		for (j = 0; j < L; j++) {
			char ch;
			scanf(" %c", &ch);
			pattern[j].clear();
			if (ch != '(') {
				pattern[j].insert(ch);
				continue;
			}
			while (1) {
				scanf(" %c", &ch);
				if (ch == ')') break;
				pattern[j].insert(ch);
			}
		}
		int ans = 0;
		for (j = 0; j < D; j++) {
			for (k = 0; k < L; k++)
				if (pattern[k].find(dict[j][k]) == pattern[k].end()) break;
			ans += k == L;
		}
		printf("%d\n", ans);
	}
	return 0;
}
