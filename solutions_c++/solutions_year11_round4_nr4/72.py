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
bool sm[505][505];
int sm2[505][505];

int dst[505][505];
set<pair<int, pair<int, int>>> q;

int cnt[70000];

int moo(int a, int b, int c)
{
    int i;
    int ret = 0;
    fi(27)
    {
        int z = sm2[a][i];
        z &= ~(sm2[b][i] | sm2[c][i]);
        ret += cnt[z];
    }
    return ret;
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    
    fi(70000) if(i) cnt[i] = cnt[i&(i-1)] + 1;

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d: ", t );
        fprintf(stderr, "%d\n", t);
        
        _(sm, 0 );
        _(sm2, 0 );
        _(dst, -1);
        n = ni(); m = ni();
        fi(m)
        {
            string s = ns();
            int a, b;
            sscanf(s.c_str(), "%d,%d", &a, &b);
            sm[a][b] = sm[b][a] = 1;
            sm2[a][b >> 4] |= (1 << (b&15));
            sm2[b][a >> 4] |= (1 << (a&15));
        }
        fi(n) sm2[i][i >> 4] |= (1 << (i & 15));
        
        q.clear();
        
        dst[0][0] = 1000000 - moo(0, 401, 401) + 1;
        q.insert(mp(dst[0][0], mp(0, 0)));

        int avd = -1;
        
        while(q.size())
        {
            auto e = *q.begin();
            q.erase(q.begin());
            
            int v = e.second.first;
            int o = e.second.second;
            
            if (sm[v][1])
            {
                if (avd == -1 || avd > dst[v][o])
                {
                    avd = dst[v][o];
                }
            }

            fi(n) if (sm[v][i])
            {
                int nd = dst[v][o] + 1000000 - moo(i, v, o) + 1;
                if (dst[i][v] == -1 || dst[i][v] > nd)
                {
                    q.erase(mp(dst[i][v], mp(i, v)));
                    dst[i][v] = nd;
                    q.insert(mp(dst[i][v], mp(i, v)));
                }
            }
        }
        
        printf("%d %d\n", avd / 1000000, (1000000 - (avd % 1000000)) % 1000000);
	}

	return 0;
}
