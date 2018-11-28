#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <cstdio>
#include <climits>
#include <cmath>
using namespace std;

int main()
{
	int T; cin>>T;
	for(int ds=1;ds<=T;ds++)
	{
		int R,k,N; cin>>R>>k>>N;
		
		vector<int> g(N,0);
		for(int i=0;i<N;i++)
			cin>>g[i];
		
		vector<int> euro(N,0);
		vector<int> next(N,-1);
		for(int i=0;i<N;i++)
		{
			int capacity=k;
			int j;
			for(j=0;j<N;j++)
			{
				if(g[(i+j)%N]<=capacity)
				{
					capacity-=g[(i+j)%N];
					continue;
				}
				break;
			}
			euro[i]=k-capacity;
			next[i]=(i+j)%N;
			fprintf(stderr,"%d %d\n",euro[i],next[i]);
		}
		
		unsigned long long ans=0;
		int current=0;
		for(int i=0;i<R;i++)
		{
			ans+=euro[current];
			current=next[current];
		}
		printf("Case #%d: %d\n",ds,ans);
	}
	return 0;
}
