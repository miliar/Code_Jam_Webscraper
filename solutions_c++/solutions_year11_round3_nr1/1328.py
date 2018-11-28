#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <string>
using namespace std;

int main(void)
{

	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int T, tempT;
	fin >> T;
	tempT = T;
	while(T--)
	{
		int R, C, numBlue = 0, i, j;
		char mat[50][50];
		fin >> R >> C;

		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C; ++j)
			{
				fin >> mat[i][j];
				if( mat[i][j] == '#' )
					++numBlue;
			}
		}
		if(numBlue % 4 != 0 )
		{
			fout <<"Case #"<<tempT - T<<":"<<endl<<"Impossible"<<endl;
			continue;
		}
		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C;)
			{
				if(mat[i][j] == '#')
				{
					if(j == C - 1 || mat[i][j+1] != '#' || i == R - 1 || mat[i+1][j] != '#' || mat[i+1][j+1] != '#')
						goto IM;
					mat[i][j] = '/';
					mat[i][j+1] = '\\';
					mat[i+1][j] = '\\';
					mat[i+1][j+1] = '/';
					j += 2;
					continue;
				}
				++j;
			}
		}

		fout <<"Case #"<<tempT - T<<":"<<endl;
		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C; ++j)
			{
				fout << mat[i][j];
			}
			fout << endl;
		}
		continue;
IM:	fout <<"Case #"<<tempT - T<<":"<<endl<<"Impossible"<<endl;
			continue;
	}
}
