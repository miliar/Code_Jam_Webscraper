#include<iostream>
using namespace std;
int main()
{

	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	int n;
	int i;
	int t;
	int k = 1;

	while(cas --)
	{
		scanf("%d",&n);

		int ans = 0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&t);

			if(t != i+1)
				ans ++;
		}

		printf("Case #%d: %.6lf\n",k++,ans * 1.0);
	}

	return 0;
}