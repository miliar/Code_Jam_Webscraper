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

#define GAND 1
#define GOR  0
#define LEAF -1
#define CANCHANGE 1

int tc, m, v;
int tab[20000][2];
int ch[20000][2];
int gate[20000];
int can[20000];

int update(int x, int y)
{
	return y == -1 ? x : min(x, y); 
}

int rec(int node, int wanted)
{
	if (tab[node][wanted] != -1) return tab[node][wanted];
	int &res = tab[node][wanted];
	int i,j,k,l;

	if (gate[node] == LEAF) return res;
	
	if (can[node] == CANCHANGE)
	{
		FOR(i, 2) FOR(j, 2) if ((i & j) == wanted)
		{
			k = rec(ch[node][0], i);
			l = rec(ch[node][1], j);
			if (k != -1 && l != -1) res = update(k + l + (gate[node] == GAND ? 0 : 1), res);
		}
		FOR(i, 2) FOR(j, 2) if ((i | j) == wanted)
		{
			k = rec(ch[node][0], i);
			l = rec(ch[node][1], j);
			if (k != -1 && l != -1) res = update(k + l + (gate[node] == GOR ? 0 : 1), res);
		}
	}
	else // cannot change
	{
		if (gate[node] == GAND) 
		{
			FOR(i, 2) FOR(j, 2) if ((i & j) == wanted) 
			{
				k = rec(ch[node][0], i);
				l = rec(ch[node][1], j);
				if (k != -1 && l != -1) res = update(k + l, res);
			}
		}
		else if (gate[node] == GOR)
		{
			FOR(i, 2) FOR(j, 2) if ((i | j) == wanted) 
			{
				k = rec(ch[node][0], i);
				l = rec(ch[node][1], j);
				if (k != -1 && l != -1) res = update(k + l, res);
			}	
		}
	}
	return res;
}

int main()
{
	int i,j,k,t;

	scanf("%d", &tc);
	FOR(t, tc)
	{
		scanf("%d %d", &m, &v);
		cerr << m << " " << v << endl;
		MINUS(tab);
		FOR(i, m) 
		{
			FOR(j, 2) { ch[i][j] = i * 2 + j + 1; if (ch[i][j] >= m) ch[i][j] = -1; }
			if (i * 2 + 2 >= m) 
			{
				scanf("%d", &j);
				tab[i][j] = 0; 
				gate[i] = LEAF;
			}
			else scanf("%d %d", &gate[i], &can[i]);
		}

		rec(0, v);
		
		printf("Case #%d: ", t+1);
		if (tab[0][v] == -1) printf("IMPOSSIBLE\n"); else printf("%d\n", tab[0][v]);
	}
	return 0;
}

