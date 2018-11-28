#include <iostream>

using namespace std;

const int MAX_N = 104;

int R;
int a[MAX_N][MAX_N];

int main()
{
	int nTests;
	cin >> nTests;
	for (int run = 1; run <= nTests; ++run)
	{
		cin >> R;
		memset(a, 0, sizeof(a));
		for (int i = 0; i < R; ++i)
		{
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int x = x1; x <= x2; ++x)
				for (int y = y1; y <= y2; ++y)
					a[x][y] = 1;
		}
		int c = 0;
		for (int i = 0; i < MAX_N; ++i)
			for (int j = 0; j < MAX_N; ++j)
				c += a[i][j];
		int t = 0;
		while (c != 0)
		{
			++t;
			for (int i = MAX_N; i > 0; --i)
				for (int j = MAX_N; j > 0; --j)
				{
					if (a[i-1][j] == 0 && a[i][j-1] == 0 && a[i][j] == 1)
					{
						a[i][j] = 0;
						--c;
					}
					if (a[i-1][j] == 1 && a[i][j-1] == 1 && a[i][j] == 0)
					{
						a[i][j] = 1;
						++c;
					}
				}
		}
		
		cout << "Case #" << run << ": " << t << endl;
	}
	
	return 0;
}
