#include <stdio.h>

int main()
{
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int n = 0,x = 0;scanf("%d",&n);
		int sum = 0,xor = 0,minx = 10000000;
		for(int i = 0;i < n;++i)
		{
			scanf("%d",&x);
			xor ^= x;sum += x;
			if(x<minx) minx = x;
		}
		if(xor) printf("Case #%d: NO\n",iCases);
		else printf("Case #%d: %u\n",iCases,sum-minx);
	}
	return 0;
}