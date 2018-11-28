#include <stdio.h>

#define MAX 60

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test, t, i;
	int n, k;
	int a[MAX], flag;
	scanf("%d", &test);
	for(t=1; t<=test; t++)
	{
		scanf("%d %d", &n, &k);
		for(i=0; i<MAX; i++) a[i] = 0;
		i=1;
		while(k)
		{
			a[i++] = k%2;
			k /= 2;
		}
		flag = 1;
		for(i=1; i<=n; i++)
			if(a[i] == 0)
			{
				flag = 0;
				break;
			}
		if(flag == 1) printf("Case #%d: ON\n", t);
		else printf("Case #%d: OFF\n", t);
	}
	return 0;
}