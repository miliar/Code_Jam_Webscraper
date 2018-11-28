#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <functional>
#include <cstdlib>
#include <iostream>

using namespace std;

int max (int n, bool s)
{
	int _max = 0;

	if (n <= 1)
		_max = n;
	else if (n >= 29)
		_max = 10;
	else if (!s)
	{
		_max = ceil(n / 3.0);
	}
	else
	{
		int m1 = ceil(n / 3.0);
		int m2 = ceil(n - m1 / 2.0);

		if ((m1+1) - (m2-1) > 2)
			_max = m1;
		else
			_max = m1 + 1;
	}

	return _max;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int cases,
		N,	// googlers
		S,	// surprising
		p;	// max
	scanf_s("%d", &cases);

	int t, count;
	list<int> Ti;

	for (int i = 1; i <= cases; i++)
	{
		scanf_s("%d %d %d", &N, &S, &p);
		Ti.clear();
		count = 0;

		for (int j = 0; j < N; j++)
		{
			scanf_s("%d", &t);
			Ti.push_back(t);

			if (max(t, false) >= p)
				count++;
			else if (S > 0)
			{
				if (max(t, true) >= p)
				{
					count++;
					S--;
				}
			}
		}
		
		cout << "Case #" << i << ": " << count << endl;
	}

	return 0;
}