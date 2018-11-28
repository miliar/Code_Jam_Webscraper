#include <iostream>
#include <cstdio>
#include <string>


int main()
{
	int N;
	scanf("%d", & N);
	for (int Case = 1; Case <= N; Case++)
	{
		int n, A, B, C, D, x0, y0, M;
		scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		long long int a[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
		long long int X = x0, Y = y0;
		for (int i = 0; i < n; i++)
		{
			++a[X % 3][Y % 3];
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
		}
		
		long long count = 0;
		for (int i1 = 0; i1 < 3; i1++) for (int j1 = 0; j1 < 3; j1++)
		for (int i2 = 0; i2 < 3; i2++) for (int j2 = 0; j2 < 3; j2++)
		{
			if (i1 == i2 && j1 == j2)
			{
				if (a[i1][j1] > 2)
					count += a[i1][j1] * (a[i1][j1] - 1) * (a[i1][j1] - 2);
			}
			else
			{
				int i3 = (6 - i1 - i2) % 3;
				int j3 = (6 - j1 - j2) % 3;
				count += a[i1][j1] * a[i2][j2] * a[i3][j3];
			}
		}

		count /= 6;
		std::cout << "Case #" << Case << ": " << count << "\n";
	}

	return 0;
}
