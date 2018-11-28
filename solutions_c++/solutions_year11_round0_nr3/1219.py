#include <iostream>
#include <stdio.h>
#include <map>

using namespace std;



long long arr[1000];

int main()
{
	int T;
	scanf("%d",&T);
	
	for(int t=0;t<T;t++)
	{
		int N;
		scanf("%d",&N);
		
		for(int n=0;n<N;n++)
		{
			scanf("%lld",&arr[n]);
		}
		
		long long sol=-1;
		
		for(int n=1;n<(1<<N);n++)
		{
			//cout<<"N : "<<n<<endl;
			long long sum1=0;
			long long sum2=0;
			
			long long val1=0;
			long long val2=0;
			
			bool used[2]={false,false};
			
			for(int k=0;k<N;k++)
			{
				if((n>>k)&1)
				{
					used[0]=true;
					sum1=sum1^arr[k];
					val1+=arr[k];
				}
				else
				{
					used[1]=true;
					sum2=sum2^arr[k];
					val2+=arr[k];
				}
			}
			
			if(used[0] && used[1] && sum1==sum2)
			{
				sol = max(sol,max(val1,val2));
			}
		}
		
		
		if(sol<0)
		{
			printf("Case #%d: NO\n",t+1);
		}
		else
		{
			printf("Case #%d: %lld\n",t+1,sol);
		}
	}
}