#include <iostream>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a2.out","w",stdout);
	int cases,n,k;
	int lib[32],i,cas = 1;
	lib[0] = 1;
	for (i = 1; i < 32; i++)
		lib[i] = lib[i-1]*2;
	
	scanf("%d",&cases);
	while(cases --)
	{
		scanf("%d %d",&n,&k);
		printf("Case #%d: ",cas++);
		if (n == 1)
		{
			if (k&1)
				printf("ON\n");
			else printf("OFF\n");
			continue;
		}
		int t = lib[n]-1;
		int left = 0,right = k/t;
		bool find = false;
		while(left <= right)
		{
			int mid = (left+right)>>1;
			if (mid*t+mid-1 == k)
			{
				find = true;
				break;
			}
			else if (mid*t+mid-1 > k)
				right = mid-1;
			else left = mid+1;
		}

		if (find)
			printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}