#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	int T = 0;
	cin >> T;
	for(int t = 0; t != T; ++t)
	{
		long long R, k, N;
		cin >> R >> k >> N;
		vector<int> gs(N);
		vector<pair<int, int> > acc(N);

		for(int n = 0; n != N; ++n)
			cin >> gs[n];

		int euros = 0;
		long long r = 0, i = 0, p = 0;
		bool not_repeated = true;

		while(r != R)
		{
			int line_start = i;
			while(p + gs[i] <= k)
			{
				p += gs[i];
				if(++i == N)
					i = 0;
				if(i == line_start)
					break;
			}
			++r;
			euros += p;
			p = 0;
			if(not_repeated)
			{
				if(acc[i].first)
				{
					int reps = (R - acc[i].first) / (r - acc[i].first) - 1;
					not_repeated = false;

					euros += reps * (euros - acc[i].second);
					if((r += reps * (r - acc[i].first)) == R)
						break;
				} else
				{
					acc[i].first = r;
					acc[i].second = euros;
				}
			}
		}


		cout << "Case #" << (t + 1) << ": " << euros << endl;
	}
	return 0;
}
