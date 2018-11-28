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

int tc, n, m;
int tab[11][1 << 10];
char inp[16][16];

int bitct(int x) { int i = 0; while (x > 0) { i += x % 2; x >>= 1; } return i; }

int cansit(int row, int col)
{
	int i;
	FOR(i, n) if ((col & (1 << i)) > 0 && inp[i][row] == 'x') return 0;
	return 1;
}

int in(int x)
{
	return x >= 0;
}

int compat(int c1, int c2)
{
	int i, j;
	
	FOR(i, n)
		if (c1 & (1 << i))
			FORI(j, -1, 0) 
				if (i + j >= 0 && (c2 & (1 << (i + j)))) return 0;
	FOR(i, m)
		if (c2 & (1 << i))
			FORI(j, -1, 0) 
				if (i + j >= 0 && (c1 & (1 << (i + j)))) return 0;
	return 1;
}

int main()
{
	int i,j,k,t;

	scanf("%d", &tc);
	FOR(t, tc)
	{
		scanf("%d%d", &n, &m);
		FOR(i, n) scanf("%s", inp[i]);
		
		ZERO(tab);
		FOR(i, 1 << n) if (cansit(0, i)) tab[0][i] = bitct(i);
//		if (t == 1) FOR(i, 1 << n) printf("%d %d\n", i, tab[0][i]);
		FORI(i, 1, m-1) 
			FOR(j, 1 << n)
				if (cansit(i, j))
					FOR(k, 1 << n)
						if (cansit(i-1, k) && compat(j, k)) 
							tab[i][j] = max(tab[i][j], tab[i-1][k] + bitct(j));
		int ans = 0;
		FOR(i, 1 << n) ans = max(tab[m-1][i], ans);
		
		printf("Case #%d: ", t+1);
		printf("%d\n", ans);
		
	}
	return 0;
}

