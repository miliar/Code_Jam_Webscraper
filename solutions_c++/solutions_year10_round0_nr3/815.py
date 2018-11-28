#include <cstdio>
#include <vector>

using namespace std;

int main()
{
	int tt;
	scanf("%d", &tt);

	for (int tp = 1; tp <= tt; ++tp)
	{
		int r, k, n;
		scanf("%d%d%d", &r, &k, &n);
		vector <long long> g(n);
		for (int i = 0; i < n; ++i) scanf("%lld", &g[i]);
		vector <int> skok(n);
		vector <long long> utrzak(n);

		for (int i = 0; i < n; ++i)
		{
			utrzak[i] = 0;
			for (skok[i] = 0; skok[i] <= n && utrzak[i] <= k; ++skok[i])
			{
				utrzak[i] += g[(i+skok[i])%n];
			}
			--skok[i];
			utrzak[i] -= g[(i+skok[i])%n];
		}

		int gdjeSam = 0;
		long long zarada = 0;
		for (int i = 0; i < r; ++i)
		{
			zarada += utrzak[gdjeSam];
			gdjeSam = (gdjeSam+skok[gdjeSam])%n;
		}
		
		printf("Case #%d: %lld\n", tp, zarada);
	}

	return 0;
}
