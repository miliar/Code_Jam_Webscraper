#include <iostream>
using namespace std;
int d[500][500];
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t;
	cin >> t;
	for (int test = 1; test <= t; test++)
	{
		int k;
		cin >> k;
		for (int z = 0; z < k; z++)
		{
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int i = x1; i <= x2; i++)
				for (int j = y1; j <= y2; j++)
					d[i][j] = 1;
		}
		bool f = true;
		int count = -1;
		while (f)
		{
			f = false;
			count++;
			for (int i = 998; i > 0; i--)
				for (int j = (i < 500 ? 0 : i - 500 + 1); j <= (i < 500 ? i : 500 - 1); j++)
				{
					if (d[i - j][j] == 1)
					{
						f = true;
						if (d[i - j - 1][j] == 0 && d[i - j][j - 1] == 0)
							d[i - j][j] = 0;
					}
					if (d[i - j][j] == 0 && d[i - j - 1][j] == 1 && d[i - j][j - 1] == 1)
						d[i - j][j] = 1;
				}
		}
		cout << "Case #" << test << ": " << count << endl;
		
	}
	return 0;
}
