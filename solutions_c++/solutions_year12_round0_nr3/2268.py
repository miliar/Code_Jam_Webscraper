/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))

typedef long long ll;

#define pb push_back
#define mp make_pair

const int MAXB = 2000000;

int recycles[MAXB+1][9];
char numr[MAXB+1];
int T;
int A, B;

int main()
{
	REP(i, MAXB)
	{
		int x = i+1;
		int len = 10;
		while (len <= x)
			len *= 10;
		
		for (int tens = 10; tens < len; tens *= 10)
		{
			int r = x % tens * (len / tens) + (x / tens);
			if (r >= x || r < len / 10)
				continue;
			bool seen = false;
			REP(j, numr[x]) if (recycles[x][j] == r)
			{
				seen = true;
				break;
			}
			if (!seen)
				recycles[x][numr[x]++] = r;
		}
	}
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d%d", &A, &B);
		int res = 0;
		for (int x = A; x <= B; x++)
			REP(j, numr[x])
				if (recycles[x][j] >= A)
					res++;
		printf("Case #%d: %d\n", tc+1, res);
	}
}
