#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	ifstream ifstr("c-large.in");
	int T = 0;
	ifstr >> T;
	ofstream ofstr("c-large.out");
	for (int t = 0; t < T; ++t)
	{
		int R = 0, k = 0, N = 0;
		vector<long long> g;
		ifstr >> R >> k >> N;
		for (int i = 0; i < N; ++i)
		{
			long long gi = 0;
			ifstr >> gi;
			g.push_back(gi);
		}

		vector<pair<long long, int> > cs; 
		for (int i = 0; i < N; ++i)
		{
			int j = 0;
			long long curs = 0;
			while (j < N && curs + g[(i + j) % N] <= k)
			{
				curs += g[(i + j) % N];
				++j;
			}
			cs.push_back(make_pair(curs, (i + j) % N));
		}

		long long res = 0;
		int pos = 0;
		for (int i = 0; i < R; ++i)
		{
			res += cs[pos].first;
			pos = cs[pos].second;
		}

		cout << "Case #" <<  t + 1 << " passed.\n";
		ofstr << "Case #" <<  t + 1 << ": " << res << "\n";
	}
	return 0;
}