#if 1
#include <functional>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <list>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;

const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;

#define mp make_pair
#define pb push_back
#define X first
#define Y second

#define dbg(x) { cerr << #x << " = " << x << endl; }

// extended template
#pragma comment(linker, "/STACK:36777216")
typedef vector<int> vi;
typedef vector<vi> vvi;


#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;

#define NAME "problem"


int solve(vector <string> &a)
{
	// horizont
	for (int i = 0; i < 4; i++)
	{
		int cnt = 0;
		char suit = a[i][0];
		if (suit == 'T')
			suit = a[i][1];
		if (suit == '.')
			continue;

		for (int k = 0; k < 4; k++)
		{
			 if (suit == a[i][k] || a[i][k] == 'T')
				 cnt++;
		}
		if (cnt == 4)
		{
			if (suit == 'X')
				return 0;
			if (suit == 'O')
				return 1;
		}
	}

	// vert
	for (int k = 0; k < 4; k++)
	{
		int cnt = 0;
		char suit = a[0][k];
		if (suit == 'T')
			suit = a[1][k];
		if (suit == '.')
			continue;
		for (int i = 0; i < 4; i++)
		{
			if (suit == a[i][k] || a[i][k] == 'T')
				 cnt++;
		}
		if (cnt == 4)
		{
			if (suit == 'X')
				return 0;
			if (suit == 'O')
				return 1;
		}
	}

	// diag1
	
	char suit = a[0][0];
	if (suit == 'T')
		suit = a[1][1];
	if (suit != '.')
	{	
		int cnt = 0;
		for (int i = 0; i < 4; i++)
		{
			if (suit == a[i][i] || a[i][i] == 'T')
				 cnt++;
		}
		if (cnt == 4)
		{
			if (suit == 'X')
				return 0;
			if (suit == 'O')
				return 1;
		}
	}

	// diag2

	suit = a[0][3];
	if (suit == 'T')
		suit = a[1][2];
	if (suit != '.')
	{	
		int cnt = 0;
		for (int i = 0; i < 4; i++)
		{
			if (suit == a[i][3 - i] || a[i][3 - i] == 'T')
				 cnt++;
		}
		if (cnt == 4)
		{
			if (suit == 'X')
				return 0;
			if (suit == 'O')
				return 1;
		}
	}

	// else
	int mark = 0;
	for (int i = 0; i < 4; i++)
	{
		for (int k = 0; k < 4; k++)
		{
			if (a[i][k] != '.')
				mark++;
		}
	}
	if (mark == 16)
		return 2;
	else
		return 3;
}
int main()
{
	START
	freopen("A-large.in","r",stdin);freopen("output2.txt","w",stdout);
	int t;
	scanf("%d\n", &t);
	for (int test = 1; test <= t; test++)
	{
		vector <string> a(4, string(4, '.'));
		for (int i = 0; i < 4; i++)
		{
			for (int k = 0; k < 4; k++)
				scanf("%c", &a[i][k]);
			scanf("\n");
		}
		printf("Case #%d: ", test);
		int ans = solve(a);
		if (ans == 0)
			printf("X won\n");
		if (ans == 1)
			printf("O won\n");
		if (ans == 2)
			printf("Draw\n");
		if (ans == 3)
			printf("Game has not completed\n");
	}
	END
    return 0;
}
/*******************************************
*******************************************/
#endif