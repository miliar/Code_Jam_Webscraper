#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define VI vector<int>
#define VS vector<string>
#define VVI vector< VI >
#define PB push_back
#define ALL(a) (a).begin(), (a).end()
#define SORT(a) sort( ALL(a) )
#define IPAIR pair<int,int>
#define VIPAIR vector< IPAIR >
#define FOR(i,b,n) for ( int i = (b); i < (n); i++ )
#define REP(i,n) FOR(i,0,n)
#define ll long long

ll select( int n, int m )
{
    if ( n < m ) return 0LL;
    if ( m == 1 ) return (ll)n;
    if ( m == 2 ) {
        return ( (ll)n * (n-1) ) / 2;
    }
    return ( (ll)n * (n-1) * (n-2) ) / 6;
}

int main()
{
    int N;
    scanf( "%d", &N );
    
    for ( int prob = 0; prob < N; prob++ ) {
        ll result = 0;
        int n_, A_, B_, C_, D_, x0_, y0_, M_;
        VIPAIR trees;
        
        scanf( "%d%d%d%d%d%d%d%d", &n_, &A_, &B_, &C_, &D_, &x0_, &y0_, &M_ );
        ll n = n_, A = A_, B = B_, C = C_, D = D_, x0 = x0_, y0 = y0_, M = M_;
        
        {
            int x = x0, y = y0;
            trees.PB( make_pair( x, y ) );
            for ( int i = 1; i <= n-1; i++ ) {
                x = ( A * x + B ) % M;
                y = ( C * y + D ) % M;
                trees.PB( make_pair( x, y ) );
            }
        }
        
#if 0
        for ( int j = 0; j < trees.size(); j++ )
            printf( "(%d,%d)\n", trees[j].first, trees[j].second );
#endif
        
#if 0
        for ( int i = 0; i < n; i++ ) for ( int j = i+1; j < n; j++ ) for ( int k = j+1; k < n; k++ ) {
            int sx = trees[i].first + trees[j].first + trees[k].first;
            int sy = trees[i].second + trees[j].second + trees[k].second;
            if ( sx % 3 == 0 && sy % 3 == 0 ) result ++;
        }
#else
        ll tr[3][3];
        REP(i,3) REP(j,3) tr[i][j] = 0LL;
        {
            ll x = x0, y = y0;
            tr[x%3][y%3] ++;
            trees.PB( make_pair( x, y ) );
            for ( int i = 1; i <= n-1; i++ ) {
                x = ( A * x + B ) % M;
                y = ( C * y + D ) % M;
                int x3 = x % 3;
                int y3 = y % 3;
                tr[x3][y3] ++;
            }
        }
        
#if 0
        REP(i,3) {
            cout << tr[i][0] << "," << tr[i][1] << "," << tr[i][2] << endl;
        }
#endif

#if 0
        for ( int i = 0; i < 9; i++ ) for ( int j = i; j < 9; j++ ) for ( int k = j; k < 9; k++ ) {
            int xi = i / 3;
            int yi = i % 3;
            int xj = j / 3;
            int yj = j % 3;
            int xk = k / 3;
            int yk = k % 3;
            int sx = xi + xj + xk;
            int sy = yi + yj + yk;
            if ( sx % 3 == 0 && sy % 3 == 0 ) {
                ll ni = tr[xi][yi];
                ll nj = tr[xj][yj];
                ll nk = tr[xk][yk];
                
            }
        }
#else
        for ( int mask = 0; mask < 262144; mask++ ) {
            ll t = 1;
            int sum = 0;
            for ( int pos = 0; pos < 9; pos++ ) {
                int m = 3 & (mask >> ( pos * 2 ) );
                sum += m;
            }
            if ( sum != 3 ) continue;
            int sumx = 0, sumy = 0;
            for ( int pos = 0; pos < 9; pos++ ) {
                int x = pos / 3;
                int y = pos % 3;
                int m = 3 & (mask >> ( pos * 2 ) );
                sumx += x * m;
                sumy += y * m;
            }
            if ( sumx % 3 || sumy % 3 ) continue;
            for ( int pos = 0; pos < 9; pos++ ) {
                int x = pos / 3;
                int y = pos % 3;
                int m = 3 & (mask >> ( pos * 2 ) );
                if ( m == 1 ) t *= select( tr[x][y], 1 );
                else if ( m == 2 ) t *= select( tr[x][y], 2 );
                else if ( m == 3 ) t *= select( tr[x][y], 3 );
            }
            result += t;
        }
#endif
#endif
        
        printf( "Case #%d: %lld\n", prob+1, result );
    }
    
    return 0;
}
