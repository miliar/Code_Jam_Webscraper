#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;


int main()
{
	int ca, c;
	int i, j, n, k;

	freopen("c:\\A-large.in", "r", stdin);
	freopen("c:\\A-large.out", "w+", stdout);

	scanf("%d", &ca);
	for(c = 1; c <= ca; c++)
	{
		printf("Case #%d: ", c);
		scanf("%d%d", &n, &k);

		j = 0;
		for(i = 1;i <= n; i++)
		{
			j = 2*j + 1;
		}

	//	printf("%d\n", j);

		if(k >= j) 
		{
			if((k+1)%(j+1) == 0)
				printf("ON\n");
			else printf("OFF\n");
		}
		else printf("OFF\n");
	}
	return 0;
}