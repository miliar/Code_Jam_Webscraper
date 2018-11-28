#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int candy[1002];

int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int nCase;
	scanf("%d",&nCase);
	for (int nc=0;nc<nCase;nc++)
	{
		int n;
		scanf("%d",&n);
		int xor = 0;
		int sum = 0;
		int min = 10000000;
		for (int i=0;i<n;i++)
		{
			int tmp;
			scanf("%d",&tmp);
			sum += tmp;
			if (tmp < min)
				min = tmp;
			xor ^= tmp;
		}
		if (xor)
			printf("Case #%d: NO\n",nc+1);
		else
			printf("Case #%d: %d\n",nc+1,sum-min);
	}
	return	0;
}