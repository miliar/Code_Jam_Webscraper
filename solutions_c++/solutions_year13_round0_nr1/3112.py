#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <cstdlib>
#include <cmath>
#include <string.h>
#include <iostream>
#include <limits.h>
#include <cctype>
#include <cfloat>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>
using namespace std;

#define exit exit(0)
#define RESET(a) memset(a,0,sizeof(a))
#define fi first
#define EPS 1e-9
#define se second
#define pb push_back
#define mp make_pair
#define FOR(a,b,c) for(a=b; a<=c; a++)
#define FORR(a,b,c) for(a=b; a<c; a++)
#define FORD(a,b,c) for(a=b; a>=c; a--)
#define bugy int abdc; cin >> abdc
#define cbm(a) ( 1 << a )
#define ALL(a) a.begin(), a.end()

typedef vector <int> vi;
typedef queue <int> qi;
typedef pair <int,int> pii;
typedef pair <double,double> pdd;
typedef long long LL;
int myr[8] = {0, 0, -1,1,-1, 1, -1, 1};
int myc[8] = {1,-1, 0, 0, 1, -1, -1, 1};
int LMAX = 2147483647;
int LMIN = -2147483647;
LL LLMAX = 9223372036854775807LL;
LL LLMIN = -9223372036854775808LL;
int mo = 1000000007;

// ~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~ //
// ~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~@Willson Copyright@~~~~~~~~~~~~#~~~~~~~~~~~~~~~~ //
// ~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~ //

string s[10];
int tc,t;
bool xwon,owon,draw;

bool check( char x )
{
	int i = 0,  j = 0,c = 0;
	while ( i < 4 && j < 4 )
	{	
		if ( s[i][j] == 'T' )
		{
			if ( c == 0 ) c++; else
			break;
		} else if ( s[i][j] != x ) break;
		i++; j++;
		if ( i == 4 && j == 4 ) return 1;
	}
	
	i = 0; j = 3; c = 0;
	while ( i < 4 && j >= 0 )
	{
		if ( s[i][j] == 'T' )
		{
			if ( c == 0 ) c++; else
			break;
		} else if ( s[i][j] != x ) break;
		i++; j--;
		if ( i == 4 && j == -1 ) return 1;
	}
	
	FOR(i,0,3)
	{
		c = 0;
		FOR(j,0,3)
		{
			if ( s[i][j] ==  'T' )
			{
				if ( c == 0 ) c++;
				else break;
			} else if ( s[i][j] != x ) break;
			
			if ( j == 3 ) return 1;
		}
	}
	
	FOR(j,0,3)
	{
		c = 0;
		FOR(i,0,3)
		{
			if ( s[i][j] == 'T' )
			{
				if ( c == 0 ) c++;
				else break;
			} else if ( s[i][j] != x ) break;
			
			if ( i == 3 ) return 1;
		}
	}
	
	return 0;
}

int main()
{
	scanf("%d",&t);
	FOR(tc,1,t)
	{
		xwon = owon = 0;
		draw = 1;
		for ( int i = 0; i < 4; i++ ) cin >> s[i];
		
		for ( int i = 0; i < 4; i++ )
			for ( int j = 0; j < 4; j++ )
				if ( s[i][j] == '.' )
				{
					draw = 0;
					break;
				}
				
		xwon = check('X');
		owon = check('O');
		
		printf("Case #%d: ",tc);
		if ( !xwon && !owon )
		{
			if ( draw ) printf("Draw\n"); else
			printf("Game has not completed\n");
		} else if ( xwon ) printf("X won\n"); 
		else if ( owon ) printf("O won\n");
	}
	return 0;
}
