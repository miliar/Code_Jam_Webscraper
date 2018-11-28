#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;

int ri() { int a; scanf( "%d", &a ); return a; }
double rf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100000]; string rs() { scanf( "%s", sbuf ); return sbuf; }
long long rll() { long long a; scanf( "%lld", &a ); return a; }

int main(void)
{
	char dict[300];	_(dict,0);
	dict['a']='y';dict['b']='h';dict['c']='e';dict['d']='s';dict['e']='o';dict['f']='c';
	dict['g']='v';dict['h']='x';dict['i']='d';dict['j']='u';dict['k']='i';dict['l']='g';
	dict['m']='l';dict['n']='b';dict['o']='k';dict['p']='r';dict['q']='z';dict['r']='t';
	dict['s']='n';dict['t']='w';dict['u']='j';dict['v']='p';dict['w']='f';dict['x']='m';
	dict['y']='a';dict['z']='q';dict[' ']=' ';

	int i, t, tt;
	freopen( "a-small.in", "r", stdin );
	freopen( "a-small.out", "w", stdout );
	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
 	{
		string s;
		getline(cin,s);
		fi(s.length())
		{
			s[i] = dict[s[i]];
		}
		printf("Case #%d: %s\n",t,s.c_str());
	}
	return (0);
}

