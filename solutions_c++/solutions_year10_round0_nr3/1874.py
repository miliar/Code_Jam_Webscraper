#include <cstdio>

#include <queue>

using std::queue;

int main(void)
{
	int cases;
	
	scanf("%d", &cases);
	for(int t = 1; t <= cases; ++t )
	{
		int k, r, n;
		unsigned long long int res = 0;
		int groups[1024];
		int somas[1024];
		int next[1024];
		
		scanf("%d %d %d", &r, &k, &n);

		for( int i = 0; i < n; ++i ) 
		{
			scanf("%d", &groups[i]);
		}
		
		for( int i = 0; i < n; ++i ) 
		{
			bool done = false;
			int pt = i;
			int total = 0;
			int start = i;
			while(!done)
			{
				if( total + groups[pt] <= k && (total == 0 || pt != start) )
				{
					total += groups[pt];
					pt = (pt+1)%n;
				}
				else
				{
					next[i] = pt;
					somas[i] = total;
					done = true;
				}
			}
		}
		
		
		int total = 0;
		int start = 0;
		int pt = 0;
		for( register int i = 0; i < r; ++i )
		{
			res += somas[pt];
			pt = next[pt];
		}
		printf("Case #%d: %llu\n", t, res);
	}
	return 0;
}
