#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <climits>
#define maxN 1000

using namespace std;

bool B[maxN][maxN];

int
main()
{
	int T, z;
	cin >> T;
	for (z = 1; z <= T; z++)
	{
		int R;
		cin >> R;
		memset(B, 0, sizeof B);
		for (int i = 0; i < R; i++)
		{
			int X1, Y1, X2, Y2;
			cin >> X1 >> Y1 >> X2 >> Y2;
			for (int x = X1; x <= X2; x++)
				for (int y = Y1; y <= Y2; y++)
					B[x][y] = true;
		}
		int ans = 0;
		int ok = false;
		for (int i = 1; i <= 100; i++)
			for (int j = 1; j <= 100; j++)
				ok |= B[i][j];
		while (ok)
		{
			ok = false;
			for (int i = 100; i >= 1; i--)
				for (int j = 100; j >= 1; j--)
				{
					if (B[i][j])
						B[i][j] = B[i - 1][j] | B[i][j - 1];
					else
						B[i][j] = B[i - 1][j] & B[i][j - 1];
					ok |= B[i][j];
				}
			ans++;
		}
		cout << "Case #" << z << ": " << ans << endl;
	}
	return 0;
}

