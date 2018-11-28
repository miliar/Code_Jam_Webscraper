#include <cstdio>
#include <climits>
#include <cstdlib>
#include <algorithm>
using namespace std;
int n;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int nT,t=0;
	scanf("%d",&nT);
	while(nT--)
	{
		scanf("%d",&n);
		int xxor=0;
		int sum=0;
		int minV=INT_MAX;
		for(int i=0;i<n;++i)
		{
			int tmp;
			scanf("%d",&tmp);
			xxor ^= tmp;
			sum+=tmp;
			minV=min(minV,tmp);
		}
		if(xxor!=0)
		{
			printf("Case #%d: NO\n",++t);
			continue;
		}
		printf("Case #%d: %d\n",++t,sum-minV);
	}
}


