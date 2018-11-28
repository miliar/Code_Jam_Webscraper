#include <cstdio>

int testnumber, testcount;

int main()
{
	int x, y;
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d%d", &x, &y);
		int r = y % (1 << x);
		printf("Case #%d: ", testcount + 1);
		if (r == (1 << x) - 1) printf("ON\n");
		else printf("OFF\n");
	}
	
	return 0;
}
