/*
	ID: lkq19921
	PROG: a
	LANG: C++
*/
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#define INF 2111222333
#define MAX(a, b)    ((a) > (b) ? (a) : (b))
#define MIN(a, b)    ((a) < (b) ? (a) : (b))
#define eps 1e-8
#define MAXN 105
#define DEBUG

using namespace std;

struct pt
{
	int val;
	int idx;
};

vector<pt> ori[2];

int t, n;

int abso(int x)
{
	return x < 0 ? -x : x;
}

void Solve()
{
	int i, tmp, a, b, apos, bpos, tot = 0, atm, btm;
	char str[3];
	ori[0].clear();
	ori[1].clear();
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		scanf("%s%d", str, &tmp);
		if (str[0] == 'B')
			ori[0].push_back((pt){tmp, i});
		else
			ori[1].push_back((pt){tmp, i});
	}
	atm = btm = 0;
	apos = bpos = 1;
	 
	for (a = 0, b = 0; a < ori[0].size() ||	b < ori[1].size(); )
	{
		if (b == ori[1].size() || (a < ori[0].size() && ori[0][a].idx < ori[1][b].idx))
		{
			//printf("%d    Now a goto %d\n", a, ori[0][a].val);
			atm = abso(ori[0][a].val - apos) + atm;
			apos = ori[0][a].val;
			tot = MAX(atm, tot) + 1;
			atm = tot;
			//printf("now time = %d\n", tot);
			a++;
		}
		else
		{
			//printf("%d   Now b goto %d\n", b, ori[1][b].val);
			btm = abso(ori[1][b].val - bpos) + btm;
			bpos = ori[1][b].val;
			tot = MAX(btm, tot) + 1;
			btm = tot;
			//printf("now time = %d\n", tot);
			b++;
		}
	}
	printf("%d\n", tot);
}

int main()
{
	#ifdef DEBUG
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	#endif
	scanf("%d", &t);
	for (int f = 1; f <= t; f++)
	{
		printf("Case #%d: ", f);
		Solve();
	}
	return 0;
}


