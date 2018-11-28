#include <cstdio>
#include <cstring>

const int LMAX = 505;
const int WLEN = 19;
const int OSN = 10000;
const char w[] = "welcome to code jam";

char s[LMAX];
int a[WLEN + 1];
int n;

int Solve()
{
	memset(a, 0, sizeof(a));
	a[WLEN] = 1;

	int len = strlen(s);
	for (int i = len - 1; i >= 0; i--)
	{
		for (int j = 0; w[j]; j++)
			if (s[i] == w[j])
			{
				a[j] += a[j + 1];
				if (a[j] >= OSN)
					a[j] -= OSN;
			}
	}

	return a[0];
}

int main()
{
	freopen("welcome.in", "r", stdin);
	freopen("welcome.out", "w", stdout);

	scanf("%d\n", &n);
	for (int tnum = 1; tnum <= n; tnum++)
	{
		gets(s);
		printf("Case #%d: %04d\n", tnum, Solve());
	}


	return 0;
}
