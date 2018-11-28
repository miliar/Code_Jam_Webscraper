#pragma comment(linker, "/STACK:1073741824")
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <iostream>
#include <functional>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
#include <cassert>
#include <cmath>
#include <ctime>

#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define fornd(i,n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i,b,a) for (int i = (int)(b); i >= (int)(a); i--)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define _(a, val) memset (a, val, sizeof(a))
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
const ld eps = 1e-9;
const int INF = 1000000000;

using namespace std;

void prepare(string s){
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if (s != "")
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

int n;
char c[4][4];

void readdata ()
{
	scanf ("%d\n", &n);
	
	forn(i, n)
	{
		bool emptyCells = false;

		forn(j, 4)
		{
			forn(k, 4)
			{
				scanf ("%c", &c[j][k]);
				if (c[j][k] == '.')
					emptyCells = true;
			}
			scanf ("\n");
		}
		scanf ("\n");

		int cntX = 0, cntO = 0;

		forn(j, 4)
		{
			int cx = 0, co = 0, t = 0;
			forn(k, 4)
			{
				if (c[j][k] == 'X')
					cx ++;
				if (c[j][k] == 'O')
					co ++;
				if (c[j][k] == 'T')
					t ++;
			}

			if (cx + t == 4 && co == 0)
				cntX ++;
			if (co + t == 4 && cx == 0)
				cntO ++;

			cx = 0, co = 0, t = 0;
			forn(k, 4)
			{
				if (c[k][j] == 'X')
					cx ++;
				if (c[k][j] == 'O')
					co ++;
				if (c[k][j] == 'T')
					t ++;
			}

			if (cx + t == 4 && co == 0)
				cntX ++;
			if (co + t == 4 && cx == 0)
				cntO ++;
		}

		int cx = 0, co = 0, t = 0;

		forn(j, 4)
		{
			if (c[j][j] == 'X')
				cx ++;
			if (c[j][j] == 'O')
				co ++;
			if (c[j][j] == 'T')
				t ++;
		}

		if (cx + t == 4 && co == 0)
			cntX ++;
		if (co + t == 4 && cx == 0)
			cntO ++;

		cx = 0, co = 0, t = 0;

		forn(j, 4)
		{
			if (c[j][3 - j] == 'X')
				cx ++;
			if (c[j][3 - j] == 'O')
				co ++;
			if (c[j][3 - j] == 'T')
				t ++;
		}

		if (cx + t == 4 && co == 0)
			cntX ++;
		if (co + t == 4 && cx == 0)
			cntO ++;

		if (cntX > 0 && cntO == 0)
			printf ("Case #%d: X won\n",i + 1);
		else
			if (cntX == 0 && cntO > 0)
				printf ("Case #%d: O won\n", i + 1);
			else
				if (!emptyCells)
					printf ("Case #%d: Draw\n", i + 1);
				else
					printf ("Case #%d: Game has not completed\n", i + 1);
	}
}

void writedata ()
{

}

void solve ()
{

}

int main ()
{
	prepare("");

	readdata ();
	solve ();
	writedata ();

    return 0;
}
