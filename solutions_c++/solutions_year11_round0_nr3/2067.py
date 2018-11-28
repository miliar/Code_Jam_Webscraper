#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int t;
	scanf("%d",&t);
	for(int j=0;j<t;++j)
	{
		int n,sum = 0,s = 0,min = 1000000;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
		{
			int x;
			scanf("%d",&x);
			s+=x;
			if(min>x)min = x;
			sum^=x;
		}
		if(sum!=0)printf("Case #%d: NO\n",j+1);
		else printf("Case #%d: %d\n",j+1,s-min);
	}
	return 0;
}
