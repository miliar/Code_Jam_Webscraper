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

inline void Magicka(int Test)
{
	int c,d,i,j,m=0,n;
	string s;
	char ch,e[300],com[300][300];
	bool cl[300][300];
	clr(e,0);
	clr(cl,0);
	clr(com,0);
	cin >> c;
	for (i = 0; i < c; i++)
	{
		cin >> s;
		com[s[0]][s[1]] = com[s[1]][s[0]] = s[2];
	}
	cin >> d;
	for (i = 0; i < d; i++)
	{
		cin >> s;
		cl[s[0]][s[1]] = cl[s[1]][s[0]] = 1;
	}
	cin >> n;
	for (i = 0; i < n; i++)
	{
		cin >> ch;
		if (!m)
			e[++m] = ch;
		else
		{
			if (com[e[m]][ch])
				ch = com[e[m--]][ch];
			if (m)
			{
    			for (j = 0; j <= m; j++)
    			if (cl[e[j]][ch])
    			{
    				m = 0;
    				break;
    			}
    			if (m)
    				e[++m] = ch;
            }
            else
                e[++m] = ch;
		}
	}
	printf("Case #%d: [", Test);
	for (i = 1; i < m; i++) printf("%c, ", e[i]);
	if (m) printf("%c]\n", e[m]); else printf("]\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, Test;
	cin >> T;
	for (Test = 1; Test <= T; Test++)
		Magicka(Test);
	return 0;
}
