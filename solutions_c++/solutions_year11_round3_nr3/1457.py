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
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }
char nc() { char a; scanf("%c", &a); return a; }
/*
typedef map<char,int> mci;

mci tmap;
tmap['O'] = 0;
tmap['B'] = 1;
*/
typedef map<char, int> mci;

mci tmap;

bool check(int x, int y)
{
	if ( ( x % y == 0) ||
		 ( y % x == 0 )) return true;
	return false;
}

int main()
{
	int i,j,k;
	int t = ni();
	fi(t)
	{
		printf("Case #%d: ", i+1);
		int num = ni();
		int low = ni();
		int hi = ni();
		vector<int> fq;
		fj(num)
		  fq.pb( ni() );
		for (j = low; j <= hi;++j)
		{
			fk(num)
			{
				if (!check(j, fq[k]))
					goto nextx;
			}
			printf("%d\n", j);
			goto nextcase;

			nextx:
			{};
		};
		printf("NO\n");
		nextcase:
		{};	  
	}

}
