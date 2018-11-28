#include<iostream>
#include<algorithm>
using namespace std;
int t[1005];
int ans[1005];

int max(int a,int b)
{
	return a>b?a:b;
}

int sum(int a,int b)
{
	int ans = t[a];
	int i,j;

	for(i= a+1;i<=b;i++)
	{
		int temp = t[i];

			for(j = 0;;j ++)
			{
				int num = 1 << j;
					
					if(num > 1000000)
						break;
					
					if( ( ans & num ) && (temp & num))
					{
						ans -= num;
						temp -= num;

					}
			}
			ans = ( ans | temp );
	}

	return ans;
}
		
int main()
{
	int cas;

	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&cas);
	int n,i;
	int k = 1;

		
	while(cas --)
	{
		scanf("%d",&n);
		
	
		int save = 0;

		for(i=0;i<n;i++)
		{
			scanf("%d",&t[i]);
		
		}

		sort(t,t+n);

		for(i=0;i<n;i++)
		{
			if(i == 0)
				ans[i] = t[i];
			else
				ans[i] = ans[i-1] + t[i];
		}

		int ret = 0;
		
		for(i=0;i<n-1;i++)
		{
			int ans1 = sum(0,i);
			int ans2 = sum(i+1,n-1);
   
			if(ans1 == ans2)
			{
				ret = max(ret , ans[i]);

				ret = max(ret , ans[n-1] - ans[i]);
			}
		/*	ans1 = sum(0,i-1);
			ans2 = sum(i,n-1);

			if(ans1 == ans2)
			{
				ret = max(ret,ans[i-1]);
				ret = max(ret,ans[n-1] - ans[i - 1]);
			}
*/

		}
		printf("Case #%d: ",k++);

		if(ret == 0)

			printf("NO\n");
		else

			printf("%d\n",ret);

	}

	return 0;
}
		
/*
10
12
6809 5391 4516 1404 5477 6947 905 7026 5792 4757 4515 6245
*/