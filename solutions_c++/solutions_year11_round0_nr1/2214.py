#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

#define inf 2000000001
#define ll long long
#define minim(a, b) ((a < b) ? a : b)
#define maxim(a, b) ((a > b) ? a : b)
#define pii pair<int, int>
#define x first
#define y second
#define pb push_back
#define mp make_pair

int N, pozA, pozB, timeA, timeB;

inline int modul(int x)
{ return x < 0 ? -x : x; }

int main()
{
	int test, T, i, newPoz, dst;
	char c;
	
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d\n", &T);
	for (test = 1; test <= T; ++test)
	{
		scanf("%d ", &N);
		pozA = pozB = 1;
		timeA = timeB = 0;
		for (i = 1; i <= N; ++i)
		{
			scanf("%c %d ", &c, &newPoz);
			if (c == 'O')
			{
				dst = modul(newPoz - pozA) + 1;
				timeA = maxim(timeA + dst, timeB + 1);
				pozA = newPoz;
			}
			else
			{
				dst = modul(newPoz - pozB) + 1;
				timeB = maxim(timeB + dst, timeA + 1);
				pozB = newPoz;
			}
		}
		scanf("\n");
		
		printf("Case #%d: %d\n", test, maxim(timeA, timeB));
		
	}
	
	return 0;
}
