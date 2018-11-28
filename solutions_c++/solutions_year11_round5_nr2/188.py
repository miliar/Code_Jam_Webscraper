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

int t[50000];
int z[50000];
int tot;

int cnt[20000];

int mn()
{
    int r = 1;
    int len = 16384;
    while (r < 16384) {
        if (z[r]) {
            t[r] += z[r] * len;
            z[2 * r] += z[r];
            z[2 * r + 1] += z[r];
            z[r] = 0;
        }
        if (t[r * 2] + z[r * 2] * len / 2) r=  r * 2;
        else r = r * 2+ 1;
        len /= 2;
    }
    return r - 16384;
}

void inc(int l, int v)
{
    tot += l * v;
    int id = l + 16384;
    int acc = 0;
    int len = 1;
    while (id > 1)
    {
        t[id] += acc * v;
        if (id & 1) { 
            z[id - 1] += v;
            acc += len;
        }
        id >>= 1;
        len *= 2;
    }
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

        int n = ni();
        vector<int> q;
        _(cnt, 0);
        fi(n) { q.pb(ni()); cnt[q.back()] ++; }

/*        int e;
        fr(e, n + 1) if(e && n % e == 0)
        {
            _(::t, 0, sizeof(::t));
            _(z, 0, sizeof(z));
            tot = 0;

            fi(n) {
                inc(q[i] + 1, 1);
                inc(q[i], -1);
            }

            fi(n / e)
            {
                int la = mn();
                inc(la + e, -1);
                inc(la, 1);
            }

            bool ok = true;
            fi(16384) if(z[i]) { z[i*2] += z[i]; z[i * 2 + 1] += z[i]; }
            fi(16384) if (z[16384 + i] + ::t[16384 + i] < 0) ok = false;

            if (ok) ans = e;
        }*/

        int ans = 20000;
        deque<int> lens;
        fi(20000) {
            while(lens.size() > cnt[i]) {
                ans = min(ans, lens.front());
                lens.pop_front();
            }
            fj(lens.size()) lens[j] ++;
            while(lens.size() < cnt[i]) lens.pb(1);
        }

        printf(" %d\n", ans % 20000);
	}

	return 0;
}
