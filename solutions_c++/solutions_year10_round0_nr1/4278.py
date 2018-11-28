#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);

	int N,T,t=1,K;
	
	cin>>T;
	while(T--)
	{
		cin>>N>>K;
		bool state[30];
		bool power[30];
		memset(state,0,sizeof(state));
		memset(power,0,sizeof(power));
		power[0] = true;

		for(int i=1;i<=K;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(power[j])
					state[j] = !state[j];
			}
			for(int j=0;j<N-1;j++)
			{
				if(state[j] && power[j])
					power[j+1] = true;
				else
					power[j+1] = false;
			}
		}

		if(power[N-1] && state[N-1])
			printf("Case #%d: ON\n",t++);
		else
			printf("Case #%d: OFF\n",t++);

	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
