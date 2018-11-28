#include <iostream>
#include <fstream>
#include <string.h>

#define x first
#define y second

using namespace std;

ifstream fin("input");
ofstream fout("output");

pair<int, int> r[101][101];

pair<int, int> f(pair<int, int>);

int main()
{
	int T, test, h, w, mat[101][101], i, j, color[101][101];
	fin >> T;

	for(test = 1; test <= T; ++test)
	{
		fin >> h >> w;
		memset(color, 0, sizeof(color));
		for(i = 0; i < h; ++i)
		{
			for(j = 0; j < w; ++j)
			{
				fin >> mat[i][j];
				r[i][j].x = i;
				r[i][j].y = j;
			}
		}
		for(i = 0; i < h; ++i)
		{
			for(j = 0; j < w; ++j)
			{
				if(i > 0 && mat[i - 1][j] < mat[r[i][j].x][r[i][j].y])
				{
					r[i][j].x = i - 1;
					r[i][j].y = j;
				}
				if(j > 0 && mat[i][j - 1] < mat[r[i][j].x][r[i][j].y])
				{
					r[i][j].x = i;
					r[i][j].y = j - 1;
				}
				if(j < w - 1 && mat[i][j + 1] < mat[r[i][j].x][r[i][j].y])
				{
					r[i][j].x = i;
					r[i][j].y = j + 1;
				}
				if(i < h - 1 && mat[i + 1][j] < mat[r[i][j].x][r[i][j].y])
				{
					r[i][j].x = i + 1;
					r[i][j].y = j;
				}
			}
		}

		for(i = 0; i < h; ++i)
		{
			for(j = 0; j < w; ++j)
			{
				r[i][j] = f(make_pair(i, j) );
				//fout << i << " " << j << "->" << r[i][j].x << " " << r[i][j].y << endl;
			}
		}
		int crt = 0;
		fout << "Case #" << test << ":\n";
		for(i = 0; i < h; ++i)
		{
			for(j = 0; j < w; ++j)
			{
				if(color[r[i][j].x][r[i][j].y] == 0)
				{
					color[r[i][j].x][r[i][j].y] = ++crt;
				}
				color[i][j] = color[r[i][j].x][r[i][j].y];
				fout << (char) (color[i][j] + 'a' - 1) << " ";
			}
			fout << "\n";
		}


	}


	return 0;
}

pair<int, int> f(pair<int, int> a)
{
	if(r[a.x][a.y] != r[r[a.x][a.y].x][r[a.x][a.y].y])
	{
		r[a.x][a.y] = f(r[a.x][a.y]);
	}
	return r[a.x][a.y];
}
