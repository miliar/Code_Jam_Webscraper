#include <stdio.h>
#include <string.h>

char line[1000];
int p[600][600];
char s[100];
int n;

int scan(int cur, int c) {
	if (p[cur][c]) return p[cur][c];
	if (!line[cur] || !s[c]) return 0;
	if (c==18) return p[cur][c]=1;
	if (line[cur]!=s[c] && line[cur]) {
		return scan(cur+1, c);
	}
	int ret=0;
	int cc = cur+1;
	while (line[cur]) {
		if (line[cur]==s[c+1] && line[cur] && s[c+1]) {
			ret+=scan(cur, c+1);
		}
		cur++;
	}
	p[cc][c]=ret;
//	printf("%c %d %d %d\n", line[cc], cc, c, ret);
	return ret;
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d ", &n);
	sprintf(s, "%s", "welcome to code jam");
	for (int i=0; i<n; i++) {
		gets(line);
		memset(p, 0, sizeof(p));
		int ret=0, maxi = strlen(line);
		for (int j=0; j<maxi; j++)
			if (line[j]=='w') ret += scan(j, 0);
		printf("Case #%d: %04d\n", i+1, ret);
	}
	return 0;
}
