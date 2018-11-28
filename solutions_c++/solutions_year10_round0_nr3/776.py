#include <iostream>
#include <cmath>
#include <string>
#include <ctime>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#define nextline { while (getchar() != '\n') ; }
#define sqr(a) (a)*(a)
using namespace std ;

#define mp make_pair
#define pb push_back
typedef long long ll ;
typedef long double dbl ;

const int INF = (1 << 30) - 1 ;
const dbl EPS = 1e-9 ;

int r , k , n ;
int g[1005] ;

void Load ()
{
	scanf ("%d%d%d", &r, &k, &n) ;
	for (int i = 0; i < n; i++)
		scanf ("%d", &g[i]) ;
}

int pr[1005] , cost[1005] , was[1005] ;
void Solve ()
{
	memset (was, 0, sizeof(was)) ;
	ll res = 0 ;
	int curk = 0 , j = 0 , st = 0 ;
	while (!was[j])
	{
		was[j] = 1 ;
		st = j , curk = 0 ;
		while (curk + g[j] <= k)
		{
			curk += g[j] ;
			j = (j + 1) % n ;
			if (j == st) break ;
		}
		cost[st] = curk ;
		pr[st] = j ;
	}
	j = 0 ;
	for (int i = 1; i <= r; i++)
	{
		res += cost[j] ;
		j = pr[j] ;
	}
	cout << res ;
}

int main()
{
	clock_t start = clock() ;
	freopen ("out","w",stdout) ;
	int t ;
	scanf ("%d", &t) ;
	for (int i = 1; i <= t; i++)
	{
		Load () ;
		printf ("Case #%d: ", i) ;
		Solve () ;
		printf ("\n") ;
	}	
	cerr << (double)(clock() - start) / CLOCKS_PER_SEC ;
	return 0 ;
}
