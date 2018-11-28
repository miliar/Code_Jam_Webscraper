#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <numeric>

using namespace std;

int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");

	int T, N;

	fin >> N;

	for(T = 1; T <= N; ++T)
	{
		int p, k, l, i;

		fin >> p >> k >> l;
		fout << "Case #" << T << ": ";

		vector <int> rep(l);

		for(i = 0; i < l; ++i)
			fin >> rep[i];

		sort(rep.begin(), rep.end());

		int res = 0, key = 0, press = 1;

		for(i = rep.size() - 1; i >= 0; --i)
		{
			res += press * rep[i];
			++key;
			if (key == k)
			{
				key = 0;
				++press;
			}
		}

		fout << res << endl;
	}

	return 0;
}