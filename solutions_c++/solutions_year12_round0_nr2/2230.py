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

const int MAX = 105;
int T;
int N, S, p, t[MAX];

int main()
{
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d%d%d", &N, &S, &p);
		REP(i, N)
			scanf("%d", &t[i]);
			
		int res = 0;
		REP(i, N)
		{
			REP(c, 10+1) REP(b, c+1) REP(a, b+1)
			{
				if (t[i] != -1 && c-a < 2 && a+b+c == t[i] && c >= p)
				{
					res++;
					t[i] = -1;
				}
			}
		}
		
		REP(i, N)
		{
			REP(c, 10+1) REP(b, c+1) REP(a, b+1)
			{
				if (t[i] != -1 && S && c-a == 2 && a+b+c == t[i] && c >= p)
				{
					res++;
					t[i] = -1;
					S--;
				}
			}
		}
		printf("Case #%d: %d\n", tc+1, res);
	}
}
