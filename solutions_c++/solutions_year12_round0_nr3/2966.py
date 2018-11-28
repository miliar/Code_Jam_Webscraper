#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

#define INPUT_FILE "C-small-attempt0.in"
#define OUTPUT_FILE "C-small-attempt0.out"

using namespace std;

int find_answer( long long a, long long b )
{
    stringstream ss( stringstream::in | stringstream::out );
    string s, k;
    long long tmp;
    int r = 0;
    bool dup;
    vector<long long> v;
    for ( long long i = a; i <= b; ++i )
    {
        v.clear();
        ss.clear();
        ss << i;
        ss >> s;
        for ( int p = 1; p < s.length(); ++p )
        {
            dup = false;
            k = s.substr( p, s.length() - 1 ) + s.substr( 0, p );
            ss.clear();
            ss << k;
            ss >> tmp;
            if ( i < tmp && tmp <= b )
            {
                for ( int j = 0; j < v.size(); ++j )
                    if ( tmp == v[j] )
                    {
                        dup = true;
                        break;
                    }
                if ( dup )
                    continue;
                v.push_back( tmp );
                ++r;
            }
        }
    }
    return r;
}

void main()
{
    ifstream fi( INPUT_FILE );
    ofstream fo( OUTPUT_FILE );

    int t;
    fi >> t;

    for ( int q = 1; q <= t; ++ q )
    {
        fo << "Case #" << q << ": ";

        long long a, b;
        fi >> a >> b;

        fo << find_answer( a, b );

        fo << endl;
    }

    fi.close();
    fo.close();
}
