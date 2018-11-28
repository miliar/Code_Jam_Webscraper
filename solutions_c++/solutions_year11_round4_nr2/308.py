#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <cstdlib>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define VI vector<int>
#define pb push_back
#define VS vector<string>
int R, C, D;
VS a;

int x[505][505];
int y[505][505];
int m[505][505];

int main()
    {
    int TC;
    cin >> TC;
    FOR(tc, 0, TC)
        {
        cin >> R >>  C >> D; a.resize( R ) ;
        FOR( i, 0 , R )
            cin >> a[i];
        memset( x, 0 , sizeof( x ));
        memset( y, 0 , sizeof( y ));
        memset( m, 0 , sizeof( m ));
        
        FOR( i, 0, R ) 
            FOR( j, 0, C )
                {
                x[i+1][j+1] = x[i+1][j] + x[i][j+1] - x[i][j] + i*(a[i][j] - '0' );
                y[i+1][j+1] = y[i+1][j] + y[i][j+1] - y[i][j] + j*(a[i][j] - '0' );
                m[i+1][j+1] = m[i+1][j] + m[i][j+1] - m[i][j] + (a[i][j] - '0' );
                }

        int sol = -1;

        FOR( i, 0, R ) 
            FOR( j, 0, C ) 
                FOR(k, max(3,sol), 500)
                    if ( i - (k-1)/2 >= 0 && i + k/2 < R && j - (k-1)/2 >= 0 && j + k/2 < C )
                    {
                    int x1 = i - (k-1)/2;
                    int x2 = i + k/2;
                    int y1 = j - (k-1)/2;
                    int y2 = j + k/2;
                    int mx = x[x2+1][y2+1] - x[x1][y2+1] - x[x2+1][y1] + x[x1][y1];
                    int my = y[x2+1][y2+1] - y[x1][y2+1] - y[x2+1][y1] + y[x1][y1];
                    int M = m[x2+1][y2+1] - m[x1][y2+1] - m[x2+1][y1] + m[x1][y1];
                    
                    mx -= x1 * ( a[x1][y1] - '0' + a[x1][y2] - '0' );
                    mx -= x2 * ( a[x2][y1] - '0' + a[x2][y2] - '0' );
                    my -= y1 * ( a[x1][y1] - '0' + a[x2][y1] - '0' );
                    my -= y2 * ( a[x1][y2] - '0' + a[x2][y2] - '0' );
                    M -= ( a[x1][y1] - '0' + a[x1][y2] - '0' );
                    M -= ( a[x2][y1] - '0' + a[x2][y2] - '0' );

                    if ( k % 2 == 1 )
                        {
                        if ( M * i == mx && M*j == my )
                            sol = max( sol , k );
                        }
                    else {
                        if ( M * ( 2*i+1) == mx*2 && M*(2*j+1) == my*2 )
                            sol = max( sol, k );
                        }
                    }
        if ( sol == - 1 ) printf("Case #%d: IMPOSSIBLE\n",tc+1);
        else printf("Case #%d: %d\n",tc+1,sol);
        }
    //system("pause");
    return 0;
    }
