/**
	site
	A name (Code: Tic_tac_toe_tomek)
	Source: GCJ 2013
*/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <iterator>
#include <algorithm>
#include <functional>
#include <string>
#include <map>
#include <vector>
#include <set>

typedef long long ll;
typedef long long unsigned llu;

#define	_min(a,b)	((a)<(b)?(a):(b))
#define _max(a,b)	((a)>(b)?(a):(b))

#define GI ({int t;scanf("%d",&t);t;})
#define GL ({ll t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define REP(i,n) FOR(i,0,n)

#define MOD 1000000007
#define INF (int)1e9
#define EPS 1e-9

#define IT(a,it) for (typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define pb push_back
#define mp make_pair

// #define DEBUG

#ifdef DEBUG
	std::string tabs;
	#define INDENT		tabs+="\t"
	#define _EXIT(val)	{ UNINDENT; return val; }
	#define UNINDENT	tabs.erase(tabs.length()-1)
	#define SHOW(x)		cout << tabs << x
	#include <time.h>
	#define STARTTIME	clock_t start = clock();
	#define GETTIME		printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
	#define _DEBUG(x)	x
#else
	#define INDENT
	#define _EXIT(val)	return val
	#define UNINDENT
	#define SHOW(x)
	#define STARTTIME
	#define GETTIME
	#define _DEBUG(x)
#endif

using namespace std;

char board[4][4];

bool checkby(char kind)
{
	int counter;
	REP(row, 4)	// by row
	{
		counter = 0;
		REP(col, 4)
		{
			if (board[row][col] == kind || board[row][col] == 'T')
				counter++;
		}
		if (counter == 4)
			return true;
	}
	REP(col, 4)	// by column
	{
		counter = 0;
		REP(row, 4)
		{
			if (board[row][col] == kind || board[row][col] == 'T')
				counter++;
		}
		if (counter == 4)
			return true;
	}
	counter = 0;
	REP(diag, 4)	// foreward diagonal
	{
		if (board[diag][diag] == kind || board[diag][diag] == 'T')
			counter++;
	}
	if (counter == 4)
		return true;
	
	counter = 0;
	REP(diag, 4)	// backward diagonal
	{
		if (board[diag][3 - diag] == kind || board[diag][3 - diag] == 'T')
			counter++;
	}
	if (counter == 4)
		return true;
	
	return false;
}

void solve_saving()
{
	int t = GI;
	REP(i, t)
	{
		REP (row, 4)
			cin >> board[row];
		scanf("\n");
			
		_DEBUG(
			REP (row, 4)
				cout << board[row] << endl;
		)
		
		cout << "Case #" << i+1 << ": ";
		if (checkby('X'))
			cout << "X won" << endl;
		else if (checkby('O'))
			cout << "O won" << endl;
		else
		{
			bool incomplete = false;
			int counter;
			REP(row, 4)
			{
				counter = 0;
				REP(col, 4)
				{
					incomplete = (board[row][col] == '.');
					if (incomplete) break;
				}
				if (incomplete) break;
			}
			if (incomplete)
				cout << "Game has not completed\n";
			else
				cout << "Draw\n";
		}
			
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
