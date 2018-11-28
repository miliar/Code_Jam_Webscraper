
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
#include <numeric>
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

ll findttime(vi& dist, int T, int i) {

                ll idist = (ll)accumulate(dist.begin(), dist.begin()+i+1, 0);
                ll itime = idist*2;
                ll ttime = 0LL; 
                if(itime >= T) {
                    ttime += dist[i+1];
                } else if(itime + dist[i+1]*2 <= T) {
                    ttime += 2*dist[i+1];                   
                } else {
                    ttime += (long long) ((T - itime) + dist[i+1] - ( T - itime ) * 0.5 + 0.1);
                }
                return ttime;
}


int main( )
{
    int i, j, k, t, tt;


    scanf( "%d\n", &tt );
    for( t = 1; t <= tt; ++ t )
    {
        printf( "Case #%d: ", t );
        ll L = nll(), T = nll(), N = nll(), C= nll();
        vi per;
        fi(C) {
            per.pb(ni());
        }
        vi dist;
        dist.pb(0);
        fi(N) {
            dist.pb(per[i%C]);
        }
        ll lowtime = oo;
        if(L >= 0) {
            lowtime = 2 * accumulate(all(dist), 0);
        } 
        if (L >= 1) {
            fi(N) {
                ll ttime = 0;
                ll idist = (ll)accumulate(dist.begin(), dist.begin()+i+1, 0);
                ll itime = idist*2;
                ttime += itime;
                ttime += findttime(dist, T, i);
                idist = accumulate(dist.begin()+i+2, dist.end(),0LL);
                itime = idist*2;
                ttime += itime;
                if(ttime < lowtime) lowtime = ttime;
            }
        } 
        if(L >= 2){
            fi(N) fj(N) {
                if(i < j) {
                ll titime = findttime(dist, T, i);
                ll tjtime = findttime(dist, T, j);
                ll ttime = 2*accumulate(dist.begin(), dist.begin()+i+1, 0) + titime + 2*accumulate(dist.begin()+i+2, dist.begin()+j+1, 0) + tjtime + 2*accumulate(dist.begin()+j+2, dist.end(), 0);
                if(ttime < lowtime) lowtime = ttime;
                }
            }
        }
        printf("%lld\n", lowtime);
    }

    return 0;
}


