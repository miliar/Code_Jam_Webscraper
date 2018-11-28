#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>

using namespace std;

#define NN 300
char m[NN][NN], d[NN][NN];
char l[NN]; int nl;
char s[NN]; int used[NN];

int main() {
	int N;
	scanf("%d", &N);
	for (int ct = 1; ct <= N; ct++) {
		memset(m, 0, sizeof m);
		memset(d, 0, sizeof d);
		int c; scanf("%d", &c);
		for (int i = 0; i < c; i++) {
			char u, v, t; scanf(" %c%c%c", &u, &v, &t);
			m[u][v] = t;
			m[v][u] = t;
		}

		int dd; scanf("%d", &dd);
		for (int i = 0; i < dd; i++) {
			char u, v, t; scanf(" %c%c%c", &u, &v, &t);
			d[u][v] = 1;
			d[v][u] = 1;
		}

		int n; scanf("%d", &n);
		scanf(" %s", s);

		memset(used, 0, sizeof used);
		nl = 0;
		for (int i = 0; i < n; i++) {
			l[nl++] = s[i];

			used[s[i]]++;
			while (nl > 1) {
				int a = l[nl-1], b = l[nl-2];
				if (m[a][b] != 0) {
					used[a]--;
					used[b]--;
					used[m[a][b]]++;
					l[nl-2] = m[a][b];
					nl--;
				} else break;

				for (int j = 0; j < NN; j++)
					if (d[l[nl-1]][j] > 0 && used[j] > 0) { 
						nl = 0; 
						memset(used, 0, sizeof used);
						break; 
					}
			}
			for (int j = 0; j < NN; j++)
				if (d[l[nl-1]][j] > 0 && used[j] > 0) { 
					nl = 0; 
					memset(used, 0, sizeof used);
					break; 
				}
		}

		printf("Case #%d: [", ct);
		if (nl > 0)
			printf("%c", l[0]);
		for (int i = 1; i < nl; i++) printf(", %c", l[i]);
		printf("]\n");
	}
	return 0;
}
