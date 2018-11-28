#include <cstdio>
#include <algorithm>
using namespace std;

int L, N, C;
int a[1001];
long long dist[1000001];
long long T;

long long saves[1000001];

long long solve()
{
	for(int i = 1; i <= N; ++i)
		dist[i] = dist[i - 1] + 2 * a[i % C];
	
	if(L == 0) return dist[N];
	else
	{
		long long max_save = 0;
		for(int star = 0; star < N; ++star)
		{
			long long save;
			if(dist[star] >= T) save = a[(star + 1) % C];
			else if(dist[star + 1] <= T) save = 0;
			else save = (dist[star + 1] - T) / 2;
			
			saves[star] = save;
		}
		
		long long save = 0;
		sort(saves, saves + N);
		
		for(int i = 0; i < L; ++i)
			save += saves[N - i - 1];
		return dist[N] - save;
	}
}

int main()
{
	int Z; scanf("%i", &Z);
	
	for(int z = 1; z <= Z; ++z)
	{
		scanf("%i %lld %i %i", &L, &T, &N, &C);
		for(int i = 1; i <= C; ++i)
			scanf("%i", &a[i]);
		a[0] = a[C];
		printf("Case #%i: %lld\n", z, solve());
	}
	return 0;
}
