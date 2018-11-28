#include<cstdio>

const int mx=1010;

int n;
int a[mx];

int main()
{
	int t;
	int ca=0;
	int i;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		int res=0;
		int sum=0;
		int min=1000001;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			res^=a[i];
			sum+=a[i];
			if(min>a[i])
				min=a[i];
		}
		printf("Case #%d: ",++ca);
		if(res!=0)
		{
			printf("NO\n");
		}
		else
		{
			printf("%d\n",sum-min);
		}
	}

	return 0;
}
