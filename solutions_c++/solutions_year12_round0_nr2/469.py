#include <iostream>
using namespace std;

int main()
{
	int t, n, s, p, i, j, x, r, y, z;


	cin >> t;
	for (i = 1; i <= t; ++i)
	{
		int ans = 0;

		cin >> n >> s >> p;
		for (j = 0; j < n; ++j)
		{
			cin >> x;
			r = x % 3;
			if (r == 0)
			{
				y = x / 3;	
				if (y >= p)
				{
					++ans;
				}
				else if (y != 0 && y + 1 >= p && s > 0)
				{
					++ans;
					--s;
				}
			}
			else if (r == 1)
			{
				y = x / 3 + 1;
				if (y >= p)
					++ans;
			}
			else
			{
				y = x / 3;
				if (y + 1 >= p)
					++ans;
				else if (y + 2 >= p && s > 0)
				{
					--s;
					++ans;
				}
			}
		}

		cout << "Case #" << i << ": " << ans << endl;
	}

	return 0;
}

