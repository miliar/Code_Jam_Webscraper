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

vector<pair<double, double>> vv;

int main( )
{
	int i, j, k, t, tt;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d: ", t );
        
        vv.clear();
        
        double x = nf();
        double s = nf();
        double r = nf();
        double t = nf();
        n= ni();
        fi(n)
        {
            double a= nf();
            double b = nf();
            double c= nf();
            vv.pb(mp(s + c, b - a));
            x -= (b - a);
        }
        vv.pb(mp(s, x));
        
        sort(all(vv));

        int q = vv.size();
        for (i = 0; i < q; ++ i)
        {
            double z = min(vv[i].second / (vv[i].first - s + r), t);
            t -= z;
            vv[i].second -= z * (vv[i].first - s + r);
            vv.pb(mp(vv[i].first - s + r, z * (vv[i].first - s + r)));
        }
        double ans = 0;
        fi(vv.size())
        {
            ans += vv[i].second / vv[i].first;
        }
        printf("%.18lf\n", ans);
	}

	return 0;
}
