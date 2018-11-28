#include<iostream>
#include<algorithm>

using namespace std;

int a[105];

int main()
{
	freopen("C-small-attempt0CCCC.in","r",stdin);
	freopen("C-small-attempt0CCCC.out","w",stdout);
	int i,j;
	int n,low,high;

	int cas;
	scanf("%d",&cas);

	int k = 1;
	while(cas --)
	{
		scanf("%d%d%d",&n,&low,&high);

		for(i=0;i<n;i++)

			scanf("%d",&a[i]);

		int got = 0;

		printf("Case #%d: ",k++);
		for(i=low;i<=high;i++)
		{
			int flag = 0;

			for(j=0;j<n;j++)
			{
				if(i % a[j] != 0 && a[j] % i != 0)
				{
					flag = 1;
					break;
				}
			}

			if(flag == 0)
			{
				got = 1;
				printf("%d\n",i);
				break;
			}
	
		}

		if(got == 0)
			printf("NO\n");
	}
	return 0;
}
/*
2
4 8 16
1 20 5 2
*/