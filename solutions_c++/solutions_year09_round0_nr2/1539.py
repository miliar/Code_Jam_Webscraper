#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <climits>
#include <string>
#include <cstring>
using namespace std;

#define forn(a, n) for(int (a) = 0; (a) < (n); ++(a))
#define forsn(a, s, n) for(int (a) = (s); (a) < (n); ++(a))
#define forall(a, b) for(typeof((b).begin()) (a) = (b).begin(); (a) != (b).end(); ++(a))
#define esta(a, b) (((a) & (1LL<<(b))) != 0)

typedef long long tint;
const int INF = INT_MAX-1000;

const int DX[] = {-1,0,0,1};
const int DY[] = {0,-1,1,0};

int t, h, w, mapa[128][128], id[128][128], usado[32], next;
char ret[128][128];

bool validpos(int x, int y)
{
	return x>=0&&x<h&&y>=0&&y<w;
}

int dfs(int i, int j)
{
	if(id[i][j] != -1) return id[i][j];
	
	int mi = INF;
	
	forn(k, 4) if(validpos(i+DX[k], j+DY[k]))
		mi <?= mapa[i+DX[k]][j+DY[k]];
	
	if(mi>=mapa[i][j])
		id[i][j] = next++;
	else
	{
		forn(k, 4) if(validpos(i+DX[k], j+DY[k]))
			if(mapa[i+DX[k]][j+DY[k]] == mi)
				{id[i][j] = dfs(i+DX[k], j+DY[k]); break;}
	}
	
	return id[i][j];
}

int main()
{
#ifdef TAVO92
	freopen("B-large.in" , "r" , stdin);
	freopen("B-large.out", "w" , stdout);
#endif

	scanf("%i", &t);
	
	forn(p, t)
	{
		scanf("%i%i", &h, &w);
		memset(id, -1, sizeof(id));
		memset(usado, 0, sizeof(usado));
		next=0;
		
		forn(i, h) forn(j, w)
			scanf("%i", &mapa[i][j]);
		
		char c = 'a';
		
		printf("Case #%i:\n", p+1);
		
		forn(i, h) forn(j, w) dfs(i, j);
		forn(i, h)
		{
			forn(j, w)
			{
				if(!usado[id[i][j]])
					usado[id[i][j]] = c++;
				
				if(j) printf(" ");
				printf("%c", usado[id[i][j]]);
			}
			
			printf("\n");
		}
	}
	
	return 0;
}
