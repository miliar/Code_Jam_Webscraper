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
		int N, M;
		cin >> N >> M;

		set<string> dir;
		loop (i, N)
		{
			string path;
			cin >> path;

			size_t p = 0;
			while ((p = path.find_first_of('/', p + 1)) != path.npos)
			{
				string ss = path.substr(0, p);
				dir.insert(ss);
			}

			dir.insert(path);
		}

		size_t oldSize = dir.size();

		loop (i, M)
		{
			string path;
			cin >> path;

			size_t p = 0;
			while ((p = path.find_first_of('/', p + 1)) != path.npos)
			{
				string ss = path.substr(0, p);
				dir.insert(ss);
			}

			dir.insert(path);
		}

		size_t r = dir.size() - oldSize;

		cout << "Case #" << caseCounter << ": " << r << endl;
	}

	return 0;
}
