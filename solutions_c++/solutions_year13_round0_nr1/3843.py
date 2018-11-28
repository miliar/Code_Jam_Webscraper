#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>

#include <set>
#include <map>
#include <list>
#include <queue>
#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i,a,b) for (int i = (int)a; i <= (int)b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

#define pb push_back
#define mp make_pair

int T;
int win = 0;

bool checkWin(char* check)
{
	char t = 'T';
	REP(i, 4)
	{
		if (check[i] == '.') return false;
		if (check[i] == 'T') 
		{
			check[i] = t;
		}
		else
		{
			if (t != 'T' && check[i] != t) return false;
		}
		t = check[i];
	}
	if (t == 'X') 
	{
		win = 1;
	} 
	else 
	{
		win = 2;
	}
	return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	REP(tc, T)
	{
		bool draw = true;
		win = 0;
		char CC[4][4];
		char C;
		REP(i, 4)
		{
			REP(j, 4)
			{
				cin >> C;
				if (C == '.') draw = false;
				CC[i][j] = C;
				if (j == 3) 
				{
					char check[4] = {CC[i][0], CC[i][1], CC[i][2], CC[i][3]}; //row i
					checkWin(check);
					if (i == 3) 
					{
						char check[4] = {CC[0][0], CC[1][1], CC[2][2], CC[3][3]}; //main diagonal
						checkWin(check);
					}
				}
				if (i == 3) 
				{
					char check[4] = {CC[0][j], CC[1][j], CC[2][j], CC[3][j]}; //column j
					checkWin(check);
					if (j == 0) 
					{
						char check[4] = {CC[3][0], CC[2][1], CC[1][2], CC[0][3]}; //secondary diagonal
						checkWin(check);
					}
				}
			}
		}
		printf("Case #%d: %s\n", tc+1, win == 0 ? (draw ? "Draw" : "Game has not completed") : (win == 1 ? "X won" : "O won"));
	}
}