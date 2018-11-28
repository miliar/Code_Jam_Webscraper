#include<iostream>
#include<cstdio>
#include<cmath>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <list>
#include <map>
#include <string>
using namespace std;


#define M_PI       3.14159265358979323846
#define forn(i, n) for(int i = 0; i < n; ++i)
#define down(i, n) for (int i = n - 1; i >= 0; --i)

#define abs(a) (((a)<0)? (-(a)):(a))

typedef long long int lli;
typedef unsigned long long int ull;
typedef vector<int> vint;


double sqr(double a)
{
	return a * a;
}

double dlin(double x1, double y1, double x2, double y2)
{
	return sqrt(sqr(x2 - x1) + sqr(y2-y1));


}


int TX, TO, O, X, E;
char * PrintAns()
{
	bool wx, wy, e;
	char arr[4][5];
	forn(i, 4)
	{
		scanf("%s", arr[i]);
	}
	forn(i, 4)
	{
		int sum = 0;
		forn(j, 4)
		{
			sum += arr[i][j];
		}
		if (sum == TX || sum == X)
		{
			return "X won";
		}
		if (sum == TO || sum == O)
		{
			return "O won";
		}

	}
	forn(i, 4)
	{
		int sum = 0;
		forn(j, 4)
		{
			sum += arr[j][i];
		}
		if (sum == TX || sum == X)
		{
			return "X won";
		}
		if (sum == TO || sum == O)
		{
			return "O won";
		}


	}
	{
		int sum = 0;
		forn(j, 4)
		{
			sum += arr[j][j];
		}
		if (sum == TX || sum == X)
		{
			return "X won";
		}
		if (sum == TO || sum == O)
		{
			return "O won";
		}

	}
	{
		int sum = 0;
		forn(j, 4)
		{
			sum += arr[3-j][j];
		}
		if (sum == TX || sum == X)
		{
			return "X won";
		}
		if (sum == TO || sum == O)
		{
			return "O won";
		}

	}
	
	forn(i, 4)
	{
		forn(j, 4)
		if (arr[i][j] == '.')
			return "Game has not completed";
	}
	return "Draw";
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	TX = 3 * 'X' + 'T';
	TO = 3 * 'O' + 'T';
	O = 4 * 'O';
	X = 4 * 'X';
	forn (i, T)
	{
		cout<<"Case #" << i + 1<< ": "<<PrintAns()<<endl;
	}
	return 0;
}