
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <limits>
#include <iomanip>

using namespace std;
ifstream fin("b.in");
ofstream fout("b.out");


unsigned char matrix[4][4];

bool isWin(char c)
{
	unsigned int	i;
	unsigned int	j;
	bool			res = false;
	
	//row
	for (i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if ((matrix[i][j] == c)||(matrix[i][j] == 'T'))
			{
				res = true;
			}
			else
			{
				res = false;
				break;
			}
		}
		if (res)
		{
			return true;
		}
	}
	
	//col
	for (i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if ((matrix[j][i] == c)||(matrix[j][i] == 'T'))
			{
				res = true;
			}
			else
			{
				res = false;
				break;
			}
		}
		if (res)
		{
			return true;
		}
	}

	res = true;
	//diag
	do 
	{
		i=0;
		res &= ((matrix[i][i] == c)||(matrix[i][i] == 'T'));
		i++;
		res &= ((matrix[i][i] == c)||(matrix[i][i] == 'T'));
		i++;
		res &= ((matrix[i][i] == c)||(matrix[i][i] == 'T'));
		i++;
		res &= ((matrix[i][i] == c)||(matrix[i][i] == 'T'));
		
		if (res)
		{
			return true;
		}
	} while (false);
	res = true;
	//diag
	do 
	{
		i=0;
		res &= ((matrix[i][3-i] == c)||(matrix[i][3-i] == 'T'));
		i++;
		res &= ((matrix[i][3-i] == c)||(matrix[i][3-i] == 'T'));
		i++;
		res &= ((matrix[i][3-i] == c)||(matrix[i][3-i] == 'T'));
		i++;
		res &= ((matrix[i][3-i] == c)||(matrix[i][3-i] == 'T'));

		if (res)
		{
			return true;
		}
	} while (false);

	return false;
}

bool isGameOver()
{
	unsigned int i;
	unsigned int j;

	for (i=0;i<4;i++)
	{
		for (j=0;j<4;j++)
		{
			if (matrix[i][j] == '.')
			{
				return false;
			}
		}
	}
	return true;
}

char* solve()
{
	bool res; 
	if (isWin('X'))
	{
		return "X won";
	}
	else if (isWin('O'))
	{
		return "O won";
	}
	else if (isGameOver())
	{
		return "Draw";
	}
	else
	{
		return "Game has not completed";
	}

}



void main2(unsigned int testNum)
{
	unsigned int i;
	unsigned int j;
	unsigned int n;
	char* res;

	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			fin>>matrix[i][j];
		}
	}

	res = solve();
	fout<<"Case #"<<testNum<<": "<<res<<endl;
}

int main(void)
{
	unsigned int numOfTests;
	unsigned int i;

	fin>>numOfTests;
	for(i=0;i<numOfTests;i++)
	{
		main2(i+1);
	}
	return 0;
}
