#include <stdio.h>
#include <string.h>

#define ARR_MAX 100000
#define CHAR_MAX 20
#define FEATURE_MAX 200

int T, L, a, n;
char t[ARR_MAX];
int len;
int s[ARR_MAX], st;
double w[ARR_MAX];
char f[ARR_MAX][CHAR_MAX];
int l[ARR_MAX], r[ARR_MAX], cnt;
char animal[CHAR_MAX], feature[FEATURE_MAX][CHAR_MAX];
int v;
double p;

int main() {
	int lT, i, j;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (lT = 1; lT <= T; lT++) {
		scanf("%d\n", &L);
		len = 0;
		for (i = 0; i < L; i++) {
			gets(t + len);
			while (t[len] != (char) NULL) len++;
			t[len++] = ' ';
		}
		t[len] = (char) NULL;
		st = 0;
		s[st] = cnt = 0;
		l[s[st]] = r[s[st]] = -1;
		for (i = 0; i < len; i++) {
			if (t[i] == '(') {
				if (l[s[st]] == -1)
					l[s[st]] = ++cnt;
				else
					r[s[st]] = ++cnt;
				s[++st] = cnt;
				l[s[st]] = r[s[st]] = -1;
				sscanf(t + i + 1, "%lf", &w[s[st]]);
			} else if ('a' <= t[i] && t[i] <= 'z') {
				sscanf(t + i, "%s", f[s[st]]);
				while ('a' <= t[i] && t[i] <= 'z') i++;
			} else if (t[i] == ')')
				st--;
		}
		printf("Case #%d:\n", lT);
		scanf("%d", &a);
		for (i = 0; i < a; i++) {
			scanf("%s%d", animal, &n);
			for (j = 0; j < n; j++)
				scanf("%s", &feature[j]);
			v = 1;
			p = 1;
			while (true) {
				p *= w[v];
				if (l[v] == -1) break;
				for (j = 0; j < n; j++)
					if (!strcmp(f[v], feature[j])) break;
				if (j < n) v = l[v];
				else v = r[v];
			}
			printf("%.7lf\n", p);
		}
	}
	return 0;
}