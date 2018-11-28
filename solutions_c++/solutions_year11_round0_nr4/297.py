#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int n,nums[1001];
int main()
{
	int tt;
	scanf("%d",&tt);
	for (int tc=1;tc<=tt;tc++)
	{
		int n;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
			scanf("%d",&nums[i]);
		int sum=0;
		for (int i=1;i<=n;i++)
			if (i!=nums[i]) sum++;
		printf("Case #%d: %.6lf\n",tc,(double)sum);
	}
	return 0;
}
