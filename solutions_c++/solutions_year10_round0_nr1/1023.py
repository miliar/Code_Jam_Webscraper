#include <stdio.h>

int main()
{
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int n = 0,k = 0;
		scanf("%d%d",&n,&k);
		int mask = 1<<n;
		printf("Case #%d: ",iCases);
		if(0 == (k+1)%mask) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
