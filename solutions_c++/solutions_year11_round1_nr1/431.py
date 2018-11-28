#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>

#include <iostream>
#include <sstream>
#include <iomanip>

#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
	int tests = 0;
	cin >> tests;
	for (int test = 0; test < tests; ++test)
	{
		long long N, pd, pg;
		cin >> N >> pd >> pg;
		
		bool ok = false;
		long long z = 0;
		for (long long i = 1; i <= N; ++i)
		{
			if (pd * i % 100 == 0)
			{
				ok = true;
				z = i;
				break;
			}
		}

		if (pg == 100 && pd < 100)
			ok = false;

		if (pg == 0 && pd > 0)
			ok = false;

		if (ok)
			cout << "Case #" << test + 1 << ": Possible" << endl;
		else
			cout << "Case #" << test + 1 << ": Broken" << endl;
	}

	return 0;
}
