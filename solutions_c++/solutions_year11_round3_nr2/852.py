// gj.cpp
//

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <utility>

using namespace std;

typedef unsigned char uchar;
typedef unsigned int uint;
typedef unsigned __int64 uint64;

uint64 x[1000001],
	   a[10001];
bool b[1000001];
pair<uint64, uint64> s[10001];

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 i = 0; i < cases; ++i)
	{
		uint64 L, t, N, c;
		cin >> L >> t >> N >> c;
		for (uint64 j = 0; j < c; ++j)
		{
			cin >> a[j];
			s[j] = make_pair(a[j], j);
		}
		sort(s, s + c);

		uint64 r = N / c;
		for (uint64 k = 0; k <= r; ++k)
		{
			uint64 col = k*c;
			for (uint64 kk = 0; kk < c && col + kk < N; ++kk)
				x[col + kk] = a[kk] * 2;
		}

		uint64 l0 = 0,
			   t0 = 0;
		while (t0 < t && l0 < N)
		{
			t0 += x[l0];
			++l0;
		}

		memset(b, 0, sizeof(b));
		uint64 idx = c - 1,
			   l = 0;

		uint64 diff = 0;
		if (l0)
			diff = (t0 - t) / 2;

		while (l < L)
		{
			uint64 beg = s[idx].second;
			while (beg < l0)
				beg += c;

			for (uint64 k = beg; k < N && l < L; k += c)
			{
				b[k] = true;
				++ l;
			}

			if (idx != 0)
				--idx;
			else
				break;

			if (beg >= N)
			{
				if (s[idx].first < diff)
					break;
			}
		}

		if (l < L)
			t0 -= (t0 - t) / 2;

		uint64 res = t0;
		for (uint64 j = l0; j < N; ++j)
		{
			res += b[j] ? x[j] / 2 : x[j];
		}

		cout << "Case #" << i + 1 << ": " << res << endl;

	}

	return 0;
}
