#include<stdio.h>

int pow2[31];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif

	pow2[0] = 1;
	for(int i = 1; i < 31; i++)
		pow2[i] = 2 * pow2[i - 1];

	int cases, n, k;
	scanf("%d\n", &cases);

	for(int i = 1; i <= cases; i++)
	{
		scanf("%d %d\n", &n, &k);

		printf("Case #%d: ", i);
		if( (k + 1) % pow2[n] == 0) printf("ON\n");
		else printf("OFF\n");
	}
		

	return 0;
}
 