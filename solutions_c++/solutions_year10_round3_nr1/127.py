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

struct Endpoint
{
	int a;
	int b;
};

int main()
{
	int numCase;
	cin >> numCase;

	for (int caseCounter = 1; caseCounter <= numCase; ++caseCounter)
	{
		int N;
		cin >> N;

		vector<Endpoint> ep;
		uint64_t n = 0;
		loop (i, N)
		{
			Endpoint e;
			cin >> e.a >> e.b;

			loop (j, ep.size())
				if ((ep[j].a < e.a && ep[j].b > e.b) || (ep[j].a > e.a && ep[j].b < e.b))
					++n;

			ep.push_back(e);
		}

		cout << "Case #" << caseCounter << ": " << n << endl;
	}

	return 0;
}
