#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
//#include <string.h>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <functional>


//#include <sstream>
//#include "Biginteger.cpp"
//#include "sqrt.cpp"
//#include "tree.cpp"
//#include "funcs.cpp"

#define ll long long
#define all(x)          (x).begin(), (x).end()
#define forn(N)         for(ll i = 0; i<N; i++)
#define fornj(N)         for(ll j = 0; j<N; j++)
#define PI 3.1415926535897932384626433
#define INF 2147483647
//#define MOD 1000007
using namespace std;


//#define ONLINE_JUDGE
//#undef ONLINE_JUDGE

char board[4][4];

bool who_Won(char xo)
{
	int tmp;
	forn(4)
	{
		tmp = 0;
		fornj(4)
		{
			tmp += (board[i][j] == xo || board[i][j] == 'T');
		}
		if (tmp == 4) return true;
	}

	forn(4)
	{
		tmp = 0;
		fornj(4)
		{
			tmp += (board[j][i] == xo || board[j][i] == 'T');
		}
		if (tmp == 4) return true;
	}

	tmp = 0;
	forn(4)
	{
		tmp+=(board[i][i] == xo || board[i][i] == 'T');
	}
	if (tmp == 4) return true;

	tmp = 0;
	forn(4)
	{
		tmp+=(board[i][3-i] == xo || board[i][3-i] == 'T');
	}
	if (tmp == 4) return true;
	
	return false;
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	#endif

	int T;
	cin>>T;
	
	for(int t = 1; t<=T; t++)
	{
		bool allFilled = true;
		forn(4)
		{
			fornj(4)
			{
				cin>>board[i][j];
				if (board[i][j] == '.') allFilled = false;
			}
		}
		if (who_Won('O'))
		{
			cout<<"Case #"<<t<<": O won";
		}
		else if(who_Won('X'))
		{
			cout<<"Case #"<<t<<": X won";
		}
		else if (allFilled)
		{
			cout<<"Case #"<<t<<": Draw";
		}
		else
		{
			cout<<"Case #"<<t<<": Game has not completed";
		}
		cout<<endl;
	}
	
	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}