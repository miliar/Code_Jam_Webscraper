/*
name 	: Nurzhan Dyussenaliyev
handle	: dyussenaliyev
mail	: imbacoder1@gmail.com
country	: Kazakhstan
*/

//include <brain.h>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

const int inf = (1<<30);
#define pi 3.1415926535897932
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define clr(a,key) memset((a), (key), sizeof((a)))
#define cpy(a,b) memcpy((a), (b), sizeof((a)))
#define all(x) (x).begin(), (x).end()
#define X first
#define Y second

#if (defined(WIN32) || !defined(__GNUC__))
#  define I64 "%I64d"
#else
#  define I64 "%Ld"
#endif

int Rand() { return (rand() << 16) | rand(); }

inline void Bot_Trust(int Test)
{
	int i,n,w,pos,turn[100],c[2]={0},secs=0,o=1,b=1;
	vector<int> p[2];
	char who;
	cin >> n;
	for (i = 0; i < n; i++)
	{
		cin >> who >> pos;
		w = (who == 'B');
		p[w].pb(pos);
		turn[i] = w;
	}
	for (i = 0; i < n; i++)
	{
		if (turn[i] == 0)
		{
			while (o != p[0][c[0]])
			{
				secs++;
				if (o < p[0][c[0]])
					o++;
				else
					o--;
                if (p[1].empty())
			        continue;
				if (b < p[1][c[1]])
					b++;
				else
				if (b > p[1][c[1]])
					b--;
			}
			secs++;
			c[0]++;
			if (p[1].empty())
			   continue;
			if (b < p[1][c[1]])
				b++;
			else
			if (b > p[1][c[1]])
				b--;
		}
		else
		{
			while (b != p[1][c[1]])
			{
				secs++;
				if (b < p[1][c[1]])
					b++;
				else
					b--;
				if (p[0].empty())
				   continue;
				if (o < p[0][c[0]])
					o++;
				else
				if (o > p[0][c[0]])
					o--;
			}
			secs++;
			c[1]++;
			if (p[0].empty())
			   continue;
			if (o < p[0][c[0]])
				o++;
			else
			if (o > p[0][c[0]])
				o--;
		}
	}
	printf("Case #%d: %d\n", Test, secs);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, Test;
	cin >> T;
	for (Test = 1; Test <= T; Test++)
		Bot_Trust(Test);
	return 0;
}
