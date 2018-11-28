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
	int i, j, k, l, t, tt;

	freopen( "input.txt", "r", stdin );
	//freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );

	for( t = 1; t <= tt; ++ t ) {
		printf( "Case #%d: ", t );
		int a = ni();
		int b = ni();

		int counter = 0;
		//map<int, int> result; // there will be duplicates, and we need to get rid of them somehow...

		for (i = a; i < b; i++) {
			int d = (int)log10(i) + 1;
			vi digits;

			for (k=d; k >= 1; k--) {
				digits.pb(i % (int) pow(10, k) / (int) pow(10, k - 1));
			}

			vi rdigits = digits;

			for (k = 0; k < digits.size() - 1; k++) {
				int c = rdigits[0];
				rdigits.erase(rdigits.begin());
				rdigits.pb(c);
				for (int c = 0; c < digits.size(); c++) {
					if (rdigits[c] > digits[c]) {
						int r = 0;
						for (j = 0; j < rdigits.size(); j++) {
							r += (int) pow(10, rdigits.size() - j - 1)*rdigits[j];
						}
						if (r > i && r <= b ) { counter++; break; }
					} else if (rdigits[c] < digits[c]) { break; }
				}
			}
		}
		printf("%d\n", counter);
	}

	return 0;
}
