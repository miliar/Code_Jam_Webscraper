#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAX = 120;
char s[MAX];
char st[MAX];
char mp[30][30];
bool rel[30][30];
int top;

int main() {
	int T, cas = 1, n;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	while (T--) {
		memset(mp, 0, sizeof(mp));
		memset(rel, 0, sizeof(rel));
		scanf("%d", &n);
		while (n--) {
			scanf("%s", s);
			mp[s[0] - 'A'][s[1] - 'A'] = s[2];
			mp[s[1] - 'A'][s[0] - 'A'] = s[2];
		}
		scanf("%d", &n);
		while (n--) {
			scanf("%s", s);
			rel[s[0] - 'A'][s[1] - 'A'] = true;
			rel[s[1] - 'A'][s[0] - 'A'] = true;
		}
		scanf("%d", &n);
		top = 0;
		scanf("%s", s);
		for (int i = 0; i < n; i++) {
			if (top && mp[st[top - 1] - 'A'][s[i] - 'A']) {
				st[top - 1] = mp[st[top - 1] - 'A'][s[i] - 'A'];
			} else {
				st[top++] = s[i];
			}
			for (int j = top - 1; j >= 0; j--) {
				if (rel[st[j] - 'A'][st[top - 1] - 'A']) {
					top = 0;
					break;
				}
			}
		}
		printf("Case #%d: [", cas++);
		for (int i = 0; i < top; i++) {
			if (i)
				printf(", ");
			putchar(st[i]);
		}
		puts("]");
	}

	return 0;
}
