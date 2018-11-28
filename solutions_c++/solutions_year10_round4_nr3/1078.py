#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

namespace
{
	bool m1[100][100];
	bool m2[100][100];
	bool (*m)[100][100], (*next_m)[100][100];

	void reset_m(bool (*m)[100][100])
	{
		for (int i = 0; i < 100; i++)
			for (int j = 0; j < 100; j++)
				(*m)[i][j] = false;
	}

	bool life(int x, int y)
	{
		if ((*m)[x][y])
			return (x > 0 && (*m)[x - 1][y]) || (y > 0 && (*m)[x][y - 1]);
		else
			return (x > 0 && (*m)[x - 1][y]) && (y > 0 && (*m)[x][y - 1]);
	}
}

int main()
{
	ifstream inFile("C-small-attempt0.in");
	ofstream outFile("C-small-attempt0.out");

	int C;
	inFile >> C;

	for (int nTestCase = 1; nTestCase <= C; nTestCase++)
	{

		m = &m1;
		next_m = &m2;
		reset_m(m);
		reset_m(next_m);

		int R;
		inFile >> R;

		for (int i = 0; i < R; i++)
		{
			int X1, Y1, X2, Y2;
			inFile >> X1 >> Y1 >> X2 >> Y2;
			for (int x = X1 - 1; x < X2; x++)
				for (int y = Y1 - 1; y < Y2; y++)
					(*m)[x][y] = true;
		}

		int T = 0;
		while (true)
		{
			reset_m(next_m);
			int alive = 0;
			for (int x = 0; x < 100; x++)
				for (int y = 0; y < 100; y++)
				{
					(*next_m)[x][y] = life(x, y);
					if ((*next_m)[x][y])
						alive++;
				}
			swap(m, next_m);
			T++;
			if (alive == 0)
				break;
		}
		outFile << "Case #" << nTestCase << ": " << T << endl;
	}

	return 0;
}
