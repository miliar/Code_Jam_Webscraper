#include <cstdio>
#include <cstring>
const int MAXM = 600;
const int BASE = 10000;
char sample[] = "welcome to code jam";

int main()
{
	int a[MAXM][19];
	int n;
	int len;
	int ans;
	char buf[MAXM];
	scanf ("%d", &n);
	gets(buf);
	for (int i = 0; i < n; i ++)
	{
		printf ("Case #%d: ", i + 1);
		gets (buf);
		len = strlen (buf);
		memset (a, 0, sizeof(a));
		for (int k = 0; k < 19; k ++)
			for (int j = 0; j < len; j ++)
				if (buf[j] == sample[k])
				{
					if (k == 0)
					{
						a[j][k] = 1;
						continue;
					}
					for (int l = 0; l < j; l ++)
					{
						a[j][k] += a[l][k - 1];	
						a[j][k] %= BASE;
					}
				}
		ans  = 0;
		for (int j = 0; j < len; j ++)
		{
			ans += a[j][18];
			ans %= BASE;
		}
		if (ans <1000)
			printf ("0");
		if (ans <100)
			printf ("0");
		if (ans <10)
			printf ("0");
		printf ("%d\n", ans);
	}
	return 0;
}
