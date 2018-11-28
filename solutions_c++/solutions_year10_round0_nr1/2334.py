#include <cstdio>
int power(int n)
{
	int p = 1, k = 2;
	while(n > 0)
	{
		if(n&1)
			p *= k;
		k *= k;
		n >>= 1;
	}
	return p;
}
int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: ",i+1);
		if((k+1) % power(n))
			printf("OFF\n");
		else
			printf("ON\n");
	}
	return 0;
}
