#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include<fstream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
using namespace std;

string arr[4];

void solve (int t)
{
	int Xwin = 0;
	int Owin = 0;
	bool comp = true;

	for (int i=0; i<4; i++)
	{
		if (arr[i][0] == '.')
		{
			comp  = false;
			continue;
		}
		else if (arr[i][0] == 'O')
		{
			bool win = 1;
			for (int j=1; j<4; j++)
			{
				if (arr[i][j] == 'X' || arr[i][j] == '.')
				{
					win= false;
					break;
				}
			}
			if (win)
				Owin++;
		}
		else if (arr[i][0] == 'X')
		{
			bool win = 1;
			for (int j=1; j<4; j++)
			{
				if (arr[i][j] == 'O' || arr[i][j] == '.')
				{
					win= false;
					break;
				}
			}
			if (win)
				Xwin++;
		}
		else if (arr[i][0] == 'T')
		{
			int winx = 1,wino = 1;
			for (int j=1; j<4; j++)
			{
				if (arr[i][j] == 'O')
					wino++;
				else if (arr[i][j] == 'X')
					winx++;
				else
					break;
			}
			if (wino == 4)
				Owin++;
			else if (winx == 4)
				Xwin++;
		}
	}
	//===============================================
	for (int i=0; i<4; i++)
	{
		if (arr[0][i] == '.')
		{
			comp  = false;
			continue;
		}
		else if (arr[0][i] == 'O')
		{
			bool win = 1;
			for (int j=1; j<4; j++)
			{
				if (arr[j][i] == 'X' || arr[j][i] == '.')
				{
					win= false;
					break;
				}
			}
			if (win)
				Owin++;
		}
		else if (arr[0][i] == 'X')
		{
			bool win = 1;
			for (int j=1; j<4; j++)
			{
				if (arr[j][i] == 'O' || arr[j][i] == '.')
				{
					win= false;
					break;
				}
			}
			if (win)
				Xwin++;
		}
		else if (arr[0][i] == 'T')
		{
			int winx = 1,wino = 1;
			for (int j=1; j<4; j++)
			{
				if (arr[j][i] == 'O')
					wino++;
				else if (arr[j][i] == 'X')
					winx++;
				else
					break;
			}
			if (wino == 4)
				Owin++;
			else if (winx == 4)
				Xwin++;
		}
	}
	//==================================
	if (arr[0][0] == '.'){}

	else if (arr[0][0] == 'X')
	{
		bool win = 1;
		for (int i=1; i<4; i++)
		{
			if (arr[i][i] == 'O' || arr[i][i] == '.')
			{
				win= false;
				break;
			}
		}
		if (win)
			Xwin++;
	}
	else if (arr[0][0] == 'O')
	{
		bool win = 1;
		for (int i=1; i<4; i++)
		{
			if (arr[i][i] == 'X' || arr[i][i] == '.')
			{
				win= false;
				break;
			}
		}
		if (win)
			Owin++;
	}
	else if (arr[0][0] == 'T')
	{
		if (arr[1][1] == 'X')
		{
			bool win = 1;
			for (int i=2; i<4; i++)
			{
				if (arr[i][i] == 'O' || arr[i][i] == '.')
				{
					win= false;
					break;
				}
			}
			if (win)
				Xwin++;
		}
		else if (arr[1][1] == 'O')
		{
			bool win = 1;
			for (int i=2; i<4; i++)
			{
				if (arr[i][i] == 'X' || arr[i][i] == '.')
				{
					win= false;
					break;
				}
			}
			if (win)
				Owin++;
		}
	}
	//==================================
	if (arr[0][3] == '.'){}

	else if (arr[0][3] == 'X')
	{
		bool win = 1;
		for (int i=1; i<4; i++)
		{
			if (arr[i][3-i] == 'O' || arr[i][3-i] == '.')
			{
				win= false;
				break;
			}
		}
		if (win)
			Xwin++;
	}
	else if (arr[0][3] == 'O')
	{
		bool win = 1;
		for (int i=1; i<4; i++)
		{
			if (arr[i][3-i] == 'X' || arr[i][3-i] == '.')
			{
				win= false;
				break;
			}
		}
		if (win)
			Owin++;
	}
	else if (arr[0][3] == 'T')
	{
		if (arr[1][2] == 'X')
		{
			bool win = 1;
			for (int i=2; i<4; i++)
			{
				if (arr[i][3-i] == 'O' || arr[i][3-i] == '.')
				{
					win= false;
					break;
				}
			}
			if (win)
				Xwin++;
		}
		else if (arr[1][2] == 'O')
		{
			bool win = 1;
			for (int i=2; i<4; i++)
			{
				if (arr[i][3-i] == 'X' || arr[i][3-i] == '.')
				{
					win= false;
					break;
				}
			}
			if (win)
				Owin++;
		}
	}
	//===========================
	printf("Case #%d: ",t);
	if (Xwin == Owin && comp)
		printf("Draw\n");
	else if (Xwin == Owin && !comp)
		printf("Game has not completed\n");
	else if (Xwin > Owin)
		printf("X won\n");
	else
		printf("O won\n");

}

int main ()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int n;
	string s;
	scanf("%d",&n);
	cin.ignore();
	for (int t=1; t<= n; t++)
	{
		for (int j=0; j<5; j++)
		{
			if (j<4)
			{
				getline(cin,arr[j]);
			}
			else
				getline(cin,s);
		}
		solve(t);
	}
	return 0;
}