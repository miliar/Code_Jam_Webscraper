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
#define TASK ""
using namespace std ;

#define mp make_pair
#define pb push_back
typedef long long ll ;
typedef long double dbl ;

const int INF = (1 << 30) - 1 ;
const dbl EPS = 1e-9 ;

int n , k ;
void Load ()
{
	scanf ("%d%d", &n, &k) ;
}

int cnt[35] ;
int state[35] ;
void Solve (int test)
{
	printf ("Case #%d: ", test) ;
	k %= (cnt[n] + 1) ;
	if (k < cnt[n])
	{
		printf ("OFF\n") ;
		return ;
	}
	else printf ("ON\n") ;
	/*for (int i = 1; i <= k % (cnt[n] + 1); i++)
	{
		int j = 1 ;
		while (j <= n && state[j]) 
		{
			state[j] = 0 ;
			j++ ;
		}
		state[j] = 1 ;	
	}
	bool on = true ;
	for (int i = 1; i <= n; i++) on &= state[i] ;
	if (on) printf (" ON\n") ;
	else printf (" OFF\n") ;*/
}

int main()
{
	freopen ("out","w",stdout) ;
	cnt[1] = 1 ;
	for (int i = 2; i <= 30; i++)
		cnt[i] = 2 * cnt[i - 1] + 1 ;
	int t ;
	scanf ("%d", &t) ;
	for (int i = 1; i <= t; i++)
	{
		Load () ;
		Solve (i) ;
	}	
	return 0 ;
}
