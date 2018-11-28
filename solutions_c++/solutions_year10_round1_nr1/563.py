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
using namespace std ;

#define mp make_pair
#define pb push_back
typedef long long ll ;
typedef long double dbl ;

const int INF = (1 << 30) - 1 ;
const dbl EPS = 1e-9 ;

int n , k ;
char s[50][50] ;
void Load ()
{
	scanf ("%d%d\n", &n, &k) ;
	for (int i = 0; i < n; i++)
		gets (s[i]) ;
}

char b[50][50] ;
bool fl[10] ;
const int di[8] = {0,0,1,-1,1,-1,-1,1} ;
const int dj[8] = {1,-1,0,0,1,-1,1,-1} ;

inline bool Good (int i , int j , char c)
{
	return (0 <= i && i < n && 0 <= j && j < n && b[i][j] == c) ;
}

bool Check (int i , int j , char c)
{
	memset (fl, true, sizeof(fl)) ;
	for (int l = 0; l < k; l++)
	{
		for (int q = 0; q < 8; q++)
			if (!Good (i + l * di[q] , j + l * dj[q] , c)) fl[q] = false ;
	}
	bool res = false ;
	for (int q = 0; q < 8; q++) res |= fl[q] ;	
	return res ;
}

void Solve ()
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			b[j][n - i - 1] = s[i][j] ;
    for (int l = 0; l < n * n; l++)
    {
    	for (int i = 0; i < n; i++)
    		for (int j = 0; j < n; j++)
    			if (b[i][j] != '.')
    			{  
    				int i1 = i + 1 ;
    				while (i1 < n && b[i1][j] == '.')
    				{
    					swap (b[i1-1][j] , b[i1][j]) ;
    					i1++ ;
    				}
    			}
    }
    bool w1 = false , w2 = false ;
    for (int i = 0; i < n; i++)
    	for (int j = 0; j < n; j++)
    	{
    		if (b[i][j] == 'R') w1 |= Check (i , j , 'R') ;
    		if (b[i][j] == 'B') w2 |= Check (i , j , 'B') ;
    	}
    if (w1 && w2) 
    {
    	puts ("Both") ;
    	return ;
    }	
    if (w1)
    {
    	puts ("Red") ;
    	return ;
    }	
    if (w2)
    {
    	puts ("Blue") ;
    	return ;
    }
    if (!w1 && !w2) puts ("Neither") ;
}

int main()
{
	int t ;
	scanf ("%d", &t) ;
	for (int i = 1; i <= t; i++)
	{
		Load () ;
		printf ("Case #%d: ", i) ;
		Solve () ; 
	}	
	return 0 ;
}
