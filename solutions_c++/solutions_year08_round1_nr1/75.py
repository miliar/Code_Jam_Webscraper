#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <fstream>
#include <map>
#include <set>
using namespace std;

int main()
{
	int T;

	cin >> T;

	for(int i = 1; i <= T; ++i)
	{
		int N;
		cin >> N;

		long long res = 0;

		vector<long long> v1;
		vector<long long> v2;
		for(int j = 0; j < N; ++j)
		{
			long long v;
			cin >> v;
			v1.push_back(v);
		}

		for(int j = 0; j < N; ++j)
		{
			long long v;
			cin >> v;
			v2.push_back(v);
		}

		sort(v1.begin(), v1.end());
		sort(v2.rbegin(), v2.rend());

		for(int j = 0; j < N; ++j)
		{
			res += v1[j]*v2[j];
		}

		cout << "Case #" << i << ": " << res << endl;

	}


	return 0;
}