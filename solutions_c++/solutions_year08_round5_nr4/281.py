#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iostream>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))
#define DBG(a) cerr << a << endl;
#define DEBUG 1

#define OBS -100000
#define MOD 10007

int tc, h, w, n;
int tab[128][128];

int inside(int a, int b) { return a < h && b < w; }

int main()
{
	int i,j,k,t;

	scanf("%d", &tc);
	FOR(t, tc)
	{
		scanf("%d %d %d", &h, &w, &n);
		ZERO(tab);
		FOR(i, n) { scanf("%d %d", &j, &k); tab[j-1][k-1] = OBS; }
		tab[0][0] = 1;
		FOR(i, h) FOR(j, w) if (tab[i][j] != OBS)
			{
				if (inside(i + 2, j + 1) && tab[i+2][j+1] != OBS) tab[i+2][j+1] = (tab[i][j] + tab[i+2][j+1]) % MOD;
				if (inside(i + 1, j + 2) && tab[i+1][j+2] != OBS) tab[i+1][j+2] = (tab[i][j] + tab[i+1][j+2]) % MOD;
			}
		
		printf("Case #%d: ", t+1);
		printf("%d\n", tab[h-1][w-1]);
	}
	return 0;
}

