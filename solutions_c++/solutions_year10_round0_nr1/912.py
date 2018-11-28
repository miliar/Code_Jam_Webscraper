#include<cstdio>

int main()
{
	int T, Z, n, k;
	scanf("%d", &T);
	for(Z = 1; Z <= T; Z ++)
	{
		scanf("%d %d", &n, &k);
		if((k+1)%(1<<n) == 0)
		{
			printf("Case #%d: ON\n", Z);
		}
		else {
			printf("Case #%d: OFF\n", Z);
		}
	}
	return 0;
}
