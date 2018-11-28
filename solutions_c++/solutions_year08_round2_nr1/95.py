#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <vector>

using namespace std;

struct Point
{
	long long x, y;
};

int main()
{
	FILE *fin = fopen("A-small-attempt0.in", "rt");
	FILE *fout = fopen("A-small-attempt0.out", "wt");

	int N;
	fscanf(fin, "%d", &N);

	// Cases
	for (int c = 0; c < N; c++)
	{
		long long n, A, B, C, D, x0, y0, M;
		fscanf(fin, "%lld %lld %lld %lld %lld %lld %lld %lld",
			&n, &A, &B, &C, &D, &x0, &y0, &M);

		// Fill the points
		vector<Point> points(n);
		long long X = x0, Y = y0;
		points[0].x = X; points[0].y = Y;
		for (long long i = 1; i <= n - 1; i++)
		{ 
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			points[i].x = X; points[i].y = Y;
		}

		long long numTri = 0;
		for (long long i = 0; i < n - 2; i++)
		{
			Point p1 = points[i];
			for (long long j = i+1; j < n - 1; j++)
			{
				Point p2 = points[j];
				for (long long k = j+1; k < n; k++)
				{
					Point p3 = points[k];
					if (((p1.x + p2.x + p3.x) % 3) == 0)
					{
						if (((p1.y + p2.y + p3.y) % 3) == 0)
						{
							numTri++;
						}
					}
				}
			}
		}

		fprintf(fout, "Case #%d: %lld\n", c+1, numTri);
	}
	//getch();

	fclose(fin);
	fclose(fout);
}