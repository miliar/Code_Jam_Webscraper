#include <iostream>
#include <fstream>

using namespace std;

int cas, index=1;
ifstream fin("A-large.in");
ofstream fout("A-large.out");

const int SIZE = 52;

int r,c;
char map[SIZE][SIZE];

void read()
{
	memset(map, '\0', sizeof(char) * SIZE * SIZE);
	fin >>  r  >> c;

	for (int i=1; i <= r; i ++)
	{
		for (int j=1; j <=c; j ++)
		{
			fin >> map[i][j];
		}
	}
}

bool square()
{
	for (int i=1; i <= r; i ++)
	{
		for (int j=1; j <= c; j ++)
		{
			if (map[i][j] == '#')
			{
				if (map[i+1][j] == '#' && map[i][j+1] == '#' && map[i+1][j+1] == '#')
				{
					map[i][j] = '/';
					map[i][j+1] = '\\';
					map[i+1][j]= '\\';
					map[i+1][j+1] = '/';
				}
				else
					return false;
			}//end if
		}//end fro j
	}//end for i
	return true;
}

void print( bool flag)
{
	fout << "Case #"<<index<<":"<<endl;
	if(flag)
	{
		for (int i=1; i <=r; i ++)
		{
			for (int j=1; j <=c; j ++)
			{
				fout << map[i][j];
			}
			fout <<endl;
		}
	}
	else
	{
		fout << "Impossible"<<endl;
	}
}

int main()
{
	fin >> cas;

	while (index <= cas)
	{
		read();
		bool flag = square();
		print(flag);
		index ++;
	}

	return 0;
}
