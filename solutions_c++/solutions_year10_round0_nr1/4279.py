#include <cstdio>
#include <cstdlib>

int main()
{
	int T,count=0;
	scanf("%d",&T);
	while(count<T)
	{
		int N,K;
		scanf("%d %d",&N,&K);
		int power=0;
		bool *ifOn=new bool[N];
		for(int i=0;i<N;i++)
		{
			ifOn[i]=0;
		}
		for(int i=0;i<K;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(j<=power)
				{
					ifOn[j]=!ifOn[j];
				}
			}
			power=0;
			while(power<N && ifOn[power])
				power++;
		}
		count++;		
		bool flag=true;
		if(power!=N)
		{
			flag=false;
			goto end;
		}
		for(int i=0;i<N;i++)
		{
			if(!ifOn[i])
			{
				flag=false;
				break;
			}
		}
		end:
		printf("Case #%d: %s\n",count,flag?"ON":"OFF");
	}
	return 0;
}
