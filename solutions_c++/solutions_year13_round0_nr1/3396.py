#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <set>
#include <map>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-9
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long
#define INF 1000000000

using namespace std;

int T;
char grid[6][6];

bool checkWin(char sym)
{
	//check horizontal
	bool win;
	for(int i = 0; i < 4; i++)
	{
		win = true;
		for(int j = 0; j < 4 && win; j++)
			if(grid[i][j] != sym && grid[i][j] != 'T') win = false;
		if(win) return true;
	}
	
	//check vertical
	for(int i = 0; i < 4; i++)
	{
		win = true;
		for(int j = 0; j < 4 && win; j++)
			if(grid[j][i] != sym && grid[j][i] != 'T') win = false;
		if(win) return true;
	}
	
	//check left-diagonal
	win = true;
	for(int i = 0; i < 4 && win; i++)
		if(grid[i][i] != sym && grid[i][i] != 'T') win = false;
	if(win) return true;
	
	//check right-diagonal
	win = true;
	for(int i = 0; i < 4 && win; i++)
		if(grid[i][3-i] != sym && grid[i][3-i] != 'T') win = false;
	if(win) return true;
	
	return false;
}

bool noEmpty()
{
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(grid[i][j] == '.') return false;
	return true;
}

int main()
{
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
	{
		for(int j = 0; j < 4; j++) scanf("%s", grid[j]);
		
		printf("Case #%d: ", i);
		if(checkWin('O')) printf("O won\n"); else
			if(checkWin('X')) printf("X won\n"); else
				if(noEmpty()) printf("Draw\n"); else
					printf("Game has not completed\n");
	}
	return 0;
}

