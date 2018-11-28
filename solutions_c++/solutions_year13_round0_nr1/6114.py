#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


#define ASSERT(X) {if (!(X)) {printf("\n assertion failed at line %d\n",__LINE__);exit(0);}}
/*

typedef struct
{
	int dist;
	int length;
} vine;

vine v[10000];
int d;
int pos;
int n;
typedef pair<int, int> State;
map<State, int> dp;

int travel(int cpos, int cv)
{
	State s = make_pair(cpos,cv);
	if (dp.find(s) != dp.end())
	{
		return 0;
	}
	
	if (cpos == 0)
	{
		if (v[cv].dist + min(v[cv].dist, v[cv].length) >= d)
		{
			return 1;
		}
	}
	
	for (int i = 0; i < n; i++)
	{
		if (v[i].dist > v[cv].dist)
		{
			if (v[i].dist <= (v[cv].dist + (v[cv].dist - cpos)))
			{
				int q = min(v[i].dist - v[cv].dist, v[i].length);
				if (v[i].dist + q >= d)
				{
					return 1;
				}
				else
				{
					if (travel(v[i].dist - q, i) == 1)
					{
						return 1;
					}
				}
			}
		}
	}
	dp[s] = 0;
	return 0;
}
*/

bool check(char a[4])
{
	bool t = false;
	int x = 0;
	int o = 0;

	for (int i = 0; i < 4; i++)
	{
		if (a[i] == 0)
		{
			return false;
		}
		else if (a[i] == 'X')
		{
			x++;
		}
		else if (a[i] == 'O')
		{
			o++;
		}
		else if (a[i] == 'T')
		{
			t = true;
		}
	}

	if ((x == 4) || ((x == 3) && (t)))
	{
		printf("X won\n");
		return true;
	}

	if ((o == 4) || ((o == 3) && (t)))
	{
		printf("O won\n");
		return true;
	}

	return false;
}

char game[4][4];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A2.out","w",stdout);

	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1; case_id<=testcase; case_id++)
	{
		printf("Case #%d: ",case_id);
		
		bool full = true;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				char c;
				char v;
				scanf("%c", &c);
				while (c == '\n')
				{
					scanf("%c", &c);
				}
				if ((c == 'X') || (c == 'O') || (c == 'T'))
				{
					v = c;
				}
				else
				{
					v = 0;
					full = false;
				}
				game[i][j] = v;
			}
		}

		char l[4];
		bool end = false;
		int line = 0;
		int column = 0;

		//Lignes
		while ((!end) && (line < 4))
		{
			l[0] = game[line][0];
			l[1] = game[line][1];
			l[2] = game[line][2];
			l[3] = game[line][3];
			end = check(l);
			line++;
		}

		//colonnes
		while ((!end) && (column < 4))
		{
			l[0] = game[0][column];
			l[1] = game[1][column];
			l[2] = game[2][column];
			l[3] = game[3][column];
			end = check(l);
			column++;
		}

		//diag 1
		if (!end)
		{
			l[0] = game[0][0];
			l[1] = game[1][1];
			l[2] = game[2][2];
			l[3] = game[3][3];
			end = check(l);
		}

		//diag 1
		if (!end)
		{
			l[0] = game[0][3];
			l[1] = game[1][2];
			l[2] = game[2][1];
			l[3] = game[3][0];
			end = check(l);
		}

		if (!end)
		{
			if (full)
			{
				printf("Draw\n");
			}
			else
			{
				printf("Game has not completed\n");
			}
		}


		//printf("NO\n");

		fflush(stdout);
	}
	return 0;
}

