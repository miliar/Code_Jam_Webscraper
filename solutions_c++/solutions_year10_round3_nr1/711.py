#include<stdio.h>
int a[2000],b[2000];
int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	
	int t;
	int sum=0;
     scanf("%d",&t);
	for (int c=0;c<t;c++) 
	{
        sum=0;
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)scanf("%d %d",&a[i],&b[i]);
		for(int i=0;i<n;i++)
		{
			int presum=0;
			for(int j=0;j<n;j++)
			{
				if(j==i)continue;
				if(a[j]>a[i] && b[j]<b[i])++presum;
			}
			sum+=presum;
		}

       	 

		printf("Case #%d: %d\n",c+1,sum);
	}

}