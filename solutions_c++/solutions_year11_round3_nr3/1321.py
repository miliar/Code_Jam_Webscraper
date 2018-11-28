#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;
int nbTests;
long long L, H;
int N;
long long freq[10000];

int main()
{
	scanf("%d", &nbTests);
	
	for(int t = 1; t <= nbTests; t++)
	{
		scanf("%d%lld%lld\n", &N, &L, &H);
		
		for(int i = 0; i < N; i++)
		{
			scanf("%lld", &freq[i]);
		}
		
		for(long long p = L; p <= H; p++)
		{
			for(int i = 0; i < N; i++)
				if(max(freq[i], p) % min(freq[i], p) != 0)
				{
					goto blabla;
				}
			printf("Case #%d: %lld\n", t, p);
			goto chocolat;
			blabla:;
		}
		printf("Case #%d: NO\n",t);
		chocolat:;
	}
	
	return 0;
}

