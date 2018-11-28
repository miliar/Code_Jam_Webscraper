#include <cstdio>
#include <cstring>

const int maxn = 60;

char a[maxn + 1];
int b[256];
int n;

int main()
{
	int testnumber, testcount;
	int num;
	long long v, base, r;
	
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%s", a);
		memset(b, 0, sizeof b);
		num = 0;
		v = 0;
		n = strlen(a);
		for (int i = 0; i < n; i++)
			if (b[a[i]] == 0)
			{
				b[a[i]] = ++num;
			}
		if (num == 1) base = 2;
		else base = num;
		for (int i = 0; i < n; i++)
		{
			if (b[a[i]] == 1) r = 1;
			else
			if (b[a[i]] == 2) r = 0;
			else r = b[a[i]] - 1;
			v = v * base + r;
		}
		printf("Case #%d: %I64d\n", testcount + 1, v);
	}
	
	return 0;
}
