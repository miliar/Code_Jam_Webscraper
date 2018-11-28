#include <fstream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <cmath>
#include <functional>
#include <stack>
#include <set>

using namespace std;

int main()
{
	ifstream ifs("a.in");
	ofstream ofs("a.out");
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		int res = 0;
		int n;
		ifs >> n;
		vector<int> v(n);
		for (int i = 0; i < n; ++i)
		{
			string s;
			ifs >> s;
			int pos = s.rfind('1');
			if (pos == -1) pos = 0;
			v[i] = pos;
		}

		for (int i = 0; i < n; ++i)
		{
			if (v[i] > i)
			{
				int j = i+1;
				for (; j < n; ++j)
					if (v[j] <= i) break;
				while (j != i)
				{
					swap(v[j], v[j-1]);
					--j;
					++res;
				}
			}
		}
		ofs << "Case #" << test + 1 << ": " << res << endl;
	}
	return 0;
}
