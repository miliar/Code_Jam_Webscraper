#include <iostream>
#include <fstream>

#define INPUT_FILE "B-large.in"
#define OUTPUT_FILE "B-large.out"

using namespace std;

int get_base( int t )
{
    int r = 0;
    while ( (r + 1) * 3 <= t )
        ++r;
    return r;
}

void main()
{
    ifstream fi( INPUT_FILE, ios::in );
    ofstream fo( OUTPUT_FILE, ios::out );

    int T;
    fi >> T;

    for ( int q = 1; q <= T; ++q )
    {
        int n, s, p, t;
        int r = 0;

        fi >> n >> s >> p;

        for ( int i = 0; i < n; ++i )
        {
            fi >> t;
            int b = get_base( t );
            if ( b >= p )
            {
                ++r;
                continue;
            }
            t -= b * 3;
            if ( t > 0 && b + 1 >= p )
            {
                ++r;
                continue;
            }
            if ( t == 2 && b + 2 >= p && s > 0 )
            {
                ++r;
                --s;
                continue;
            }
            if ( b - 1 >= 0 && b + 1 >= p && s > 0 )
            {
                ++r;
                --s;
            }
        }

        // cout << "Case #" << q << ": " << r << endl;

        fo << "Case #" << q << ": " << r << endl;
    }

    fi.close();
    fo.close();

    // system( "pause" );
}