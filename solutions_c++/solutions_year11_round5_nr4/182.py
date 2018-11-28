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

bool sq(long long a) {
    long long l = 0; long long r = 2000000000LL;
    while (r - l > 1) 
    {
        long long e = (l + r) / 2;
        if (e * e  <= a) l = e;
        else r = e;
    }
    return l * l == a;
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
        fprintf(stderr, "%d\n", t);
		printf( "Case #%d:", t );
        int cnt = 0;
        string s = ns();
        fi(s.size()) if (s[i] == '?') ++ cnt;
        fi(1 << cnt)
        {
            string f = s;
            int moo = i;
            fj(f.size()) if (f[j] == '?') {
                f[j] = (moo & 1) + '0';
                moo >>= 1;
            }

            long long q = 0;
            fj(f.size()) q = q * 2LL + (long long)(f[j] - '0');

            if (sq(q)) { printf(" %s\n", f.c_str()); break; }
        }
	}

	return 0;
}
