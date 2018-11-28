#include <cstdio>
#include <cstring>

using namespace std;

int t;
char cm[26][26];
char op[26][26];

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);

	scanf("%d", &t);
	for (int gi = 0; gi < t; gi++) {
		memset(cm, 0, sizeof(cm));
		memset(op, 0, sizeof(op));
		int c;
		int d;
		int wc;
		scanf("%d", &c);
		char comb[4];
		for (int i = 0; i < c; i++) {
			scanf("%s", comb);
			cm[comb[0]-'A'][comb[1]-'A'] = comb[2];
			cm[comb[1]-'A'][comb[0]-'A'] = comb[2];
		}
		scanf("%d", &d);
		for (int i = 0; i < d; i++) {
			scanf("%s", comb);
			op[comb[0]-'A'][comb[1]-'A'] = 1;
			op[comb[1]-'A'][comb[0]-'A'] = 1;
		}
		char str[101];
		char res[101];
		int ridx = 0;
		scanf("%d %s", &wc, str);
		res[0] = str[0];
		ridx++;
		for (int i = 1; i < wc; i++) {
			res[ridx] = str[i];
			if (ridx == 0) {
				ridx++;
				continue;
			}
			if (cm[res[ridx-1]-'A'][res[ridx]-'A']) {
				res[ridx-1] = cm[res[ridx-1]-'A'][res[ridx]-'A'];
				continue;
			}
			bool found = false;
			for (int j = 0; j < ridx; j++) {
				if (op[res[j]-'A'][res[ridx]-'A']) {
					ridx = 0;
					found = true;
					break;
				}
			}
			if (!found) {
				ridx++;
			}
		}
		printf("Case #%d: [", gi+1);
		if (ridx > 0) {
			printf("%c", res[0]);
			for (int i = 1; i < ridx; i++) {
				printf(", %c", res[i]);
			}
		}
		printf("]\n");
	}

	return 0;
}
