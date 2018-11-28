#include <iostream>
#include <algorithm>
#include <vector>
#include <limits>

using namespace std;

typedef long long lint;
const lint inf = numeric_limits<lint>::max() / 2;

bool cell[128];

typedef vector<int> vint;

int main()
{
	int tc;
	cin >> tc;
	for (int casecnt = 1; casecnt <= tc; ++casecnt)
	{
		int p, q;
		cin >> p >> q;

		vint release;
		while (q--)
		{
			int r;
			cin >> r;
			--r;

			release.push_back(r);
		}

		sort(release.begin(), release.end());

		lint minBribe = inf;
		do
		{
			lint bribe = 0;
			for (int c = 0; c < p; ++c)
				cell[c] = true;

			for (int c = 0; c < release.size(); ++c)
			{
				int r = release[c];

				cell[r] = false;

				for (int k = r-1; k >= 0 && cell[k]; --k)
					++bribe;
				for (int k = r+1; k < p && cell[k]; ++k)
					++bribe;
			}

			minBribe = min(minBribe, bribe);

		} while (next_permutation(release.begin(), release.end()));

		cout << "Case #" << casecnt << ": " << minBribe << endl;
	}

	return 0;
}
