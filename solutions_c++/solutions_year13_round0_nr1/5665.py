#include <cstdio>
#include <iostream>

using namespace std;

char tab[6][6];
int res[6][6];
int t1, t2;

bool ifx(int x, int y)
{
	int sum = 0;
	for(int i = x ; i <= x + 4  && i >= 1 && i <= 4; i++)
	{	
		if(res[i][y] == 1 || res[i][y] == 3)
			sum++;
	}
	if(sum == 4)
		return true;
	sum = 0;
	for(int i = x ; i >= x - 4  && i >= 1 && i <= 4; i--)
	{
		if(res[i][y] == 1 || res[i][y] == 3)
			sum++;
	}
	if(sum == 4)
		return true;
	sum = 0;
	for(int i = y ; i <= y + 4  && i >= 1 && i <= 4; i++)
	{
		if(res[x][i] == 1 || res[x][i] == 3)
			sum++;
	}
	if(sum == 4)
		return true;
	sum = 0;
	for(int i = y ; i >= y - 4  && i >= 1 && i <= 4; i--)
	{
		if(res[x][i] == 1 || res[x][i] == 3)
			sum++;
	}
	if(sum == 4)
		return true;
	sum = 0;
	if(x == 1 && y == 1)
	{
		int j = 1;
		for(int i = 1; i <= 4; i++)
		{
				if(res[i][j] == 1 || res[i][j] == 3)
					sum++;
				j++;
		}
		if(sum == 4)
			return true;
	}
	sum = 0;
	if(x == 1 && y == 4)
	{
		int j = 4;
		for(int i = 1 ; i <= 4 ; i++)
		{
			if(res[i][j] == 1 || res[i][j] == 3)
				sum++;
			j--;
		}
		if(sum == 4)
			return true;
	}
	return false;
}

bool ifo(int x, int y)
{
	int sum = 0;
	for(int i = x ; i <= x + 4  && i >= 1 && i <= 4; i++)
	{	
		if(res[i][y] == 2 || res[i][y] == 3)
			sum++;
	}
	if(sum == 4)
		return true;
	sum = 0;
	for(int i = x ; i >= x - 4  && i >= 1 && i <= 4; i--)
	{
		if(res[i][y] == 2 || res[i][y] == 3)
			sum++;
	}
	if(sum == 4)
		return true;
	sum = 0;
	for(int i = y ; i <= y + 4  && i >= 1 && i <= 4; i++)
	{
		if(res[x][i] == 2 || res[x][i] == 3)
			sum++;
	}
	if(sum == 4)
		return true;
	sum = 0;
	for(int i = y ; i >= y - 4  && i >= 1 && i <= 4; i--)
	{
		if(res[x][i] == 2 || res[x][i] == 3)
			sum++;
	}
	if(sum == 4)
		return true;
	sum = 0;
	if(x == 1 && y == 1)
	{
		int j = 1;
		for(int i = 1; i <= 4; i++)
		{
				if(res[i][j] == 2 || res[i][j] == 3)
					sum++;
				j++;
		}
		if(sum == 4)
			return true;
	}
	sum = 0;
	if(x == 1 && y == 4)
	{
		int j = 4;
		for(int i = 1 ; i <= 4 ; i++)
		{
			if(res[i][j] == 2 || res[i][j] == 3)
				sum++;
			j--;
		}
		if(sum == 4)
			return true;
	}
	return false;
}
void testcase(int l)
{
	for(int i = 1 ; i <= 4 ; i++)
	{
		for(int j = 1 ; j <= 4 ; j++)
		{
			cin >> tab[i][j];
			if(tab[i][j] == '.')
				res[i][j] = 0;
			if(tab[i][j] == 'X')
				res[i][j] = 1;
			if(tab[i][j] ==  'O')
				res[i][j] = 2;
			if(tab[i][j] == 'T')
				res[i][j] = 3;
		}
	}
	bool odp = 0;
	for(int i = 1 ; i <= 4 ; i++)
	{
		for(int j = 1 ; j <= 4 ; j++)
		{
			if(ifx(i, j) && res[i][j] == 1)
			{	
				printf("Case #%d: X won\n", l);
				odp = true;
				return;
			}
			if(ifo(i, j) && res[i][j] == 2)
			{
				printf("Case #%d: O won\n", l);
				odp = true;
				return;
			}
		}
		if(odp == true)
			break;
	}
	if(odp == false)
	{
		bool odp2 = 0;
		for(int i = 1 ; i <= 4 ; i++)
		{	for(int j = 1 ; j <= 4 ; j++)
			{
				if(res[i][j] == 0)
				{
					odp2 = true;
					printf("Case #%d: Game has not completed\n", l);
					return;
				}
			}
			if(odp2)
				return;
		}
		if(odp2 == false)
			printf("Case #%d: Draw\n", l);
	}
}
int main()
{
	int n;
	cin >> n;
	for(int i = 1 ; i <= n ; i++)
	{
		testcase(i);
	}	
}
