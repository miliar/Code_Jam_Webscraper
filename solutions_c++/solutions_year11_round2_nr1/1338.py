#include <iostream>
#include <fstream>
#include <string.h>
#include <iomanip>
using namespace std;

int cas, index=1;
ifstream fin("A-large.in");
ofstream fout("A-large.out");

const int SIZE = 101;
int n;
char map[SIZE][SIZE];
int game[SIZE];
int win[SIZE];
double wp[SIZE];
double owp[SIZE];
double oowp[SIZE];
double result[SIZE];

void read()
{
	memset(game, 0 , sizeof(int) * SIZE);
	memset(win, 0, sizeof(int) * SIZE);

	fin >> n;

	for (int i=0; i < n; i ++)
	{
		for (int j=0; j <n; j ++)
		{
			fin >> map[i][j];

			if (map[i][j] == '0')
			{
				game[i] ++;
			}
			else if (map[i][j] == '1')
			{
				game[i]++;
				win[i] ++;
			}//end else if
		}//end for j
	}
}

void cal()
{
	//WP
	for (int i=0; i < n; i ++)
	{
		wp[i] = (double)win[i] / game[i];
	}

	for (int i =0; i < n; i ++)
	{
		int number = 0;
		owp[i] = 0.000000;
		for (int j=0; j < n; j ++)
		{
			if (map[i][j] != '.')
			{
				if (map[i][j] == '1')
				{
					owp[i] += (double)win[j] / (game[j] -1);
				}//
				else
					owp[i] += (double) (win[j]-1) / (game[j] -1);
				number ++;
			}
		}
		if (number != 0)
		{
			owp[i]=owp[i] / number;
		}	
	}

	//oowp
	for (int i=0; i < n; i ++)
	{
		int number = 0;
		oowp[i] = 0.000000;
		for (int j=0; j < n; j ++)
		{
			if (map[i][j] != '.')
			{
				oowp[i] += owp[j];
				number ++;
			}
		}

		if (number != 0)
		{
			oowp[i] /= number;
		}
	}

	for (int i=0; i < n; i ++)
	{
		result[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
	}
}

void print()
{
	fout << "Case #"<<index<<":" << endl;
	for (int i=0; i < n; i ++)
	{
		fout << result[i] << endl;
	}
}

int main()
{
	fin >> cas;

	while (index <= cas)
	{
		read();
		cal();
		print();
		index ++;
	}

	return 0;
}
