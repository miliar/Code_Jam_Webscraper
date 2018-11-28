//============================================================================
// Name        : alien_.cpp
// Author      : Fify
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <memory.h>
using namespace std;

string letter[5001];
char status[16][30];
int l, d, n;
int main()
{
	freopen("/home/fify/Desktop/data.in", "r", stdin);
	freopen("/home/fify/Desktop/data.out", "w", stdout);
	int process(int);
	cin>> l >> d >> n;

	for(int i = 0;i<d;i++)
	{
		cin>> letter[i];
	}

	for(int i = 0;i<n;i++)
	{
		printf("Case #%d: %d\n", i + 1, process(i));
	}
}

int process(int i)
{
	int match(char, int);
	string str;
	cin>> str;

	memset(status, 0, sizeof(status));

	for(int i = 0;i<l;i++)
	{
		for(int j = 0;j<29;j++)
		{
			status[i][j] = ' ';
		}
	}
	int on = 0;
	int step = 0;
	for(int i = 0;i<(int)str.length(); i++)
	{
		if(str[i] == '(')
		{
			on ++;
			continue;
		}

		if(str[i] == ')')
		{
			on --;
			step++;
			continue;
		}

		int count = status[step][29];
		status[step][29] ++;
		status[step][count] = str[i];

		if(on <= 0)
		{
			step ++;
		}
	}

	step = 0;
	int res = 0;
	for(int i = 0;i<d;i++)
	{
		for(int j = 0;j<l;j++)
		{
			if(!match(letter[i][j], j))
			{
				res --;
				break;
			}
		}
		res ++;
	}

	return res;
}

int match(char ch, int step)
{
	for(int i = 0;i<status[step][29];i++)
	{
		if(ch == status[step][i])
		{
			return 1;
		}
	}
	return 0;
}

