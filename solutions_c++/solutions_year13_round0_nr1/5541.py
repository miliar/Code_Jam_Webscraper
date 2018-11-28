#include <stdio.h>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <memory.h>
#include <cassert>
#include <set>
#include <queue>
#include <deque>
#include <iostream>
#include <math.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a, b) memset(a, b, sizeof(a))

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 4000000000000000000ll;

void prepare()
{
#ifdef LOLWUT
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
#endif
}

int testNumber = 0;

char field[10][10];

bool solve()
{
	printf("Case #%d: ", ++testNumber);

	for (int i = 0; i < 4; i++)
		scanf("%s", field[i]);

	for (int i = 0; i < 4; i++)
	{
		char win = '@';
		for (int j = 0; j < 4; j++)
		{
			if (field[i][j] == 'T') continue;
			if (field[i][j] == '.' || (win != '@' && win != field[i][j])) { win = '@'; break; }
			win = field[i][j];
		}

		if (win != '@')
		{
			printf("%c won\n", win);
			return false;
		}
	}

	for (int i = 0; i < 4; i++)
	{
		char win = '@';
		for (int j = 0; j < 4; j++)
		{
			if (field[j][i] == 'T') continue;
			if (field[j][i] == '.' || (win != '@' && win != field[j][i])) { win = '@'; break; }
			win = field[j][i];
		}

		if (win != '@')
		{
			printf("%c won\n", win);
			return false;
		}
	}

	{
		char win = '@';
		for (int j = 0; j < 4; j++)
		{
			if (field[j][j] == 'T') continue;
			if (field[j][j] == '.' || (win != '@' && win != field[j][j])) { win = '@'; break; }
			win = field[j][j];
		}

		if (win != '@')
		{
			printf("%c won\n", win);
			return false;
		}
	}
	
	{
		char win = '@';
		for (int j = 0; j < 4; j++)
		{
			if (field[3 - j][j] == 'T') continue;
			if (field[3 - j][j] == '.' || (win != '@' && win != field[3 - j][j])) { win = '@'; break; }
			win = field[3 - j][j];
		}

		if (win != '@')
		{
			printf("%c won\n", win);
			return false;
		}
	}

	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (field[i][j] == '.')
			{
				printf("Game has not completed\n");
				return false;
			}

	printf("Draw\n");
	
	return false;
}

int main()
{
	prepare();
	int tn;
	for (scanf("%d", &tn); tn; tn--)
	{
		solve();
	}
	return 0;
}