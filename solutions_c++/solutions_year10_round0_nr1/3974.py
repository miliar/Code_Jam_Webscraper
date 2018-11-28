#include <stdio.h>
#include <stdlib.h>

using namespace std;

int t, n, k;

int main()
{
	scanf("%d", &t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d%d", &n, &k);
		if((long long)(k + 1) % (1ll << n))
		{
			printf("Case #%d: OFF\n", i);
		}
		else
		{
			printf("Case #%d: ON\n", i);
		}
	}
	return 0;
}
