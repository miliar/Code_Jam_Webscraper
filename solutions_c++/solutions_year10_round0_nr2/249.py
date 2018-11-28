#include <cstdio>
#include <algorithm>
using namespace std;

int T;
int N;
long long data[200];
int main()
{
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%lld", &data[i]);

		long long best = -1;
		for (int i = 0; i < N; i++)
			for (int j = i+1; j < N; j++) if (data[i] != data[j])
			{
				if (best == -1) best = abs(data[i]-data[j]);
				else best = __gcd(best, abs(data[i]-data[j]));
			}
		printf("Case #%d: ", t);
		if (data[0]%best) printf("%lld\n", best-data[0]%best);
		else printf("0\n");
	}
}
