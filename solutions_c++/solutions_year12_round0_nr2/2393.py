#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int tt = 0;
	
	cin >> tt;
	for (int t = 1; t <= tt; ++t)
	{
		int N = 0, S = 0, p = 0, count = 0;
		cin >> N >> S >> p;
		for (int i = 0; i < N; ++i)
		{
			int val_n = 0;
			cin >> val_n;
			if ((val_n == 0) && (p > 0))
				continue;
			div_t lowest = div(val_n, 3); 
			if (lowest.quot >= p)
			{
				++count;
				continue;
			}
			if (((p - lowest.quot) == 1) && (lowest.rem > 0))
			{
				++count;
				continue;
			}
			if (S > 0)
			{
				if (((p - lowest.quot) == 2) && (lowest.rem == 2))
				{
					--S;
					++count;
					continue;
				}
				if (((p - lowest.quot) == 1) && (lowest.rem == 0))
				{
					--S;
					++count;
					continue;
				}
			}
		}
		cout << "Case #" << t << ": " << count << endl;
	} 
	return 0;
}