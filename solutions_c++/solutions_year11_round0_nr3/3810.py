#include <stdio.h>

int a[1001],max,sum,u=0,n;
void work(int x,int tmp,int res)
{
	if (tmp==res)
	{
		if (!(res==0 || res==sum))
		{
			if (res>max) max=res;
			if (sum-res>max) max=sum-res;
		}
	}
	if (x==n) return ;
	work(x+1,tmp,res);
	work(x+1,tmp ^ a[x],res-a[x]);
}
void init()
{
	scanf("%d",&n);
	max=0;
	sum=0;
	for (int i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		sum+=a[i];
	}
	work(0,0,sum);
	printf("Case #%d: ",u);
	if (max==0) printf("NO\n");
	else printf("%d\n",max);
}
int main()
{
	int w;
	scanf("%d",&w);
	while (w--)
	{
		u++;
		init();
	}

	return 0;
}
