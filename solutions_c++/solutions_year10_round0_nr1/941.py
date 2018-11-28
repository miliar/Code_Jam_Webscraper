#include <stdio.h>

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	int n , k;
	int x;

	scanf("%d" , &x);
	for (int t = 1; t <= x; t ++)
	{
		scanf("%d %d" , &n , &k);
		int a = 1;
		for (int i = 0; i < n; i ++) a *= 2;
		a --;
		printf("Case #%d: " , t);
		if ((k & a) == a) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}