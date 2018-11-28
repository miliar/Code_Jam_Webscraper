#include <cstdio>
int main()
{
	int t, n, k;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", i);
		bool on = k?true:false;
		for (int j = 0; j < n; ++j)
		{
			if ((k & 1) == 0)
				on = false;
			k >>= 1;
		}
		printf(on?"ON\n":"OFF\n");
	}
	return 0;
}