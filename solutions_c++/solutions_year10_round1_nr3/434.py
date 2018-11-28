#include <iostream>
#include <map>
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
using namespace std ;

#define mp make_pair
#define pb push_back
#define PII pair<int,int>
typedef long long ll ;
typedef long double dbl ;

const int INF = (1 << 30) - 1 ;
const dbl EPS = 1e-9 ;

int a1 , b1 , a2 , b2 ;
void Load ()
{
	scanf ("%d%d", &a1, &a2) ;
	scanf ("%d%d", &b1, &b2) ;
}

map < pair <PII , int> , int> dp ;
bool Rec (int a , int b , int x)
{
	if (dp.find(mp(mp(a,b),x)) != dp.end()) return dp[mp(mp(a,b),x)] ;
	if (a <= 0 || b <= 0) return x ;
	if ((a == 1 && b != 1) || (b == 1 && a != 1)) return x ;
	if (a == b) return !x ;
	bool res = !x ;
	for (int k = 1; ;k++)
	{
		if (b * k > a && a * k > b) break ;
		if (Rec (a - b * k , b , !x) == x) res = x ;
		if (Rec (a , b - a * k , !x) == x) res = x ;
		if (res == x) break ;
	}
	//cerr << a << " " << b << " " << x << " " << res << endl ;
	return dp[mp(mp(a,b),x)] = res ;
}

void Solve ()
{
	//cerr << Rec (5 , 8 , 0) << endl ;
	//return ;
	int res = 0 ;
	for (int i = a2; i >= a1; i--)
		for (int j = b2; j >= b1; j--)
			if (!Rec (i , j , 0))  
			{
				res++ ;                        
			}	
	printf ("%d", res) ;
	cout << endl ;
}

int main()
{
	//clock_t start = clock() ;
	int t ;
	scanf ("%d", &t) ;
	for (int i = 1; i <= t; i++)
	{
		printf ("Case #%d: ", i) ;
		Load () ;
		Solve () ;
	}	
	//fprintf (stderr, "%.6lf", (double)(clock() - start) / CLOCKS_PER_SEC) ;
	return 0 ;
}
