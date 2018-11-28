#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#define nextline { while (getchar() != '\n') ; }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
using namespace std ;

#define mp make_pair
#define pb push_back
#define PII pair<int,int>
typedef long long ll ;
typedef long double ldb ;

const int INF = (1 << 30) - 1 ;
const ldb EPS = 1e-9 ;

int p ;
vector <PII> m;
int cost[20][1 << 12] ;
void Load ()
{
	scanf ("%d", &p) ;
	int cm ;
	m.resize(0) ;
	m.reserve (1 << p) ;
	memset (cost, 0, sizeof(cost)) ;
	for (int i = 0; i < (1 << p) ; i++)
	{
		scanf ("%d", &cm) ;
		m.pb(mp(cm,i)) ;
	}
	for (int i = 1; i <= p; i++)
	{
		for (int j = 0; j < (1 << (p - i)); j++)
			scanf ("%d", &cost[i][j]) ;
	}
}

bool was[20][1 << 12] ;
void Solve ()
{
	memset (was, false, sizeof(was)) ;
	sort (m.begin(), m.end()) ;
	int res = 0 ;
	for (int i = 0; i < (int)m.size(); i++)
	{
		int x = m[i].second >> 1 ;
		for (int j = 1; j <= p; j++)
		{
			if (was[j][x]) 
			{
				x >>= 1 ;
				continue ;
			}	
			if (m[i].first) m[i].first-- ;
			else
			{
				was[j][x] = 1 ;
				res+=cost[j][x] ;
			}
			x >>= 1 ;
		}
	}
	printf ("%d", res) ;	
}

int main()
{
	int nt ;
	scanf ("%d", &nt) ;
	for (int tt = 1; tt <= nt; tt++)
	{ 
		Load () ;
		printf ("Case #%d: ", tt) ;
		Solve () ;
		printf ("\n") ;
	}	
	return 0 ;
}
