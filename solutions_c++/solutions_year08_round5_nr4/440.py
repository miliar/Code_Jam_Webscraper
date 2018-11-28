#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const int maxh = 100;
const int maxw = 100;

int map[maxh][maxw];

int main()
{
	int N;
	cin >> N;
	for (int tc = 0; tc < N; tc++)
	{
		int h, w, r;
		cin >> h >> w >> r;
		for (int i=0; i<h; i++)
			for (int j=0; j<w; j++)
				map[i][j] = 0;
		map[0][0] = 1;
		for (int i=0; i<r; i++)
		{
			int j,k;
			cin >> j >> k;
			map[j-1][k-1] = -1;
		}
		for (int i=0; i<h; i++)
			for (int j=0; j<w; j++)
			{
				if (map[i][j] == -1)
					continue;
				else
				if (i+j == 0)
					map[i][j] = 1;
				else
				{
					if ((i-1>=0) && (j-2>=0))
						if (map[i-1][j-2] != -1)
						{
							map[i][j] += map[i-1][j-2];
							map[i][j] = map[i][j] % 10007;
						}
					if ((i-2>=0) && (j-1>=0))
						if (map[i-2][j-1] != -1)
						{
							map[i][j] += map[i-2][j-1];
							map[i][j] = map[i][j] % 10007;
						}
				}
			}
		cout << "Case #" << tc+1 << ": " << map[h-1][w-1] << endl;
	}
}

