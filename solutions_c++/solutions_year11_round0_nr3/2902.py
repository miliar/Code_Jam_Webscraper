#include <cstdio>

using namespace std;

int n,c[1024];

bool possible()
{
	int k=0,result=0;
	while(k<n)
	{
		result^=c[k];
		k++;
	}
	return result==0;
}

int solve()
{
	int sum,min=sum=c[0];
	for(int i=1;i<n;i++)
	{
		if(min>c[i])min=c[i];
		sum+=c[i];
	}
	return sum-min;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%d",&n);
		for(int k=0;k<n;k++)
		{
			scanf("%d",&c[k]);
		}
		printf("Case #%d: ",i+1);
		if(possible())
		{
			printf("%d",solve());
		}else printf("NO");
		printf("\n");
	}
	return 0;
}
