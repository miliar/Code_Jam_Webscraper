#include<cstdio>
#include<vector>
using namespace std;
#define RANGE 1020
int nums[RANGE];
int N;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,cnt = 1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&N);
		for(int i = 0;i<N;++i)
		{
			scanf("%d",&nums[i]);
		}
		int min = nums[0];
		int val = 0,rval = 0;
		for(int i = 1;i<N;++i)
		{
			if(min > nums[i])
			{
				val = val^min;
				rval += min;
				min = nums[i];
			}
			else
			{
				rval += nums[i];
				val = val^nums[i];
			}
		}
		printf("Case #%d: ",cnt++);
		if(val != min)
			printf("NO\n");
		else
			printf("%d\n",rval);
	}
	return 0;
}