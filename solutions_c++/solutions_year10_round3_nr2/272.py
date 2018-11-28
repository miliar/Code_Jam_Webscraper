#include<stdio.h>

int main()
{
	int L,P,C;
	int t;
	int ans;
//	freopen("B-small.in","r",stdin);
//	freopen("B-small.out","w",stdout);


	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;++i)
	{
		ans=0;
		scanf("%d%d%d",&L,&P,&C);
		for(int j=0;;++j)
		{
			if(j==32)
				break;
			int t=1<<j;
			_int64 temp=L;
			for(int k=0;k<t;++k)
				temp*=C;
			if(temp>=P)
			{
				ans=j;
				break;
			}
		}
		
		printf("Case #%d: %d\n",i,ans);
	}

	return 0;
}