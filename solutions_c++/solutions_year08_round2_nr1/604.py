#include <iostream>
#include <vector>
#include <utility>

using std::cin;
using std::cout;

using std::pair;

typedef std::vector<std::pair<__int64, __int64> > GridPoints;

int main()
{
	int nCases = 0;

	cin >> nCases;
	for (int icase = 0; icase < nCases; ++icase)
	{
		int n = 0, A = 0, B = 0, C = 0, D = 0, x0 = 0, y0 = 0, M = 0;
		
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

		GridPoints trees;
		trees.reserve(n);
		__int64 X = x0, Y = y0;
		trees.push_back(pair<__int64, __int64>(X, Y));
		for (int i = 1; i < n; ++i)
		{
		  X = ((__int64)A * X + B) % M;
		  Y = ((__int64)C * Y + D) % M;
		  trees.push_back(pair<__int64, __int64>(X, Y));
		}

		int nTriangles = 0;

		for (int p1 = 0; p1 < n-2; ++p1)
		{
			for (int p2 = p1+1; p2 < n-1; ++p2)
			{
				for (int p3 = p2+1; p3 < n; ++p3)
				{
					__int64 xxx = trees[p1].first + trees[p2].first + trees[p3].first;
					__int64 yyy = trees[p1].second + trees[p2].second + trees[p3].second;
					if ((xxx % 3) == 0 && (yyy % 3) == 0)
						++nTriangles;
				}
			}
		}

		cout << "Case #" << (icase+1) << ": " << nTriangles << std::endl;
	}

	return 0;
}