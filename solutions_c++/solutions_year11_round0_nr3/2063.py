#include<iostream>
#include<algorithm>
using namespace std;
int candy[1000];
int cmp(const void* a,const void* b)
{
	 return *((int*)(a))-*((int*)(b));
}
int main()
{
	int T,N;
	scanf("%d",&T);
	for (int casenum = 1;casenum <= T;++casenum)
	{
		scanf("%d",&N);
		int xor = 0;
		int sum = 0;
		for (int i = 0;i < N;++i)
		{
			scanf("%d",&candy[i]);
			xor ^= candy[i];
			sum += candy[i];
		}
		if (xor != 0)
		{
			printf("Case #%d: NO\n",casenum);
			continue;
		}
		qsort(candy,N,sizeof(int),cmp);
		printf("Case #%d: %d\n",casenum,sum-candy[0]);
	}
	return 0;
}