#include <stdio.h>

#define MAXS 128
#define MAXQ 1024
#define MAXN 128

char se[MAXS][MAXN];
int query[MAXQ], mic[MAXQ][MAXS];

void readline(char *str) {
	int count = -1;
	while(1) {
		scanf("%c", &str[++count]);
		if(str[count] == '\n')break;
	}
	str[count] = 0;
}
int stringcmp(char *a, char *b) {
	int i;
	for(i = 0; a[i] != 0 && b[i] != 0; i++)
		if(a[i] < b[i])return 1;
		else if(a[i] > b[i])return -1;
	if(a[i] == 0 && b[i] == 0)
		return 0;
	return 1;
}

int main(int argc, char *argv[])
{
	int i, j, k, c;
	int n, s, q;
	char str[MAXN];
	int ans;

	scanf("%d", &n);
	for(c = 1; c <= n; c++) {
		scanf("%d\n", &s);
		for(j = 0; j < s; j++)
			readline(se[j]);
		scanf("%d\n", &q);
		for(j = 0; j < q; j++) {
			readline(str);
			for(k = 0; k < s; k++)
				if(stringcmp(se[k], str) == 0) {
					query[j] = k;
					break;
				}
		}

		for(i = 0; i < s; i++)
			mic[0][i] = 0;
		for(j = 0; j < q; j++) {
			for(i = 0; i < s; i++)
				mic[j + 1][i] = MAXQ;
			for(k = 0; k < s; k++) {
				if(query[j] != k)
					if(mic[j + 1][k] > mic[j][k])
						mic[j + 1][k] = mic[j][k];
				for(i = 0; i < s; i++) {
					if(query[j] != i)
						if(mic[j + 1][i] > mic[j][k] + 1)
							mic[j + 1][i] = mic[j][k] + 1;
				}
			}
		}

		ans = MAXQ;
		for(i = 0; i < s; i++)
			if(ans > mic[q][i])
				ans = mic[q][i];

		printf("Case #%d: %d\n", c, ans);
	}

	return 0;
}
