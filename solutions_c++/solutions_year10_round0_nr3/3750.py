#include<cstdio>
#include<iostream>
using	namespace	std;
int	num[1000];

int	main()
{
	freopen("outdata.txt","w",stdout);
	int	t,r,k,n;
	int	u,i,j,sum,cnt,res;
	scanf("%d",&t);
	for(u=0;u<t;u++)
	{
		scanf("%d%d%d",&r,&k,&n);
		sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&num[i]);
			sum+=num[i];
		}
		printf("Case #%d: ",u+1);
		if(sum<=k)
		{
			printf("%d\n",sum*r);
			continue;
		}
		sum=cnt=res=0;
		for(i=0;;i++)
		{
			j=i%n;
			if(num[j]+sum>k)
			{
				cnt++;
				res+=sum;
				sum=num[j];
			}
			else
				sum+=num[j];
			if(cnt==r)
				break;
		}
		printf("%d\n",res);
	}
	return	0;
}