#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cctype>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <gmp.h>
#ifdef HOME_RUN
# include <debug.hpp>
# include <dump.hpp>
# include <cassert>
#else
# define TR(x) do{}while(0)
# ifdef assert
#  indef assert
# endif
# define assert(x) do{}while(0)
#endif
using namespace std;

#define ALL(C) (C).begin(), (C).end()
#define forIter(I,C) for(typeof((C).end()) I=(C).begin(); I!=(C).end(); ++I)
#define forNF(I,S,C) for(int I=(S); I<int(C); ++I)
#define forN(I,C) forNF(I,0,C)
#define forEach(I,C) forN(I,(C).size())
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long i64;
typedef unsigned long long u64;

inline istream& skip_endl(istream& in)
{
    string s;
    getline(in, s);
    forIter( i, s ) assert(isspace(*i));
    return in;
}

inline string get_str()
{
    string ret;
    getline(cin, ret);
    return ret;
}

map<string, int> str_index;
int get_index(const string& s)
{
    return str_index.insert(make_pair(s, str_index.size())).first->second;
}
int get_str_index()
{
    return get_index(get_str());
}

const int MAX_P = 10;
int P;
int mm[1<<MAX_P];
int tt[MAX_P+1][1<<MAX_P];
int cc[MAX_P+1][1<<MAX_P][1<<MAX_P];

int go(int r, int i0, int missed)
{
    int& cret = cc[missed][r][i0];
    if ( cret >= 0 ) return cret;
    if ( r == 0 ) {
        return cret = 0;
    }
    assert(tt[r][i0] >= 0);
    int im = i0 + (1<<r-1);
    int i1 = i0 + (1<<r);
    int ret = tt[r][i0] + go(r-1, i0, missed) + go(r-1, im, missed);
    bool can_miss = 1;
    forNF ( i, i0, i1 ) {
        if ( missed == mm[i] ) {
            can_miss = 0;
            break;
        }
    }
    if ( can_miss ) {
        ret <?= go(r-1, i0, missed+1) + go(r-1, im, missed+1);
    }
    return cret = ret;
}

int main(int argc, const char** argv)
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    int part_cases = 0;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        // parse input
        cin >> P >> skip_endl;
        forN ( i, 1<<P ) {
            cin >> mm[i];
        }
        cin >> skip_endl;
        memset(tt, -1, sizeof(tt));
        forNF ( r, 1, P+1 ) {
            for ( int i0 = 0; i0 < (1<<P); i0 += 1<<r ) {
                cin >> tt[r][i0];
            }
            cin >> skip_endl;
        }

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        memset(cc, -1, sizeof(cc));
        int out = go(P, 0, 0);

        // output
        cout << "Case #"<<nc+1<<": ";
        if ( out < 0 )
            cout << "IMPOSSIBLE";
        else
            cout << out;
        cout << endl;
    }
}
