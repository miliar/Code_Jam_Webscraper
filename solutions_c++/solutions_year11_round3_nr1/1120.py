#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");

	long long test_cases, rows, r, c, columns, solved;
	char matrix[52][52];

	for (r = 0; r < 52; r++)
		for (c = 0; c < 52; c++)
			matrix[r][c] = 'v'; // Void.

	fin >> test_cases;

    for (int kase = 0; kase < test_cases; kase++)
    {
		fin >> rows >> columns;
		for (r = 1; r <= rows; r++)
			for (c = 1; c <= columns; c++)
				fin >> matrix[r][c];

		solved = 1;
		for (r = 1; r <= rows; r++)
			for (c = 1; c <= columns; c++)
				if (matrix[r][c] == '#' && matrix[r][c+1] == '#' && matrix[r+1][c] == '#' && matrix[r+1][c+1] == '#')
				{
					matrix[r][c] = '/';
					matrix[r][c+1] = '\\';
					matrix[r+1][c] = '\\';
					matrix[r+1][c+1] = '/';
				}
				else if (matrix[r][c] == '#')
				{
					solved = 0;
				}

		if (solved)
		{
			fout << "Case #" << (kase + 1) << ":" << endl;
			for (r = 1; r <= rows; r++)
			{
				for (c = 1; c <= columns; c++)
					fout << matrix[r][c];

				fout << endl;
			}
		}
		else
		{
			fout << "Case #" << (kase + 1) << ":" << endl << "Impossible" << endl;
		}

		for (r = 1; r <= rows; r++)
			for (c = 1; c <= columns; c++)
				matrix[r][c] = 'v';
    }

	return 0;
}