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

int tc, n, ngroup;
char abc[50001];
int group[50000][26];
int ct[50000];
int tab[50000][26]; // tab[i][j] = min count with group i end in char j

void printtable()
{
	if (DEBUG)
	{
		int i,j;
		FOR(i, ngroup) 
		{
			printf("%d: ", i);
			FOR(j, 3) printf("%d ", group[i][j]);
			printf("\n");
		}
		FOR(i, ngroup)
		{
			printf("%d: ", i);
			FOR(j, 3) printf("%d ", tab[i][j]);
			printf("\n");
		}
		FOR(i, ngroup) printf("%d: %d\n", i, ct[i]);
	}
}

int update(int x, int y)
{
	return (y == -1) ? x : min(x, y);
}

int main()
{
	int i,j,k,l,S,t;

	scanf("%d", &tc);
	FOR(t, tc)
	{
		ZERO(abc);
		ZERO(group);
		ZERO(ct);
		MINUS(tab);
		scanf("%d %s", &k, abc);
		S = strlen(abc);
		ngroup = S / k;
		FOR(i, S) abc[i] -= 'a';
		FOR(i, ngroup) FOR(j, k) group[i][abc[i * k + j]]++;
		FOR(i, ngroup) FOR(j, 26) ct[i] += group[i][j] ? 1 : 0;
		
		FOR(j, 26) if (group[0][j]) tab[0][j] = ct[0];
		FORI(i, 1, ngroup - 1)
		{
			FOR(j, 26) // prev group
				if (tab[i-1][j] != -1) // prev group can end in this one
					FOR(k, 26) // end of new group
						if (group[i][k]) // new group has this, and we end the group with this one
						{
							if (ct[i] == 1) // the only group!
							{
								if (j == k) tab[i][k] = update(tab[i-1][j], tab[i][k]);
								else tab[i][k] = update(tab[i-1][j] + 1, tab[i][k]);
							}
							else
							{
								if (j == k) // something needs to go in between :(
									tab[i][k] = update(tab[i-1][j] + ct[i], tab[i][k]);
								else 
								{
									if (group[i][j] != 0)// can reduce 1 group! :)
									{
										fprintf(stderr, "Here %d %d %d -- %d %d\n", i, j, k, tab[i-1][j], ct[i]);
										tab[i][k] = update(tab[i-1][j] + ct[i] - 1, tab[i][k]);
									}
									else // don't have j :(
										tab[i][k] = update(tab[i-1][j] + ct[i], tab[i][k]);
								}
							}
						}
		}

		printtable();
		
		printf("Case #%d: ", t+1);
		i = S;
		FOR(j, 26) if (tab[ngroup - 1][j] != -1) i = min(i, tab[ngroup - 1][j]);
		printf("%d\n", i);
	}
	return 0;
}

