#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <numeric>
#include <cstring>

using namespace std;

#define ll          long long
#define VI          vector<int>
#define ALL(a)      (a).begin(), (a).end()
#define SORT(a)     sort( ALL(a) )
#define PB          push_back
#define FOR(i,a,b)  for( int i = (a); i < (int)(b); i++ )
#define dump_(x)     cerr << #x << " = " << (x) << " ";
#define dump(x)     cerr << #x << " = " << (x) << endl
#define dump_vec(x) FOR(zZz,0,x.size()) cout << x[zZz] << " "; cout << endl


template< typename type > type readOne()
{
    type res;
    char inp[5000];
    char* dum = fgets( inp, sizeof( inp ), stdin );
    stringstream ss( dum );
    ss >> res;
    return res;
}

template< typename type > vector<type> readMulti()
{
    vector<type> res;
    char inp[5000];
    char* dum = fgets( inp, sizeof( inp ), stdin );
    stringstream ss( dum );
    for ( type t; ss >> t; )
        res.push_back( t );
    return res;
}

//
//
// LET'S START
//
//

string doCase()
{
    int C, D;
    cin >> C;
    vector<string> bases( C );
    FOR( i, 0, C )
        cin >> bases[i];
    cin >> D;
    vector<string> opposed( D );
    FOR( i, 0, D )
        cin >> opposed[i];
    int N;
    cin >> N;
    string str;
    cin >> str;

    string res;
    FOR( i, 0, N ) {
        if ( res.size() > 0 ) {
            int idx = -1;
            FOR( j, 0, C ) {
                if ( ( bases[j][0] == res[res.size() - 1] && bases[j][1] == str[i] ) ||
                     ( bases[j][0] == str[i] && bases[j][1] == res[res.size() - 1] ) ) {
                    idx = j;
                    break;
                }
            }
            if ( idx >= 0 )
                res[res.size() - 1] = bases[idx][2];
            else {
                bool op = false;
                FOR( j, 0, D ) {
                    FOR( k, 0, res.size() ) {
                        if ( ( opposed[j][0] == str[i] && opposed[j][1] == res[k] ) ||
                             ( opposed[j][1] == str[i] && opposed[j][0] == res[k] ) ) {
                            op = true;
                            break;
                        }
                    }
                }
                if ( op ) {
                    res = "";
                }
                else
                    res += str[i];
            }
        }
        else {
            res += str[i];
        }
    }

    stringstream ss;
    ss << "[";
    FOR( i, 0, res.size() ) {
        if ( i > 0 ) ss << ", ";
        ss << res[i];
    }
    ss << "]";
    return ss.str();
}

int main()
{
    int cases = readOne<int>();
    for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;
    return 0;
}

