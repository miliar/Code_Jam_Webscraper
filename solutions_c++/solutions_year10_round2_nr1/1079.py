#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

char s[200], t[200];
int main() {
	int T, n, m, i, ai, ct=1;
	FILE *f;
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d ", &n, &m);
		for (i = 0; i < n; i++) {
			scanf("%s ", s);
			sprintf(t, "mkdir -p raiz/%s", s);
			system(t);
		}
		system("find > conta");
		f = fopen("conta", "r"); i = 0;
		while (!feof(f)) { fscanf(f, "%*s "); i++; }
		ai = i;
		for (i = 0; i < m; i++) {
			scanf("%s ", s);
			sprintf(t, "mkdir -p raiz/%s", s);
			system(t);
		}
		system("find > conta");
		f = fopen("conta", "r"); i = 0;
		while (!feof(f)) { fscanf(f, "%*s "); i++; }
		
		system("rm -rf raiz/*");
		printf("Case #%d: %d\n", ct++, i-ai);
	}
	return 0;
}
