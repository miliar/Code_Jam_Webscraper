#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int n, s, p;
		cin >> n >> s >> p;
		int ret = 0;
		for (int i = 0; i < n; ++i)
		{
			int x;
			cin >> x;
			int x1 = x/3;
			int x2 = (x-x1)/2;
			int x3 = x - x1 - x2;
			if (x3 >= p)
			{
				++ret;
				continue;
			}
			// Try to raise x3
			if (s > 0 && x2 > 0)
			{
				--x2;
				++x3;
				if (x3-x2 == 2 && x3-x1 <= 2 && x3 >= p)
				{
					++ret;
					--s;
					continue;
				}
			}
		}
		cout << "Case #" << (t+1) << ": " << ret << endl;
	}
	return 0;
}
