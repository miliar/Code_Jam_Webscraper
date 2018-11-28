#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>

#define MAX 100200

using namespace std;
//FILE *in; FILE *out;
ifstream in; ofstream out;

int n;
long long a[MAX][2];
long long cnt[4][4];

void doWork(int testNum)
{
	int i, c, j;
	long long ans = 0;
	long long A, B, C, D, X, Y, M;
	long long x0, y0, m1, m2, m3;
	
//	fscanf(in, "%d", &n);
//	fscanf(in, "%d %d %d %d", &A, &B, &C, &D);
//	fscanf(in, "%d %d %d", &x0, &y0, &M);

	in >> n;
	in >> A >> B >> C >> D >> x0 >> y0 >> M;
	
	a[0][0] = X = x0; a[0][1] = Y = y0;
	for (i=1; i<n; i++)
	{
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
		a[i][0] = X; a[i][1] = Y;
	}
	
	memset(cnt, 0, sizeof(cnt));
	for (i=0; i<n; i++) cnt[a[i][0]%3][a[i][1]%3]++;
	for (i=0; i<9; i++)
	{
		m1 = cnt[i/3][i%3];
		if (m1 <= 0) continue;

		for (c=0; c<9; c++)
		{
			m2 = cnt[c/3][c%3]; m2 -= (i == c);
			if (m2 <= 0) continue;

			for (j=0; j<9; j++)
			{
				m3 = cnt[j/3][j%3]; m3 -= (int)(i == j) + (int)(c == j);
				if (m3 <= 0) continue;

				if ((i/3 + c/3 + j/3) % 3 != 0) continue;
				if ((i%3 + c%3 + j%3) % 3 != 0) continue;
				
				ans += m1 * m2 * m3;
			}
		}
	}
	
	out << ans / 6 << endl;	
	return;
}

int main(void)
{
	int tests, i;
	
//	in = fopen("cropTriangles.in", "rt");
//	out = fopen("cropTriangles.out", "wt");

	in.open("cropTriangles.in");
	out.open("cropTriangles.out");
	
	in >> tests;
	for (i=0; i<tests; i++)
	{
		out << "Case #" << i+1 << ": ";
		doWork(i+1);
	}
	
	/*
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++)
	{
		fprintf(out, "Case #%d: ", i+1);
		doWork(i + 1);
	}
	*/
	
	return 0;
}
