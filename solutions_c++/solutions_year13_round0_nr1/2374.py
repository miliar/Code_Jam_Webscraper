#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> vi;
typedef vector<string> vs;
const int INF = 0x7fffffff;

int Solution()
{
	char mas[4][4];
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			cin >> mas[i][j];

	// X won
	char win = 'X';
	for(int i = 0; i < 4; ++i)
	{
		bool flag = true;
		for(int j = 0; j < 4; ++j)
			if(mas[i][j] != win && mas[i][j] != 'T')
			{
				flag = false;
				break;
			}
		if(flag)
		{
			cout << win << " won";
			return 0;
		}
	}

	for(int i = 0; i < 4; ++i)
	{
		bool flag = true;
		for(int j = 0; j < 4; ++j)
			if(mas[j][i] != win && mas[j][i] != 'T')
			{
				flag = false;
				break;
			}
		if(flag)
		{
			cout << win << " won";
			return 0;
		}
	}

	bool flag = true;
	for(int i = 0; i < 4; ++i)
		if(mas[i][i] != win && mas[i][i] != 'T')
		{
			flag = false;
			break;
		}
	if(flag)
	{
		cout << win << " won";
		return 0;
	}

	flag = true;
	for(int i = 0; i < 4; ++i)
		if(mas[i][3 - i] != win && mas[i][3 - i] != 'T')
		{
			flag = false;
			break;
		}
	if(flag)
	{
		cout << win << " won";
		return 0;
	}

	//-------------------------------------------------------------------

	// O won
	win = 'O';
	for(int i = 0; i < 4; ++i)
	{
		bool flag = true;
		for(int j = 0; j < 4; ++j)
			if(mas[i][j] != win && mas[i][j] != 'T')
			{
				flag = false;
				break;
			}
		if(flag)
		{
			cout << win << " won";
			return 0;
		}
	}

	for(int i = 0; i < 4; ++i)
	{
		bool flag = true;
		for(int j = 0; j < 4; ++j)
			if(mas[j][i] != win && mas[j][i] != 'T')
			{
				flag = false;
				break;
			}
		if(flag)
		{
			cout << win << " won";
			return 0;
		}
	}

	flag = true;
	for(int i = 0; i < 4; ++i)
		if(mas[i][i] != win && mas[i][i] != 'T')
		{
			flag = false;
			break;
		}
	if(flag)
	{
		cout << win << " won";
		return 0;
	}

	flag = true;
	for(int i = 0; i < 4; ++i)
		if(mas[i][3 - i] != win && mas[i][3 - i] != 'T')
		{
			flag = false;
			break;
		}
	if(flag)
	{
		cout << win << " won";
		return 0;
	}

	// ------------------------------------------------------------------------

	//draw

	flag = true;
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			if(mas[i][j] == '.')
			{
				flag = false;
				break;
			}

	if(flag)
		cout << "Draw";
	else
		cout << "Game has not completed";

	return 0;
}

#define debug 1

int main()
{
#ifdef debug
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int n;
	cin >> n;
	getchar();
	for(int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		Solution();
		printf("\n");
	}
	return 0;
}
