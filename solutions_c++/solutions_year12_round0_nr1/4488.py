#include <cstdio>
#include <cstring>

const int MAXL = 1000;

int r[MAXL];

char s1[MAXL], s2[MAXL];

int main()
{
	int T;
	freopen("a_sample.in", "r", stdin);
	scanf("%d", &T);
	gets(s1);
	memset(r, 222, sizeof(r));
	while (gets(s1)) {
		gets(s2);
		int len = strlen(s1);
		for (int i = 0; i < len; ++i)
			if (r[s1[i]] < 0)
				r[s1[i]] = s2[i];
	}
	r['z'] = 'q';
	r['q'] = 'z';
	freopen("a.in", "r", stdin);
	scanf("%d", &T);
	gets(s1);
	freopen("a.out", "w", stdout);
	for (int t = 1; t <= T; ++t)
	{
		gets(s1);
		printf("Case #%d: ", t);
		int len = strlen(s1);
		for (int i = 0; i < len; ++i)
			printf("%c", r[s1[i]]);
		puts("");
	}
	return 0;
}
