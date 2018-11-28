#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);

	for(int t=1; t <= T; ++t)
	{
		int R,K,N,g;
		scanf("%d %d %d", &R, &K, &N);
		
		vector<int> G;
		for(int i=0; i < N; ++i)
		{
			scanf("%d", &g);
			G.push_back(g);
		}

		int idx=0;
		int k=0;
		int ret=0;
		g=0;
		while(R)
		{
			if( k+G[idx] <= K && g < N)
			{
				//printf("%d ",  G[idx]);
				k += G[idx];
				++idx;
				++g;
				idx = idx%N;
			}
			else
			{
				//printf("[%d]\n", R);
				ret += k;
				k=0;
				g=0;
				--R;
			}						
		}
		printf("Case #%d: %d\n",t, ret);

	}

	return 0;
}