#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int N;
	cin >> N;

	int caseNum = 1;

	do
	{
		long long result = 0;
		long long n, A, B, C, D, x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

		vector<pair<long long, long long> > points;

		long long X = x0, Y = y0;
		points.push_back(make_pair(X, Y));
		for(long long i = 1; i < n; ++i)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			points.push_back(make_pair(X, Y));
		}

		int sz = (int)points.size();
		for (int i = 0; i < sz; ++i)
		{
			for (int j = i + 1; j < sz; ++j)
			{
				for (int k = j + 1; k < sz; ++k)
				{
					if (((points[i].first + points[j].first + points[k].first) % 3 == 0) &&
						((points[i].second + points[j].second + points[k].second) % 3 == 0))
					{
						++result;
					}
				}
			}
		}

		printf("Case #%d: %ld\n", caseNum++, result);
	} while (caseNum <= N);

	return 0;
}

