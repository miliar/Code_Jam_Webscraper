#include <cstdio>
#include <cmath>

int t, n, k;

int main()
{
	scanf("%d", &t);
	for(int i=0; i<t; i++)
	{
		scanf("%d %d", &n, &k);
		if(k%(int)pow(2, n)==(int)pow(2,n)-1)
			printf("Case #%d: ON\n", i+1);
		else
			printf("Case #%d: OFF\n", i+1);
	}
	return 0;
}
