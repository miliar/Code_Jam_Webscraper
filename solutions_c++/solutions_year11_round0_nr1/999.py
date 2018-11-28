#include <iostream>
#include <algorithm>
#include <vector>

#define maxN (100 + 100)

using namespace std;

int n;
vector <pair <int, int> > o, b;

int solve ()
{
	cin >> n;

	o.resize (0);
	b.resize (0);
	o.push_back (make_pair (0, 0)); 
	b.push_back (make_pair (0, 0)); 
	for (int i = 0; i < n; i++)
	{
		char x; int p;
		cin >> x >> p;
		p--;

		if (x == 'O')
			o.push_back (make_pair (p, i + 1));
		else
			b.push_back (make_pair (p, i + 1));
	}

	o.push_back (make_pair (0, n + 1)); 
	b.push_back (make_pair (0, n + 1)); 

	int x = 0, y = 0;
	int p = 0, q = 0;
	int res = 0;
	while (p + q < n)
		if (o[p + 1].second < b[q + 1].second)
		{
			int nx = o[p + 1].first;
			int ny = b[q + 1].first;
			res += abs (x - nx) + 1;

			if (abs (x - nx) >= abs (y - ny) - 1)
				y = ny;
			else 
				if (ny > y)
					y += abs (x - nx) + 1;
				else
					y -= abs (x - nx) + 1;
			x = nx;

			p++;
		}
		else
		{
			int nx = o[p + 1].first;
			int ny = b[q + 1].first;
			res += abs (y - ny) + 1;

			if (abs (y - ny) >= abs (x - nx) - 1)
				x = nx;
			else 
				if (nx > x)
					x += abs (y - ny) + 1;
				else
					x -= abs (y - ny) + 1;
			y = ny;

			q++;
		}

	return res;
}

int main()
{
	int t, x;
	cin >> t; x = t;
	while (t --> 0)
		cout << "Case #" << x - t << ": " << solve () << endl;

	return 0;
}
