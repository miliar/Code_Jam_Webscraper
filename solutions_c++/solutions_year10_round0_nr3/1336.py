/**
 * rolco.cc
 * Google code jam 2010 Qualification Round 
 * C. Theme Park
 */

#include <cstdio>
#include <fstream>
#include <iterator>
#include <numeric>
#include <vector>

using namespace std;

int calc(int R, int k, int N, const vector<int>& group)
{
	vector<int> vals;
	vector<int> startPoints;
	int startPoint = 0;
	startPoints.push_back(startPoint);
	int nonIterSize = 0;
	while(true)
	{
		int val = 0;
		int i=startPoint;
		for (int ctr = 0; (ctr < N) && (val + group[i] <= k) ; i = (i + 1) % group.size(), ++ctr)
			val += group[i];
		vals.push_back(val);
		startPoint = i;
		vector<int>::iterator result = find(startPoints.begin(), startPoints.end(), startPoint);
		if (result == startPoints.end())
			startPoints.push_back(startPoint);
		else 
		{
			nonIterSize = distance(startPoints.begin(), result);
			break;
		}
	}

	// vals.size() must be positive
	if (R <= nonIterSize)
		return (accumulate(vals.begin(), vals.begin() + R, 0));
	else
	{
		int euro = accumulate(vals.begin(), vals.begin() + nonIterSize, 0);
		R -= nonIterSize;
		int sumVal = accumulate(vals.begin() + nonIterSize, vals.end(), 0);
		euro += (R / (vals.size() - nonIterSize)) * sumVal;
		euro += accumulate(vals.begin() + nonIterSize, vals.begin() + (R % (vals.size() - nonIterSize)) + nonIterSize, 0);

		return euro;
	}
}

int main(int argc, char* argv[])
{
	ifstream fin(argv[1]);

	int T;
	fin >> T;

	for (int i=1; i <= T; ++i)
	{
		int R, k, N;
		fin >> R >> k >> N;

		vector<int> group(N);
		for (int j=0; j < N; ++j)
			fin >> group[j];

		int euro = calc(R, k, N, group);

		printf("Case #%d: %d\n", i, euro);
	}
}
