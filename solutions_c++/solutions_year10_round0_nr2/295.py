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
#define sqr(a) (a)*(a)
using namespace std ;

#define mp make_pair
#define pb push_back
typedef long long ll ;
typedef long double dbl ;

const int INF = (1 << 30) - 1 ;
const dbl EPS = 1e-9 ;

int n ;
int t[3] ;
void Load ()
{
	scanf ("%d", &n) ;
	for (int i = 0; i < n; i++)
		scanf ("%d", &t[i]) ;
}

void Solve ()
{
	int tt = 0 ;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			tt = __gcd (tt , abs(t[i] - t[j])) ;
	printf ("%d", (tt - (t[0] % tt)) % tt) ;	
}

int main()
{
	freopen ("out1","w",stdout) ;
	int t ;
	scanf ("%d", &t) ;
	for (int i = 1; i <= t; i++)
	{
		Load () ;
		printf ("Case #%d: ", i) ;
		Solve () ;
		printf ("\n") ;
	}	
	return 0 ;
}
