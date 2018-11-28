
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>

using namespace std;

#define PATH "c:\\jam3\\jam3\\"

int main(void)
{
    ifstream fin(PATH "s.in");
    ofstream fout(PATH "s.out");

    int count;
    fin >> count;

    for (int x = 1; x <= count; ++x)
    {
		int M, V;
		fin >> M >> V;

		int G[10001];  // 9998 /2
		int C[10001];
		int val[10001]; // 10000/2

		int i,j;
		for (i = 0; i < (M -1) / 2; ++i)
			fin >> G[i+1] >> C[i+1];
		for (i = 0; i < (M +1) / 2; ++i)
			fin >> val[(M - 1) / 2 + i +1];



		int ans = 0;

		const int MAXV = 100000;

		int k[10001][2];
		for (i = 1; i <= M; ++i)
			k[i][0] = k[i][1] = MAXV;

		for (i = 8192; i >= 1; i /= 2)
		{
			if (i >= M) continue;

			for (j = i; j < i * 2; ++j)
			{
				if (j > M) continue;

				if (j * 2 +1 > M)
					k[j][val[j]] = 0;
				else
				{
					if (C[j] == 0) // not changable
					{
						if (G[j] == 0) // or
						{
							if (k[j*2][0] >= MAXV || k[j*2+1][0] >= MAXV)
								k[j][0] = MAXV;
							else
								k[j][0] = k[j*2][0] + k[j*2+1][0];
							k[j][1] = min(k[j*2][1], k[j*2+1][1]);
						}
						else // and
						{
							if (k[j*2][1] >= MAXV || k[j*2+1][1] >= MAXV)
								k[j][1] = MAXV;
							else
								k[j][1] = k[j*2][1] + k[j*2+1][1];
							k[j][0] = min(k[j*2][0], k[j*2+1][0]);
						}
					}
					else // changable
					{
						int or[2];
						int and[2];

						if (k[j*2][0] >= MAXV || k[j*2+1][0] >= MAXV)
							or[0] = MAXV;
						else
							or[0] = k[j*2][0] + k[j*2+1][0];
						or[1] = min(k[j*2][1], k[j*2+1][1]);

						if (k[j*2][1] >= MAXV || k[j*2+1][1] >= MAXV)
							and[1] = MAXV;
						else
							and[1] = k[j*2][1] + k[j*2+1][1];
						and[0] = min(k[j*2][0], k[j*2+1][0]);

						if (G[j] == 0) // or
						{
							k[j][0] = min(or[0], and[0] +1);
							k[j][1] = min(or[1], and[1] +1);
						}
						else // and
						{
							k[j][0] = min(or[0] +1, and[0]);
							k[j][1] = min(or[1] +1, and[1]);
						}
					}
				}
				//printf("%d: %d %d\n", j, k[j][0], k[j][1]);
			}


		}
		ans = k[1][V];

		if (ans >= MAXV)
			fout << "Case #" << x << ": IMPOSSIBLE\n";
		else
			fout << "Case #" << x << ": " << ans << "\n";
    }

    return 0;
}

