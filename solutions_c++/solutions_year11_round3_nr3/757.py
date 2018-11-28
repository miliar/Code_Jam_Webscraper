#include <cstdio>
#include <algorithm>

using namespace std;

long long T, L, H, N;
long long a[10005];
long long min(long long a, long long b) {return a < b ? a : b;}
long long gcd(long long a, long long b)
{
	if (!b) return a;
	return gcd(b, a % b);
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	long long i, j, t;
	
	scanf("%lld", &T);
	for (t = 1; t <= T; t++)
	{
		long long res = 1;
		printf("Case #%lld: ", t);
		
		scanf("%lld %lld %lld", &N, &L, &H);
		for (i = 1; i <= N; i++) scanf("%lld", &a[i]);
		
		for (i = L; i <= H; i++)
		{
			int ok = 1;
			for (j = 1; j <= N; j++) 
				if (a[j] % i != 0 & i % a[j] != 0) {ok = 0; break;}
			if (ok) 
			{
				printf("%lld\n", i);
				break;
			}
		}
		if (i > H) printf("NO\n");
		
	}
	
	
	return 0;
}