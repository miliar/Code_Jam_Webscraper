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
#define rfo(a, b) for ( a = (b - 1); a >= 0; a-- ) 
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

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int n, m;


int main( ) {
	int i, j, k, t, tt;

	char eng [] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
	char goo [] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};
        //		0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16  17   18   19   20   21    22   23   24   25
	int map [] = {24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};

	//if it does not work change q <-> m in eng

	freopen( "input.txt", "r", stdin );
	//freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );

	for( t = 1; t <= tt; ++ t ) {
		printf( "Case #%d: ", t );

		string enc;
		getline (cin,enc);

		for ( i = 0; i < enc.size(); i++ ) {
			if (enc[i] == ' ') { printf(" "); continue; }
			printf("%c", eng[map[(int) enc[i] - 97]]);
		}
		
		printf("\n");
	}

	return 0;
}
