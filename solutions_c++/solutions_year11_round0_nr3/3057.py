#include<stdio.h>

int a[1111], n, T;
int all;
int ret;
int sum;

int main(void)
{
	int l1, l2, l0;
	freopen("C2.in","r",stdin);
	freopen("C2.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d",&n);
		all = 0;
		sum = 0;
		for(l1=0;l1<n;l1++)
		{
			scanf("%d",&a[l1]);
			all ^= a[l1];
			sum += a[l1];
		}
		ret = -1;

		for(l1=0;l1<n;l1++)
		{
			if((all ^ a[l1]) == a[l1])
			{
				if(ret == -1 || a[l1] < ret) ret = a[l1];
			}
		}
		for(l1=0;l1<n;l1++) for(l2=l1+1;l2<n;l2++)
		{
			int temp = a[l1] ^ a[l2];
			if((all ^ temp) == temp)
			{
				if(ret == -1 || a[l1]+a[l2] < ret) ret = a[l1]+a[l2];
			}
		}

		printf("Case #%d: ",l0);
		if(ret == -1) printf("NO\n");
		else printf("%d\n",sum - ret);
	}

	return 0;
}