#include <fstream>
#include<string>
#include<iostream>
#include<sstream>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<functional>
#include<numeric>
#include <iomanip>
using namespace std;

typedef pair<int, int> pii;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	fout << std::setprecision(20);

	unsigned int numberOfCases;
	fin >> numberOfCases;

	int X, W, R, T, N, start, end, w_speed;


	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		fin >> X >> W >> R >> T >> N;

		vector<pii> v;
		for (int i=0; i<N; ++i)
		{
			fin >> start >> end >> w_speed;
			v.push_back(make_pair(w_speed, end-start));
			X -= (end-start);
		}
		v.push_back(make_pair(0, X));
		sort(v.begin(), v.end());

		double fastLeft = (double)T;
		double ret = 0.0;
		for (size_t i=0; i<v.size(); ++i)
		{
			double distance = v[i].second;
			double speedIfRunning = v[i].first + R;
			double speedIfWalking = v[i].first + W;
			double timeIfRunning = distance /speedIfRunning;

			if (fastLeft >= timeIfRunning)
			{
				ret += timeIfRunning;
				fastLeft -= timeIfRunning;
			}
			else
			{
				double distanceCovered = fastLeft * speedIfRunning;
				ret += fastLeft;
				fastLeft = 0.0;
				
				double distanceLeft = distance-distanceCovered;
				double timeWalking = distanceLeft / speedIfWalking;
				ret += timeWalking;
			}
		}

		fout << "Case #" << zz << ": " << ret << endl;
	}

	return 0;
}
