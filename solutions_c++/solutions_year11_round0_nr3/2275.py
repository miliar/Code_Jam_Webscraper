#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long ull;

int T, N, xorTot;
ull normTot;
vector<int> scores;

int best = -1;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		best = -1;
		scores.clear();
		cin >> N;
		xorTot = normTot = 0;

		for (int i = 1; i <= N; ++i)
		{
			int val;
			cin >> val;
			scores.push_back(val);
			xorTot = (xorTot ^ val);
			normTot += val;
		}
		
		if (xorTot != 0)
		{
			cout << "Case #" << t <<": " << "NO" << endl;
			continue;
		}

		for (int i = 0; i < scores.size(); ++i)
			if ( (xorTot ^ scores[i]) == scores[i] )
			{
				if (scores[i] > best)
					best = scores[i];
				if (normTot - scores[i] > best)
					best = normTot - scores[i];
			}

		cout << "Case #" << t <<": " << best << endl;
	}

	return 0;
}