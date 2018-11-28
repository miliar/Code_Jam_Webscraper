#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char picture[50][50];

bool canFill(int r, int c)
{
	for(int i = 0; i < 2; i++)
		for(int j = 0; j < 2; j++)
			if (picture[r + i][c + j] != '#')
				return false;
	
	picture[r + 0][c + 0] = '/';
	picture[r + 0][c + 1] = '\\';
	picture[r + 1][c + 0] = '\\';
	picture[r + 1][c + 1] = '/';
}

int main()
{
	ifstream fin("large input.txt");
	ofstream fout("output.txt");
	
	int T;	

	fin >> T;
	for(int i = 0; i < T; i++)
	{
		int R, C;
		fin >> R >> C;

		string row;
		for(int r = 0; r < R; r++)
		{
			fin >> row;
			for(int c = 0; c < C; c++)
				picture[r][c] = row.at(c);
		}

		bool possible = true;
		for(int r = 0; r < R - 1; r++)
		{
			for(int c = 0; c < C - 1; c++)
				if (picture[r][c] == '#')
					if (canFill(r, c) == false)
						possible = false;

			if (!possible) break;
		}

		for(int r = 0; r < R; r++)
			if (picture[r][C - 1] == '#')
				possible = false;

		for(int c = 0; c < C; c++)
			if (picture[R - 1][c] == '#')
				possible = false;

		fout << "Case #" << (i + 1) << ":" << endl;
		if (!possible)
			fout << "Impossible" << endl;
		else
			for(int r = 0; r < R; r++)
			{
				for(int c = 0; c < C; c++)
					fout << picture[r][c];

				fout << endl;
			}
	}
	
	fout.close();
	fin.close();
	return 0;
}