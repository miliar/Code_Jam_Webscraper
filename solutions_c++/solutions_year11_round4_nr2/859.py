#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>

#define MAX 1024

using namespace std;
FILE *in; FILE *out;

int n, m, d;
int a[MAX][MAX];

int canDoIt(int size)
{
	for (int srow = 0; srow + size <= n; srow++)
	{
		for (int scol = 0; scol + size <= m; scol++)
		{
			int cx = srow * 2 + size;
			int cy = scol * 2 + size;

			long long x = 0, y = 0;
			for (int i = 0; i < size; i++)
			{
				for (int c = 0; c < size; c++)
				{
					if (i == 0 && (c == 0 || c == size - 1)) continue;
					if (i == size - 1 && (c == 0 || c == size - 1)) continue;

					int diffx = (srow + i) * 2 + 1 - cx;
					int diffy = (scol + c) * 2 + 1 - cy;
					x += (long long)diffx * (long long)a[srow + i][scol + c];
					y += (long long)diffy * (long long)a[srow + i][scol + c];
				}
			}
//			if (size == 5 /*&& srow == 1 && scol == 1*/)
//				cout << x << " " << y << endl;
			if (x == 0 && y == 0) return 1;
		}
	}
	return 0;
}

void doWork(int testNum)
{
	fscanf(in, "%d %d %d", &n, &m, &d);
	char buff[1024];
	for (int i = 0; i < n; i++)
	{
		fscanf(in, "%s", buff);
		for (int c = 0; c < m; c++)
			a[i][c] = buff[c] - '0' + d;
	}

	int ans = -1;
	for (int size = 3; size <= min(n, m); size++)
	{
//		cout << "Trying size " << size << endl;
		if (canDoIt(size))
			ans = size;
	}
	if (ans == -1) fprintf(out, "IMPOSSIBLE\n");
	else fprintf(out, "%d\n", ans);
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("SpinningBlade.in", "rt");
	out = fopen("SpinningBlade.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++)
	{
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		doWork(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	system("pause");
	return 0;
}
