#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

typedef long long ll;

int main()
{
	int T;
	ll R,l,N,k;
	vector<ll> g(1000),cyclicity(1000),firstvisit_val(1000),firstvisit_round(1000),next(1000),val(1000);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%lld%lld%lld",&R,&k,&N);
		for(ll i=0;i<N;i++)
			scanf("%lld",&g[i]);

		for(ll i=0;i<N;i++)
		{
			ll temp_val=0;
			ll j;
			for(j=0;j<N;j++)
			{
				if(temp_val+g[(i+j)%N]<=k)
					temp_val+=g[(i+j)%N];
				else
					break;
			}
			val[i] = temp_val;
			next[i] = ((i+j)%N);
			cyclicity[i] = -1;
			firstvisit_val[i] = -1;
			firstvisit_round[i]=-1;
	
		}
	
		int curr_index=0;
		ll total=0;
		ll round;
		for(round=0;round<R;round++)
		{
			if(firstvisit_round[curr_index]==-1)
			{
				firstvisit_val[curr_index] = total;
				firstvisit_round[curr_index] = round;
				total+=val[curr_index];
			
				curr_index = next[curr_index];
				
			}
			else
			{ // time to come out of loop
				
				cyclicity[curr_index] = round-firstvisit_round[curr_index];
				break;
			}
		}
		ll rem_round = R-round+1;
		ll loop = rem_round % cyclicity[curr_index];
		if(rem_round>=cyclicity[curr_index])
		{
			total += loop*(total-firstvisit_val[curr_index]);
			round += loop*cyclicity[curr_index];
		}

		for(;round<R;round++)
		{
			total += val[curr_index];
			curr_index = next[curr_index];
		}
		printf("Case #%d: %lld\n",t,total);
	}
	getchar();
	getchar();
	return 0;
}