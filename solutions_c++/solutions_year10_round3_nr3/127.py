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


#define maxSize 32

int main()
{
	int numCase;
	cin >> numCase;

	uint8_t c[maxSize][maxSize];
	bool m[maxSize][maxSize];

	for (int caseCounter = 1; caseCounter <= numCase; ++caseCounter)
	{
		memset(m, false, maxSize*maxSize);

		int M, N;
		cin >> M >> N;

		loop (i, M)
		{
			string buffer;
			cin >> buffer;

			loop (j, N/4)
			{
				char ch = buffer[j];
				if ('0' <= ch && ch <= '9')
					ch -= '0';
				else
					ch = (ch - 'A') + 10;

				c[i][(j*4)]		= (ch >> 3) & 1;
				c[i][(j*4) + 1]	= (ch >> 2) & 1;
				c[i][(j*4) + 2]	= (ch >> 1) & 1;
				c[i][(j*4) + 3]	= (ch) & 1;

				// flip
				if (i % 2 == 0)
				{
					c[i][(j*4) + 1] = (c[i][(j*4) + 1] == 0) ? 1 : 0;
					c[i][(j*4) + 3] = (c[i][(j*4) + 3] == 0) ? 1 : 0;
				}
				else
				{
					c[i][(j*4)] = (c[i][(j*4)] == 0) ? 1 : 0;
					c[i][(j*4) + 2] = (c[i][(j*4) + 2] == 0) ? 1 : 0;
				}
			}
		}

		map<int, int> counter;

		for (int s = min(M, N); s > 0; --s)
		{
			loop (i, M - s + 1)
			{
				loop (j, N - s + 1)
				{
					if (m[i][j])
						continue;

					bool square = true;
					for (int k = i; k < i + s; ++k)
					{
						for (int l = j; l < j + s; ++l)
						{
							if (m[k][l] || c[k][l] != c[i][j])
							{
								square = false;
								break;
							}
						}
					}

					if (square)
					{
						for (int k = i; k < i + s; ++k)
							memset(m[k] + j, true, s);

						++counter[s];
					}
				}
			}
		}

		cout << "Case #" << caseCounter << ": " << counter.size() << endl;
		foreach (i, counter.rbegin(), counter.rend())
			cout << i->first << " " << i->second << endl;
	}

	return 0;
}
