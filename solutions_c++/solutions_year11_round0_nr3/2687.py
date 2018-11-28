#include<stdio.h>
#include<iostream>
using namespace std;
#include<algorithm>
int a[1000005];
int main()
{
	int t;
    freopen("3.txt","w",stdout);
	scanf("%d",&t);
	{
		int jj=1;
		while(t--)
		{
			int n;
			scanf("%d",&n);
			int i;
			int sum=0;
			for(i=0;i<n;i++)
			{
				scanf("%d",&a[i]);
				sum+=a[i];
			}

			sort(a,a+n);
			int aa=a[0];
			for(i=1;i<n;i++)
				aa=aa^a[i];
			printf("Case #%d: ",jj++);
			if(n==2&&a[0]==a[1])
			{
				printf("%d\n",a[0]);
				continue;
			}
			if(aa!=0)
			{
				printf("NO\n");
				continue;
			}
			int sum1=a[n-1];
			int sum2=a[n-1];
			int l=0;
			for(i=n-2;i>=0;i--)
			{
				sum2+=a[i];
				sum1=sum1^a[i];
				if(sum1==sum-sum2&&sum1!=0 )
				{
					l=sum2;
				}
			}
				printf("%d\n",l);

		}
	}
}