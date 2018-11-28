/*
 * Q-Tic-Tac-Toe-Tomek.cpp
 *
 *  Created on: Apr 13, 2013
 *  Author: mohamedgamal
 *  Tags:
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <memory.h>
#include <queue>
using namespace std;
#define mp(X,Y) make_pair((X),(Y))
#define SZ(X) (int)((X).size())
typedef pair<int,int> pii;
int const MAX = 0;
int const OO = (1<<28);
char grid[4][5];
bool check(char x)
{
	for(int i=0;i<4;++i)
	{
		int cnt=0;
		for(int j=0;j<4;++j)
			cnt+=(grid[j][i]==x || grid[j][i]=='T');
		if(cnt==4)
			return true;
		cnt=0;
		for(int j=0;j<4;++j)
			cnt+=(grid[i][j]==x || grid[i][j]=='T');
		if(cnt==4)
			return true;
	}
	int dig1=0,dig2=0;
	for(int i=0;i<4;++i)
	{
		dig1+=(grid[i][i]==x || grid[i][i]=='T');
		dig2+=(grid[i][4-i-1]==x || grid[i][4-i-1]=='T');
	}
	return dig1==4 || dig2==4;
}
bool emptyCells()
{
	for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
			if(grid[i][j]=='.')
				return true;
	return false;
}
int main()
{
	freopen("in.in","rt",stdin);
	freopen("out.out","wt",stdout);
	int t,id=1;
	scanf("%d",&t);
	while(t--)
	{
		for(int i=0;i<4;++i)
			scanf("%s",grid[i]);
		printf("Case #%d: ",id++);
		if(check('O'))
			printf("O won\n");
		else if(check('X'))
			printf("X won\n");
		else if(emptyCells())
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
}
