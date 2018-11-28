#include <iostream>

int main()
{
	//freopen("../input.in","r",stdin);
	//freopen("../output.out","w",stdout);

	int T,N,K,trueNum,init=0,n;
	scanf("%d",&T);
	bool *snappers;

	for(int t=1;t<=T;t++)
	{
		scanf("%d",&N);
		scanf("%d",&K);

		snappers=new bool[N];
		for(n=0;n<N;n++)
			snappers[n]=false;

		for(int k=0;k<K;k++)
		{
			if(snappers[0])
				snappers[0]=false;
			else
				snappers[0]=true;

/*
			printf("%d: ",k);
			for(int i=0;i<N;i++)
				printf("%d ",snappers[i]);
			printf("\n");
*/
			if(k==K-1)break;




			init=0;
			for(int i=0;i<N;i++)if(snappers[i])init++;
			if(init==N)
			{
				for(int i=1;i<N;i++)snappers[i]=false;
				continue;
			}

			
			for(n=1;n<N;n++)
			{
				
				if(snappers[n]==false)
				{
					trueNum=0;
					for(int i=0;i<n;i++)
						if(snappers[i])
							trueNum++;
					if(trueNum==n)
					{
						snappers[n]=true;
						for(int i=1;i<n;i++)
							snappers[i]=false;
						break;
					}
					else
						break;
				}
			}
			
		}
		trueNum=0;
		for(int i=0;i<N;i++)if(snappers[i])trueNum++;
		if(trueNum==N)
			printf("Case #%d: ON\n",t);
		else
			printf("Case #%d: OFF\n",t);
		delete [] snappers;
	}

	return 0;
}
