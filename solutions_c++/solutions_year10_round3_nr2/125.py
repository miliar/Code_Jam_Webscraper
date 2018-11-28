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

double calc(double x, double base)
{
	return log(x) / log(base);
}

int main()
{
	int numCase;
	cin >> numCase;

	for (int caseCounter = 1; caseCounter <= numCase; ++caseCounter)
	{
		int64_t l,p,c;
		cin>>l>>p>>c;

		int64_t n = 1;
		int64_t x = l;
		while ((x*=c) < p)
			++n;

		int64_t r = ceil(calc(n, 2));

		cout << "Case #" << caseCounter << ": " << r << endl;
	}

	return 0;
}
