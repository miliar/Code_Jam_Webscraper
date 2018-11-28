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

struct Pnt
{
	int x;
	int y;

	Pnt() {}
	Pnt(int z1, int z2) : x(z1), y(z2) {}
};

inline bool operator==(const Pnt& p1, const Pnt& p2)
{
	return p1.x == p2.x && p1.y == p2.y;
}

inline bool operator!=(const Pnt& p1, const Pnt& p2)
{
	return !(p1 == p2);
}

inline bool operator<(const Pnt& p1, const Pnt& p2)
{
	if (p1.x != p2.x)
		return p1.x < p2.x;
	else
		return p1.y < p2.y;
}

set<Pnt> p;
vector<set<Pnt>::iterator> d;
vector<Pnt> b;

int main()
{
	int numCase;
	cin >> numCase;

	for (int caseCounter = 1; caseCounter <= numCase; ++caseCounter)
	{
		int R;
		cin >> R;

		p.clear();

		loop (i, R)
		{
			int x1,x2,y1,y2;
			cin>>x1>>y1>>x2>>y2;

			for (int x = x1; x <= x2; ++x)
				for (int y = y1; y <= y2; ++y)
					p.insert(Pnt(x, y));
		}

		int seconds = 0;
		while (!p.empty())
		{
			d.clear();
			b.clear();

			foreach (i, p.cbegin(), p.cend())
			{
				if (p.find(Pnt(i->x - 1, i->y)) == p.end() && p.find(Pnt(i->x, i->y - 1)) == p.end())
					d.push_back(i);

				if (p.find(Pnt(i->x - 1, i->y + 1)) != p.end())
					b.push_back(Pnt(i->x, i->y + 1));
			}

			foreach (i, d.begin(), d.end())
				p.erase(*i);

			p.insert(b.begin(), b.end());

			++seconds;
		}

		cout << "Case #" << caseCounter << ": ";

		cout << seconds;

		cout << endl;
	}

	return 0;
}
