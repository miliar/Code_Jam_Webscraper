#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	freopen("bin", "r", stdin);
	freopen("bout", "w", stdout);
	int t, n, l, i, j, k;
	char s[30], x[30], ans[30];
	scanf("%d", &t);
	for (l = 1; l <= t; l++)
	{
		scanf("%s", s);
		n = strlen(s);
		for (i = 0; i < n+1; i++)
			ans[i] = 100;
		for (i = 0; i+1 < n; i++)
		{
			k = -1;
			for (j = i+1; j < n; j++)
				if (s[j] > s[i] && (k == -1 || s[k] > s[j]))
					k = j;
			if (k == -1)
				continue;
			strcpy(x, s);
			swap(x[i], x[k]);
			sort(x+i+1, x+n);
			if (strcmp(ans, x) > 0)
				strcpy(ans, x);
		}
		printf("Case #%d: ", l);
		if (ans[0] == 100)
		{
			s[n++] = '0';
			s[n] = 0;
			sort(s, s+n);
			for (i = 0; i < n && s[i] == '0'; i++);
			swap(s[i], s[0]);
			printf("%s\n", s);
		}
		else
			printf("%s\n", ans);
	}
	return 0;
}

