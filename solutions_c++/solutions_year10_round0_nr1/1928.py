#include <stdio.h>

const int T = 10000;
const int N = 30;
const int K = 100000000;

int check(int, int);

main()
{
	int t, n, k;
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		scanf("%d%d", &n, &k);
		printf("Case #%d: %s\n", i, check(n,k)?"ON":"OFF");
	}
}

int check(int n, int k)
{
	return (k%(1<<n))==((1<<n)-1);
}
