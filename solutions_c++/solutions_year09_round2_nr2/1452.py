// problem A

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MAX INT_MAX

int data, len, min;
char txt[20], pat[20], res[20];
int flag[20];

void Dfs(int k)
{
	int i;
	if (k == len) {
		pat[k] = '\0';
		int cnt = atoi(pat);
		if (data < cnt && cnt < min) min = cnt;
		return ;
	}
	for (i=0; i<len; i++) {
		if (flag[i] ==0) {
			flag[i] = 1;
			pat[k] = txt[i];
			Dfs(k+1);
			flag[i] = 0;
		}
	}
	return ;
}

int main()
{
	int i, t, cas, mark;

	freopen("B-small.in", "r", stdin);
	freopen("res.out", "w", stdout);

	scanf("%d", &cas);

	for (t=1; t<=cas; t++) {
		scanf("%d", &data);
		itoa(data, txt, 10);
		len = strlen(txt);

		for (i=0, mark=0; i<len-1; i++) if (txt[i] < txt[i+1]) 
		{
			mark = 1;
			break ;
		}

		if (mark==0) {
			txt[len++] = '0';
			txt[len] = '\n';
		}

		min = MAX;
		memset(flag, 0, sizeof(flag));
		Dfs(0);
		printf("Case #%d: %d\n", t, min);
	}

	return 1;
}