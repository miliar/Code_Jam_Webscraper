#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <iterator>
#include <algorithm>

using namespace std;


#define MAXN 1000


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.in.out","w",stdout);
    int T,cases;
    cases = 1;
    cin >> T;
    while(T--)
    {
        int N;
        int W, L;
        int rs[MAXN] ;
        int p[MAXN] ;
        int x[MAXN], y[MAXN] ;
        cin >> N >> W >> L ;
        for ( int i=0; i < N ;++i ) {
            cin >> rs[i] ;
        }
        bool flag[MAXN];
        memset ( flag, 0, sizeof flag ) ;
        for ( int i=0;i<N;++i ) {
            int m = -1 ;
            for ( int j=0;j<N;++j ) {
                if ( !flag[j] ) {
                    if ( m == -1 ) m = j ;
                    else if ( rs[j] > rs[m] ) m = j ;
			}
		}
            p[i] = m;
            flag[m] = true;
        }
        int y_0 = 0 ;
        int x_0 = 0 ;
        int dy = -1 ;
        for ( int i=0;i<N;++i ) {
            int r = rs[p[i]] ;
            if ( x_0 == 0 ) {
                x[p[i]] = x_0, y[p[i]] = y_0 ;
                dy = r ;
                x_0 += r ;
            } else if ( x_0 + r <= W ) {
                x[p[i]] = x_0 + r ;
                y[p[i]] = y_0 ;
                x_0 += r*2 ;
            } else {
                y_0 += dy + r ;
                x[p[i]] = 0;
                y[p[i]] = y_0 ;
                x_0 = r ;
            }
        }
        printf( "Case #%d:", cases++ ) ;
        for ( int i=0;i<N;++i ) {
            printf ( " %d.0 %d.0", x[i], y[i] ) ;
        }
        printf( "\n" ) ;
    }
    return 0;
}
