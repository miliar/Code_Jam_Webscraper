#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int distances[1000002];

main ()
{
	int t;
	scanf("%d",&t);

	for(int T=1; T<=t;T++)
	{
		int numBoosters,N,C;
		long long ti;
		scanf("%d%lld%d%d",&numBoosters,&ti,&N,&C);
		

		int temp[C];
		int i = 0;
		while (i < C) 
		{
			scanf("%d",&temp[i]);
			i++;
		}

		
		for (int i = 0; i < N; i++)
		{
			distances[i] = temp[i % C];
		}
	 for(int i=0;i<N;i++) cout<<distances[i]<<' ';
	 cout<<endl;
		long long totalTime = 0;
		for (int i = 0; i < N; i++)
		{
			totalTime += distances[i]*2;
			if (totalTime - ti >= 0)
			{
				
				distances[N] = (totalTime-ti)/2;
				
				int rem = N-i;
				totalTime = ti;

				sort(distances+i+1,distances+N+1);
				reverse(distances+i+1,distances+N+1);
				for (int j = 1; j <= min(rem,numBoosters); j++)
				{
					totalTime += distances[i+j];
				}
				
				if (numBoosters < rem)
				{
					for (int j = numBoosters+1; j <= rem; j++) totalTime += distances[i+j]*2;
				}
				i = N;
			}
		}

		printf("Case #%d: %lld\n",T,totalTime);
	}
}
