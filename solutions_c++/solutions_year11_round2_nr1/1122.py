
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
typedef vector<double> vd;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int n, m;

int main( )
{
    int i, j, k, t, tt;


    scanf( "%d\n", &tt );
    for( t = 1; t <= tt; ++ t )
    {
        printf( "Case #%d:\n", t );

        vs arr;
        n = ni();
        fi(n) {
            arr.pb(ns());

        }
        vi p(n), w(n);
        vector<vd> wpw = vector<vector<double> > (n, vector<double>(n,0));
        fi(n) fj(n) {
            if(arr[i][j] != '.') p[i]++;
            if(arr[i][j] == '1') w[i]++;
        }
        vd wp(n);
        fi(n) {
            wp[i] = (double)w[i]/p[i];
        }


        fi(n) fj(n) {
            if(arr[i][j] == '.') continue;
            if(arr[i][j] == '0') {
                wpw[i][j] = (double)w[i]/(p[i]-1);
            } else {
                wpw[i][j] = (double)(w[i]-1)/(p[i]-1);
            }
        }

        vd owp(n);

        fi(n) {
            double sum = 0;
            int cnt  = 0;
            fj(n) {
                if(arr[i][j] != '.') {
                    sum += wpw[j][i];
                    cnt++;
                }
                owp[i] = sum/cnt;
            }
        }

        vd oowp(n);

        fi(n) {
            double sum = 0;
            int cnt = 0;
            fj(n) {
                if(arr[i][j] != '.') {
                    sum += owp[j];
                    cnt++;
                }
            }
            oowp[i] = sum/cnt;
        }
        fi(n) 
            printf("%.6lf\n", 0.25 * wp[i] + 0.5*owp[i] + 0.25 * oowp[i]);

    }

    return 0;
}


