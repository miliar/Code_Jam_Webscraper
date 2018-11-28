#include <cstdio>
#include <cstring>

int main()
{
	int T, t;
	char s[100];
	int i, j, base;
	int v[200], x[200];
	unsigned long long r;
	
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		scanf("%s", s);
		j = 0;
		for (i = 0; i < 200; ++i)
		{
			v[i] = -1;
		}
		for (i = 0; i < strlen(s); ++i)
		{
			if (v[s[i]] == -1)
			{
				v[s[i]] = j;
				++j;
			}
		}
		for (i = 0; i < 200; ++i)
		{
			if (v[i] == 0)
			{
				x[i] = 1;
			}
			else if (v[i] == 1)
			{
				x[i] = 0;
			}
			else
			{
				x[i] = v[i];
			}
		}
		r = 0;
		base = (j == 1) ? 2 : j;
		j = 1;
		for (i = strlen(s) - 1; i >= 0; --i)
		{
			//printf("%d ", x[s[i]]);
			r += x[s[i]] * j;
			j *= base;
		}
		printf("Case #%d: %lld\n", t, r);
	}
	return 0;
}
