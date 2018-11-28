#include <cstdio>
#include <iostream>
typedef long long ll;

int main()
{
	int T;
	scanf("%d",&T);
	ll N,K;
	
	for(int c=1;c<=T;c++)
	{
		scanf("%lld%lld",&N,&K);
		bool Power[30]={0};
		Power[0] = true;
		bool State[30] = {0};
		for(ll i=0;i<K;i++)
		{
			State[0] = !State[0]; // Always the case
			bool flag=State[0];
			for(int j=1;j<N;j++)
			{
				if(Power[j]==true)
					State[j] = !State[j];
				if(flag)
				{
					Power[j] = true;
					flag = State[j];
				}
				else
					Power[j]=false;
			}
		}
		if(State[N-1] == true && Power[N-1]==true)
			printf("Case #%d: ON\n",c);
		else
			printf("Case #%d: OFF\n",c);
	}
	
	//getchar();
	//getchar();
	//getchar();
	return 0;
}