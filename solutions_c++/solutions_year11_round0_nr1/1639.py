#include <cstdio>
#include <cstring>

#define MAX(a, b) ( (a) > (b) ? (a) : (b) )
#define ABS(a) ( (a) > 0 ? (a) : -(a) )

const int MAXN = 100 + 1;

int n;
char r[MAXN];
int p[MAXN];
int f[MAXN];

int main() {
	int m;
	scanf("%d", &m);
	int tmp = m;
	while (m > 0) {
		m --;
		memset(f, 0, sizeof(f));
		scanf("%d ", &n);
		for (int i = 1; i < n; i++) scanf("%c %d ", &r[i], &p[i]);
		scanf("%c %d\n", &r[n], &p[n]);	
		p[0] = 1;
		for (int i = 1; i <= n; i++) {
			int j = i - 1;
			while (j > 0 && r[j] != r[i]) j --;
			f[i] = f[i - 1] + 1 + MAX(0, ABS(p[i] - p[j]) - f[i - 1] + f[j]);
		}
		printf("Case #%d: %d\n", tmp - m, f[n]);
	}
	return 0;
		
}

