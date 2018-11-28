#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <iostream>
#include <sstream>
#include <string>

#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>

#define foreach(iName, iBegin, iEnd) for (auto iName = (iBegin); iName != (iEnd); ++iName)

#define forever for (;;)

#define loop(counterName, times) for (decltype(times) counterName = 0; counterName < (times); ++counterName)

#if defined(_MSC_VER) && _MSC_VER >= 1600
#	define null __nullptr
#else
#	define null 0
#endif

using namespace std;

int main()
{
	int numCase;
	cin >> numCase;

	for (int caseCounter = 1; caseCounter <= numCase; ++caseCounter)
	{
		int p;
		cin >> p;

		vector<int> w;
		w.resize(1 << p);

		loop (i, 1 << p)
		{
			cin >> w[i];
			w[i] = p - w[i];
		}
		loop (i, (1 << p) - 1)
		{
			int dummy;
			cin >> dummy;
		}

		int cost = 0;
		int span = 2;
		int ct = 0;
		int round = p;
		loop (i, (1 << p) - 1)
		{
			int mx = 0;
			loop (i, span)
			{
				if (mx < w[ct + i])
					mx = w[ct + i];
			}

			if (mx >= round)
			{
				loop (i, span)
					--w[ct++];

				++cost;
			}
			else
				ct += span;

			if (ct == 1 << p)
			{
				ct = 0;
				span <<= 1;
				--round;
			}
		}

		cout << "Case #" << caseCounter << ": ";

		cout << cost;

		cout << endl;
	}

	return 0;
}
