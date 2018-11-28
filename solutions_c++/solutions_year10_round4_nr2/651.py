#include <iostream>
#include <cstring>
#include <cstdio>
#define maxP 20
#define maxM 200000
#define inf 100000000

using std::cin;
using std::cout;
using std::endl;
using std::min;

int M[maxM];
int F[maxM][maxP][maxP];
int cost[maxM][maxP];

int
main()
{
	int T, z;
	cin >> T;
	for (z = 1; z <= T; z++)
	{
		int ans = 0, P;
		cin >> P;
		int PP = 1 << P;
		for (int i = 0; i < PP; i++)
			for (int j = 0; j <= P; j++)
				for (int k = 0; k <= P; k++)
					F[i][j][k] = inf;
		memset(cost, 0, sizeof cost);
		for (int i = 0; i < PP; i++)
		{
			cin >> M[i];
			M[i] = P - M[i];
			F[i][0][M[i]] = 0;
		}
		for (int i = 1; i <= P; i++)
			for (int j = 0; j < PP; j += (1 << i))
				cin >> cost[j][i];
		for (int j = 1; j <= P; j++)
			for (int i = 0; i < PP; i += (1 << j))
				for (int k = 0; k <= P; k++)
				{
					int jj = 1 << (j - 1);
					for (int p = 0; p <= k + 1; p++)
						for (int q = 0; q <= k + 1; q++)
						{
							F[i][j][k] = min(F[i][j][k], F[i][j - 1][p] + F[i + jj][j - 1][q] + cost[i][j]);
							if (p <= k && q <= k)
								F[i][j][k] = min(F[i][j][k], F[i][j - 1][p] + F[i + jj][j - 1][q]);
						}
				}
		cout << "Case #" << z << ": " << F[0][P][0] << endl;
	}
	return 0;
}