#include <stdio.h>

int main()
{
int ca;

	freopen("C-large.in" , "r" , stdin);
	freopen("C-large.out" , "w" , stdout);
	scanf("%d" , &ca);
	for (int cas = 1; cas <= ca; cas ++)
	{
		printf("Case #%d: " , cas);
		int n;
		int a[1100];
		int tot = 0;
		scanf("%d" , &n);
		int tes = 0;
		int min = 1 << 30;
		for (int i = 0; i < n; i ++)
		{
			scanf("%d" , &a[i]);
			tot += a[i]; tes ^= a[i];
			if (a[i] < min) min = a[i];
		}
		if (tes != 0) {printf("NO\n"); continue;}
		else printf("%d\n" , tot - min);
	}
	return 0;
}