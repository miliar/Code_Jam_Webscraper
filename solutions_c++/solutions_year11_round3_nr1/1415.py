#include <iostream>
#include <fstream>
#include <bitset>
#include <cstdlib>
#include <string>

using namespace std;

namespace
{
	static const int RMax = 50;
	static const int CMax = 50;

	typedef bitset<CMax> line_t;

	inline bool check(line_t (&picture)[RMax], int r, int c)
	{
		return picture[r][c + 1] && picture[r + 1][c] && picture[r + 1][c + 1];
	}

	inline void clear(line_t (&picture)[RMax], int r, int c)
	{
		picture[r][c] = picture[r][c + 1] = picture[r + 1][c] = picture[r + 1][c + 1] = false;
	}

	inline void set(char (&pic)[RMax][CMax], int r, int c)
	{
		pic[r][c] = pic[r+1][c+1] = '/';
		pic[r][c+1] = pic[r+1][c] = '\\';
	}

	inline void print(char (&pic)[RMax][CMax], int R, int C, ofstream &fout)
	{
		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
				fout << pic[r][c];
			fout << endl;
		}
	}
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	fin >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int R, C;
		fin >> R >> C;

		static line_t picture[RMax];
		static char picture_backup[RMax][CMax];
		memset(picture, 0, sizeof(picture));
		memset(picture_backup, '.', sizeof(picture_backup));

		for (int nRow = 0; nRow < R; nRow++)
		{
			string text;
			fin >> text;
			
			for (int nCol = 0; nCol < C; nCol++)
				picture[nRow][nCol] = text[nCol] == '#';
		}

		bool possible = true;
		for (int nRow = 0; possible && nRow < R - 1; nRow++)
		{
			for (int nCol = 0; possible && nCol < C - 1; nCol++)
			{
				if (!picture[nRow][nCol])
					continue;

				if (check(picture, nRow, nCol))
				{
					clear(picture, nRow, nCol);
					set(picture_backup, nRow, nCol);
				}
				else
					possible = false;
			}
			possible = picture[nRow].none();
		}
		possible = possible && picture[R - 1].none();

		fout << "Case #" << nTestCase << ":" << endl;
		if (possible)
			print(picture_backup, R, C, fout);
		else
			fout << "Impossible" << endl;
	}

	return 0;
}
