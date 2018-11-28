#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const int MAX = 101;

int board[MAX][MAX];
int result[MAX][MAX];

int n, h, w;

int Fill(int r, int c, int current)
{
	if(result[r][c] >= 0)
	{
	}
	else
	{
		int row = r, col = c;
		int min = board[r][c];
		if(r > 0 && board[r - 1][c] < min)
		{
			min = board[r - 1][c];
			row = r - 1;
			col = c;
		}
		if(c > 0 && board[r][c -1] < min)
		{
			min = board[r][c -1];
			row = r;
			col = c - 1;
		}
		if(c < w - 1 && board[r][c + 1] < min)
		{
			min = board[r][c + 1];
			row = r;
			col = c + 1;
		}
		if(r < h - 1 && board[r + 1][c] < min)
		{
			min = board[r + 1][c];
			row = r + 1;
			col = c;
		}

		if(min != board[r][c])
		{
			result[r][c] = Fill(row, col, current);
		}
		else
		{
			result[r][c] = current;
		}
	}

	return result[r][c];
}

int main()
{
	fin >> n;

	int	a;
	for(int i = 0; i < n; ++i)
	{
		fin >> h >> w;
		for(int j = 0; j < h; ++j)
		{
			for(int k = 0; k < w; ++k)
			{
				fin >> a;
				board[j][k] = a;
				result[j][k] = -1;
			}
		}

		int current = 0;
		for(int j = 0; j < h; ++j)
		{
			for(int k = 0; k < w; ++k)
			{
				if(result[j][k] < 0)
				{
					int r = Fill(j, k, current);
					if(r == current)
					{
						++current;
					}
				}
			}
		}

		fout << "Case #" << i + 1 << ":" << endl;
		for(int j = 0; j < h; ++j)
		{
			for(int k = 0; k < w; ++k)
			{
				if(k > 0)
				{
					fout << " ";
				}
				fout << (char)(result[j][k] + 'a');
			}

			fout << endl;
		}
	}

	return 0;
}