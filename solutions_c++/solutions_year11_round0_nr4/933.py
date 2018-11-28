#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int cases,N;
	int num[1005],snum[1005];

	scanf("%d",&cases);
	
	for(int i=1;i<=cases;i++)
	{
		scanf("%d",&N);
		for(int j=1;j<=N;j++)
		{
			scanf("%d",&num[j]);
			snum[j]=num[j];
		}
		sort(snum,snum+N+1);
		double ans=N;
		for(int j=1;j<=N;j++)
			ans-=(snum[j]==num[j]);
		printf("Case #%d: %.6lf\n",i,ans);
	}

	return 0;
}
