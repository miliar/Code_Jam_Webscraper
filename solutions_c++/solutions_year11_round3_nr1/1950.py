

#include <fstream>
#include <iostream>
using namespace std;

int T, C, R;
char tiles[50][50];

bool cover();
void print(ofstream & out, bool flag, int test);

void main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("in", ios::in);
	outfile.open("out.txt", ios::out | ios::trunc);
	if(!infile)
		return;
	infile>>T;
	int test = 0;
	while (++test <= T)
	{
		infile>>R>>C;
		int i = 0, j = 0;
		for (i = 0; i < R; ++i)
			for (j = 0; j < C; ++j)
				infile>>tiles[i][j];
		print(outfile, cover(), test);		
	}
	infile.close();
	outfile.close();
}

bool cover()
{
	int i = 0, j = 0;
	for (i = 0; i < R; ++i)
	{
		for (j = 0; j < C; ++j)
		{
			if(tiles[i][j] == '#')
			{
				if (j >= C-1 || i >= R - 1 || tiles[i+1][j] != '#' || tiles[i][j+1] != '#' || tiles[i+1][j+1] != '#')
					return false;
				tiles[i][j] = '/';
				tiles[i+1][j+1] = '/';
				tiles[i+1][j] = '\\';
				tiles[i][j+1] = '\\';
			}
		}
	}

	return true;
}

void print(ofstream & out, bool flag, int test)
{
	out<<"Case #"<<test<<":"<<endl;
	if(!flag)
	{
		out<<"Impossible"<<endl;
		return;
	}
	int i, j;
	for(i = 0; i < R; ++i)
	{
		for(j = 0; j < C; ++j)
		{
			out<<tiles[i][j];
		}
		out<<endl;
	}
	return;
}