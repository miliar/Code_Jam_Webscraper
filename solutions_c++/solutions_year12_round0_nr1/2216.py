#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

#define file "..\\..\\GCJ\\2012qual\\in\\a"

void prepare()
{
#ifdef _DEBUG
	freopen( "in.txt", "r", stdin );
#else
	freopen( file ".in", "r", stdin );
	freopen( file ".out", "w", stdout );
#endif
}

char p[27];

void precalc()
{
	string s = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	string t = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
	for ( int i = 0; i < s.size( ); i++ )
		p[s[i] - 'a'] = t[i];
	p['z' - 'a'] = 'q';
	for ( char i = 'a'; i <= 'z'; i++ )
	{
		char k;
		for ( k = 'a'; k <= 'z'; k++ )
		{
			if ( p[k - 'a'] == i )
				break;
		}
		if ( k > 'z' )
		{
			for ( k = 'a'; k <= 'z'; k++ )
				if ( p[k - 'a'] < 'a' || p[k - 'a'] > 'z' )
					p[k - 'a'] = i;
			//fprintf(stderr, "%c\n", i);
			break;
		}
	}
	//for ( char i = 'a'; i <= 'z'; i++ )
	//	fprintf( stderr, "%c", p[i - 'a'] );
	//fprintf( stderr, "%c", '\n' );
}

const int MAXL = 111;
char s[MAXL];

bool solve()
{
	gets( s );
	int i, l = strlen( s );
	for ( i = 0; i < l; i++ )
		putchar( ( s[i] >= 'a' && s[i] <= 'z' ) ? p[s[i] - 'a'] : s[i] );
	putchar( '\n' );
	return false;
}

int main()
{
	precalc( );
	prepare( );
	//solve( );
//#ifdef _DEBUG
	int tt;
	scanf( "%d\n", &tt );
	for (int ttt = 0; ttt < tt; ttt++)
	{
		printf( "Case #%d: ", ttt + 1 );
		solve( );
	}
//#endif
	return 0;
}