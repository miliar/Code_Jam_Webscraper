//VC++6.0
//author:wangmeng

#include <iostream>
#include <fstream>
using namespace std;

int dir[5][3] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int map[103][103];
char number[10003];
bool ifNum[10003];
int father[10003];
bool ifFa[10003];

int getFather(int x, int y, int h, int w);
int main()
{
	ifstream fin("B-large.in", ios::in);
	ofstream fout("b.out", ios::out);

	int t;
	int h;
	int w;
	int chain;
	char next;
	char mapchar[103][103];
	fin >> t;
	for (int z=0; z<t; z++)
	{
		fin >> h >> w;
		for (int i=0; i<h; i++)
			for (int j=0; j<w; j++)
				fin >> map[i][j];
		// set father[][]
		memset(father, 0, sizeof(father));
		memset(ifFa, 0, sizeof(ifFa));
		for ( i=0; i<h; i++)
			for (int j=0; j<w; j++)
			{
				chain = i*w+j;
				if (ifFa[chain] == false)
				{
					father[chain] = getFather(i, j, h, w);
					ifFa[chain] = true;
				}
			}

		// number
		memset(number, 0, sizeof(number));
		memset(ifNum, 0, sizeof(ifNum));
		next = 'a';
		for ( i=0; i<h; i++)
			for (int j=0; j<w; j++)
			{
				chain = i * w + j;
				if (ifNum[ father[chain] ])
				{
					mapchar[i][j] = number[ father[chain] ];
				}
				else
				{
					number[ father[chain] ] = next;
					mapchar[i][j] = next;
					ifNum[ father[chain] ] = true;
					next++;
				}
			}
		
		// output
		fout << "Case #" << z+1 << ':' <<endl;
		for (i=0; i<h; i++)
		{
			for (int j=0; j<w; j++)
				fout << mapchar[i][j] << ' ';
			fout << endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}
int getFather(int x, int y, int h, int w)
{
	if (ifFa[x*w+y])
		return father[x*w+y];

	int min = map[x][y];
	int mini = -1;
	int xN;
	int yN;
	int chain;
	for (int i=0; i<4; i++)
	{
		xN = x+dir[i][0];
		yN = y+dir[i][1];
		if (( xN> -1 )
			&& (xN < h)
			&& (yN > -1)
			&& (yN < w)
			&& (map[xN][yN] < min)
			)
		{
			min = map[xN][yN];
			mini = i;
		}
	}
	if (mini == -1)
	{
		chain = x*w+y;
		father[chain] = chain;
		ifFa[chain] = true;
		return chain;
	}
	else
	{
		chain = (x+dir[mini][0]) * w + (y+dir[mini][1]);
		if (!ifFa[chain])
		{
			father[chain] = getFather(x+dir[mini][0], (y+dir[mini][1]), h, w);
			ifFa[chain] = true;
			return father[chain];
		}
		else
			return father[chain];
	}
}