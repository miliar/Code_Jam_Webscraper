#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		long long ans = 0;

		long long R, k, N;
		cin >> R >> k >> N;
		vector<long long> g(N, 0);

		for (size_t i = 0; i < N; ++i)
			cin >> g[i];

		size_t i = 0;
		for (size_t r = 0; r < R; ++r)
		{
			long long total = 0;
			bool ok = false;
			size_t j = i;
			while (total + g[i] <= k)
			{
				total += g[i];
				ok = true;
				++i;
				if (i == N)
					i = 0;
				if (i == j)
					break;
			}

			ans += total;

			if (!ok)
				break;
		}

		cout << "Case #" << t + 1 << ": " << ans << endl;
	}

	return 0;
}
