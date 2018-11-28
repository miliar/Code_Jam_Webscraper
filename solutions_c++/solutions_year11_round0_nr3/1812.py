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
#define cl(a,key) memset((a), (key), sizeof((a)))
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

inline void Candy_Splitting(int Test)
{
	int i, n, s1 = 0, s2 = 0, x1 = 0, x2 = 0;
	scanf("%d", &n);
	int c[n];
	for (i = 0; i < n; i++)
		scanf("%d", c + i);
	sort(c, c + n);
	for (i = 1; i < n; i++)
	{
		s1 += c[i];
		x1 ^= c[i];
	}
	s2 += c[0];
	x2 ^= c[0];
	if (x1 != x2)
		printf("Case #%d: NO\n", Test);
	else
		printf("Case #%d: %d\n", Test, s1);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int Test = 1; Test <= T; Test++)
		Candy_Splitting(Test);
	return 0;
}
