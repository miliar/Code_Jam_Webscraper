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
int n1, n2;
double X1[105], Y1[105];
double X2[105], Y2[105];

double moo(double l, double r, int n, double* x, double* y)
{
    int i;
    double ret = 0;
    fi(n - 1)
    {
        double lx = max(x[i], l);
        double rx = min(x[i + 1], r);
        if (lx < rx)
        {
            ret += ((y[i + 1] - y[i]) * (lx + rx - x[i] * 2) / (x[i + 1] - x[i]) / 2 + y[i]) * (rx - lx);
        }
    }
    return ret;
}

double moo(double l, double r)
{
    return - moo(l, r, n1, X1, Y1) + moo(l, r, n2, X2, Y2);
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
        printf("Case #%d:\n", t);
        double w = nf();
        n1 = ni(); n2 = ni();

        int g = ni();
        fi(n1) scanf("%lf %lf", &X1[i], &Y1[i]);
        fi(n2) scanf("%lf %lf", &X2[i], &Y2[i]);

        double s = moo(0, w) / g;
        fi(g) if (i)
        {
            double l = 0; double r = s;
            fj( 100 ) {
                double e = (l + r) / 2.0;
                if (moo(0, e) < i * s) l = e;
                else r = e;
            }
            printf("%.18lf\n", r);
        }
	}

	return 0;
}
