#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const int MAX_N = 10;
const int MODULUS = 10007;


int f[101][101];

int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		int h, w, n;
		scanf("%d%d%d", &h, &w, &n);
		//bool okay = true;
		for (int i = 1; i <= h; i++)
			for (int j = 1; j <= w; j++)
				f[i][j] = 0;
		f[1][1] = 1;
		for (int i = 0; i < n; i++)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			f[x][y] = -1;
		}
		for (int i = 1; i <= h; i++)
			for (int j = 1; j <= w; j++)
				if (f[i][j] > -1)
				{
					if (i - 1 >= 1 && j - 2 >= 1 && f[i - 1][j - 2] >= 0)
						f[i][j] = (f[i][j] + f[i - 1][j - 2]) % MODULUS;
					if (i - 2 >= 1 && j - 1 >= 1 && f[i - 2][j - 1] >= 0)
						f[i][j] = (f[i][j] + f[i - 2][j - 1]) % MODULUS;
				}
		if (f[h][w] == -1)
			f[h][w] = 0;
		printf("Case #%d: %d\n", testInd + 1, f[h][w] % MODULUS);
	}
	return 0;
}

/*
n = 100;
m = 100;
Do[f[i, j] = 0, {i, 1, n}, {j, 1, m}];
f[1, 1] = 1;
Do[f[i + 1, j + 2] += f[i, j]; f[i + 2, j + 1] += f[i, j], {i, 1, n - 2}, {j, 1, m - 2}]
g[i_, j_] := If[Mod[i + j, 3] == 2, r = (i + j - 2) / 3; c = j - r - 1; Binomial[r, c], 0];

Table[f[i, j],{i, 1, 50}, {j, 1, 50}] == Table[g[i, j],{i, 1, 50}, {j, 1, 50}]

*/

