#include <iostream>
#include <fstream>
#include <string>
using	namespace	std;

string	ep, pat;
int		N;
int		opt[510][20];

int		main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int		len = 19;
    pat = "welcome to code jam";
    cin >> N; getline(cin, ep);
    for( int i = 0; i < N; i ++ )
    {
        getline(cin, ep);
        int		Len = ep.length();
        memset( opt, 0, sizeof( opt ) );
        for( int k = 0; k < len; k ++ )
        for( int j = 0; j < Len; j ++ )
        {
            if( j == 0 ) opt[j][k] = 0; else opt[j][k] = opt[j - 1][k];
            if( ep[j] == pat[k] )
            {
                if( k == 0 ) opt[j][k] ++; else if( j == 0 ) opt[j][k] = 0; else
                (opt[j][k] += opt[j - 1][k - 1]) %= 10000;
            }
        }
        printf( "Case #%d: %04d\n", i + 1, opt[Len - 1][len - 1] );
    }
}

