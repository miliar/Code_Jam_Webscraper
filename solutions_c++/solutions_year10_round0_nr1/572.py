#include<cstdio>

int main()
{
	freopen("A-large.in","r", stdin);
	freopen("output.txt","w", stdout);
	int cases;
	scanf("%d" , &cases);
	int n,k;
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d%d", &n, &k);
		int mask = (1 << n) - 1;
		printf("Case #%d: ", ca);
		if ((k & mask) == mask) puts("ON"); else puts("OFF");
	}
	fclose(stdin);
	fclose(stdout);
}
