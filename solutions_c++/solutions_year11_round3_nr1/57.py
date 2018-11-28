#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <vector>
#include <time.h>

#define REP(i, n) for(int i=0, _n=(n); i<_n; i++)
#define REPD(i, n) for(int i=(n-1); i>=0; i--)
#define FOR(i, a, b) for(int i=a, _b=(b); i<=_b; i++)
#define FORD(i, a, b) for(int i=a, _b=(b); i>=_b; i--)
#define FILL(a, v) memset(&a, v, sizeof(a))
#define DB(x) cout << #x << " : " << x << endl
#define x first
#define y second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long LL;
typedef pair<int, int> pii;

const int maxr = 109;

int t, r, c;
char f[maxr][maxr];
bool bad = 0;

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	FOR(tnum, 1, t)
	{
		scanf("%d %d\n", &r, &c);
		REP(i, r)
		{
			REP(j, c)
			{
				scanf("%c", &f[i][j]);
			}
			scanf("\n");
		}
		printf("Case #%d:\n", tnum);
		bad = 0;
		REP(i, r)
		{
			REP(j, c)
			{
				if (f[i][j] == '#')
				{
					if (f[i+1][j] != '#' || f[i][j+1] != '#' || f[i+1][j+1] != '#')
						bad = 1;
					else
					{
						f[i][j] = '/';
						f[i+1][j] = '\\';
						f[i][j+1] = '\\';
						f[i+1][j+1] = '/';
					}
				}
				if (bad) { printf("Impossible\n"); j = c+1; i = r+1; }
			}
		}
		if (!bad)
		{
			REP(i, r)
			{
				REP(j, c)
				{
					printf("%c", f[i][j]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}
