#include <iostream>

using namespace std;

void main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		int n, s, p;
		cin >> n >> s >> p;

		int total = 0;
		for (int j = 0; j < n; j++)
		{
			int x;
			cin >> x;

			int val = (int)(ceil(x / 3.0) + 0.5);
			int res = x % 3;
			if (val >= p) total++;
			else if ((res != 1) && (x != 0) && (x != 1) && (val + 1 == p) && (s > 0))
			{
				total++;
				s--;
			}
		}

		cout << "Case #" << i + 1 << ": " << total << endl;
	}
}
