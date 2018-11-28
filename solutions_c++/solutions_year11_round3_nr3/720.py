
#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <sstream>
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
#define oo (int) 10e8
#define mp make_pair
#define pb push_back
#define sz(a) (int)a.size()
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
typedef stringstream ss;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;
typedef vector<ll> vll;

int n, m;

ll gcd(ll a, ll b) {
    return b==0?a:gcd(b,a%b);
}

ll lcm(ll a, ll b) {
    return a*b/gcd(a,b);
}

int main( )
{
    int i, j, k, t, tt;


    scanf( "%d\n", &tt );
    for( t = 1; t <= tt; ++ t )
    {
        printf( "Case #%d: ", t );
        int N = ni(), L = nll(), H = nll();
        vll freq;
        fi(N) freq.pb(ni());
        ll Gcd = freq[0], Lcm = freq[0];
        if(N != 1) 
        fr(i,N-1) {
           Gcd = gcd(Gcd, freq[i+1]);
           Lcm = lcm(Lcm, freq[i+1]);
        }
        ll ans = -1;
        for(ll no = L; no <= H; no++) {
            bool nope = false;
            fi(N) {
                if(freq[i] % no == 0 || no%freq[i] == 0) ;
                else nope = true;
            }
            if(nope == false) {ans = no; break;}
            //if(Gcd%no == 0) {ans = no; break;} 
            //if(no%Lcm == 0) {ans = no; break;}
        }
        if(ans == -1) printf("NO\n");
        else printf("%lld\n",ans);
    }

    return 0;
}


