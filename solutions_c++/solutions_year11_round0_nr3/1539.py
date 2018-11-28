/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define REPE(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))

#define pb push_back
#define mp make_pair
#define DEBUG 1
#define PRINT(x...) DEBUG && printf(x)


int T;
int N, C[1005];
int main()
{
	//freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d", &N);
		int xall = 0, tot = 0, least = 999999999;
		REP(i, N)
		{
			scanf("%d", &C[i]);
			xall ^= C[i];
			tot += C[i];
			least = min(least, C[i]);
		}
		
		printf("Case #%d: ", tc+1);
		
		if (xall)
			puts("NO");
		else
			printf("%d\n", tot - least);
	}
}
