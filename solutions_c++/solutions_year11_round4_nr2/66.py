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

int a[505][505];
int xi[505][505][505];
int xj[505][505][505];
int si[505][505];
int sj[505][505];

int main( )
{
	int i, j, k, t, tt;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d: ", t );
        fprintf(stderr, "%d\n", t);
        
        n = ni(); m = ni();
        ni();
        
        int z = max(n,m);
        
        fi(n)
        {
            string s = ns();
            fj(m)
            {
                a[i][j] = s[j] - '0';
                if (i) si[i][j] = si[i - 1][j] + a[i - 1][j];
                if (j) sj[i][j] = sj[i][j - 1] + a[i][j - 1];
            }
        }

        fi(n) fj(m)
        {
            int j1 = j, j2 = j, moo = 0;
            fk(z)
            {
                if (j1 < 0 || j2 >= m) break;
                xj[i][j1][j2] = moo;
                -- j1; ++ j2;
                moo += (a[i][j1] - a[i][j2]) * (k + 1);
            }
        } 
        fi(n) fj(m)
        {
            int j1 = j, j2 = j + 1, moo = a[i][j] - a[i][j + 1];
            fk(z)
            {
                if (j1 < 0 || j2 >= m) break;
                xj[i][j1][j2] = moo;
                -- j1; ++ j2;
                moo += (a[i][j1] - a[i][j2]) * (2 * (1+k) + 1);
            }
        } 

        fi(n) fj(m)
        {
            int i1 = i, i2 = i, moo = 0;
            fk(z)
            {
                if (i1 < 0 || i2 >= n) break;
                xi[j][i1][i2] = moo;
                -- i1; ++ i2;
                moo += (a[i1][j] - a[i2][j]) * (k + 1);
            }
        } 
        fi(n) fj(m)
        {
            int i1 = i, i2 = i + 1, moo = a[i][j] - a[i + 1][j];
            fk(z)
            {
                if (i1 < 0 || i2 >= n) break;
                xi[j][i1][i2] = moo;
                -- i1; ++ i2;
                moo += (a[i1][j] - a[i2][j]) * (2 * (1+k) + 1);
            }
        } 
        
        int ans = -1;
        fi(n) fj(m)
        {
            int i1 = i, i2 = i, j1 = j, j2 = j, ii = 0, jj = 0;
            fk(z)
            {
                ii += a[i1][j1] * k + a[i1][j2] * k - a[i2][j1] * k - a[i2][j2] * k;
                jj += a[i1][j1] * k - a[i1][j2] * k + a[i2][j1] * k - a[i2][j2] * k;

                -- i1; -- j1; ++ i2; ++ j2;
                
                if (i1 < 0 || i2 >= n) break;
                if (j1 < 0 || j2 >= m) break;
                
                ii += xi[j1][i1][i2];
                ii += xi[j2][i1][i2];
                
                jj += xj[i1][j1][j2];
                jj += xj[i2][j1][j2];
                
                ii += (sj[i1][j2] - sj[i1][j1 + 1]) * (k + 1);
                ii -= (sj[i2][j2] - sj[i2][j1 + 1]) * (k + 1);

                jj += (si[i2][j1] - si[i1 + 1][j1]) * (k + 1);
                jj -= (si[i2][j2] - si[i1 + 1][j2]) * (k + 1);

                ii -= a[i1][j1] * (k+1) + a[i1][j2] * (k+1) - a[i2][j1] * (k+1) - a[i2][j2] * (k+1);
                jj -= a[i1][j1] * (k+1) - a[i1][j2] * (k+1) + a[i2][j1] * (k+1) - a[i2][j2] * (k+1);

                if (ii == 0 && jj == 0) ans = max(ans, k * 2 + 3);
            }
        }

        fi(n) fj(m)
        {
            int i1 = i, i2 = i + 1, j1 = j, j2 = j + 1, ii = 0, jj = 0;
            fk(z)
            {
                ii += a[i1][j1] * (2*k+1) + a[i1][j2] * (2*k+1) - a[i2][j1] * (2*k+1) - a[i2][j2] * (2*k+1);
                jj += a[i1][j1] * (2*k+1) - a[i1][j2] * (2*k+1) + a[i2][j1] * (2*k+1) - a[i2][j2] * (2*k+1);
                
                int mul = (2*(1+k)+1);

                -- i1; -- j1; ++ i2; ++ j2;
                
                if (i1 < 0 || i2 >= n) break;
                if (j1 < 0 || j2 >= m) break;
                
                ii += xi[j1][i1][i2];
                ii += xi[j2][i1][i2];
                
                jj += xj[i1][j1][j2];
                jj += xj[i2][j1][j2];
                
                ii += (sj[i1][j2] - sj[i1][j1 + 1]) * mul;
                ii -= (sj[i2][j2] - sj[i2][j1 + 1]) * mul;

                jj += (si[i2][j1] - si[i1 + 1][j1]) * mul;
                jj -= (si[i2][j2] - si[i1 + 1][j2]) * mul;
                
                ii -= a[i1][j1] * mul + a[i1][j2] * mul - a[i2][j1]  * mul - a[i2][j2] * mul;
                jj -= a[i1][j1] * mul - a[i1][j2] * mul + a[i2][j1]  * mul - a[i2][j2] * mul;
                
                if (ii == 0 && jj == 0) ans = max(ans, k * 2 + 4);
            }
        }
        
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
	}

	return 0;
}
