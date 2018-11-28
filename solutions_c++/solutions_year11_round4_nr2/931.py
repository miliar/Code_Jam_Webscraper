
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

bool dev(int p[600][600], int si, int sj, int size)
{
	int sumx = 0, sumy = 0;

	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			if ((i == 0 || i == size-1) && (j == 0 || j == size-1)) continue;
			
			int ox, oy;
			//if (size % 2 == 0)
			{
				ox = 2 * i - (size-1);
				oy = 2 * j - (size-1);
			} /*else
			{
				ox = i - (size/2);
				oy = j - (size/2);
			}*/

			sumx += ox * p[i+si][j+sj];
			sumy += oy * p[i+si][j+sj];
		}
	}

	//cout << " " << si << " " << sj << " " << size << ": " << sumx << " " <<sumy<<endl;

	return (sumx == 0 && sumy == 0);
}

int main()
{
	int N;

	cin >> N;

	for (int n = 1; n <= N; n++)
	{
		int R, C, D;
		cin >> R >> C >> D;

		int p[600][600];

		for (int i = 0; i < R; i++)
		{
			string s;
			cin >> s;
			for (int j = 0; j < C; j++) p[i][j] = s.c_str()[j] - '0';
		}

		bool possible = false;
		int max = R;
		if (max > C) max = C;

		while (max >= 3)
		{
			for (int i = 0; i <= R-max; i++)
			{
				for (int j = 0; j <= C-max; j++)
				{
					possible = dev(p, i, j, max);

/*
					if (possible)
					{
						cout << i << " " << j << " " << max << endl;
					}
					*/

					if (possible) break;
				}
				if (possible) break;
			}
			if (possible) break;
			max--;
		}


		if (possible)
		{
			cout << "Case #" << n << ": " << max << endl;
		} else
		{
			cout << "Case #" << n << ": IMPOSSIBLE" << endl;
		}
	}
}

