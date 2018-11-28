#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++)
	{
		int n, m, a;
		cin >> n >> m >> a;
		int x0 = 0, y0 = 0;
		int x1, y1, x2, y2;
		int f = 1;
		cout << "Case #" << cc << ": ";
		for (x1 = 1; x1 <= n && f; x1++)
			for (y1 = 0; y1 <= m && f; y1++)
				for (x2 = 0; x2 <= n && f; x2++)
				{
					int t = y1*x2;
					int A = a + t;
					if (A % x1 == 0 && A/x1 >= 0 && A/x1 <= m)
					{
						cout << x0 << " " << y0 << " " << x1 << " " << y1;
						cout << " " << x2 << " " << A/x1 << endl;
						f = 0;
					}
				}
		if (f)
		for (x2 = 1; x2 <= n && f; x2++)
			for (y2 = 0; y2 <= m && f; y2++)
				for (x1 = 0; x1 <= n && f; x1++)
				{
					int t = x1*y2;
					int A = a - t;
					if (A % x2 == 0 && A/(-x2) >= 0 && A/(-x2) <= m)
					{
						cout << x0 << " " << y0 << " " << x1 << " " << y1;
						cout << " " << x2 << " " << A/x1 << endl;
						f = 0;
					}
				}
		if (f) cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
						
