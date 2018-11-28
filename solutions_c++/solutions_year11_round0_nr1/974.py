#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <map>
#include <queue>

#define REP(i,n) for(int i=0; i<n; i++)
#define REPD(i,n) for(int i=(n-1); i>=0; i--)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i, a,b) for(int i=a; i>=b; i--)
#define FILL(a, v) memset(&a, v, sizeof(a))
#define DB(x) cout << #x << " : " << x << endl
#define pb push_back
#define mp make_pair
#define x first
#define y second

using namespace std;

int T, k, n, tmm;
int bpos, opos, blast, olast;
char c;

int main()
{
	//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	FOR(Tn, 1, T)
	{
		printf("Case #%d: ", Tn);
		scanf("%d", &k);
		bpos = opos = 1; olast = blast = 0;
		tmm = 0;
		REP(Mn, k)
		{
			scanf(" %c %d", &c, &n);
			if (c == 'B')
			{
				int d = abs(n - bpos);
				int free = tmm - blast;
				d = max(d - free, 0);
				tmm += d + 1;
				blast = tmm;
				bpos = n;
			}
			else
			if (c == 'O')
			{
				int d = abs(n - opos);
				int free = tmm - olast;
				d = max(d - free, 0);
				tmm += d + 1;
				olast = tmm;
				opos = n;
			}
		}
		printf("%d\n", tmm);
	}
	return 0;
}
