#include <cstdio>
#include <cstring>


void work()
{
	int T,N,K;
	int cas;
	int i,flag;
	
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++)
	{
		scanf("%d%d",&N,&K);
		
		flag=1;
		for (i=1;i<=N;i++)
		{
			if (K%2!=1)
				flag=0;
			K/=2;
		}
		printf("Case #%d: %s\n",cas,flag%2?"ON":"OFF");
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	work();

	
	return 0;
}
