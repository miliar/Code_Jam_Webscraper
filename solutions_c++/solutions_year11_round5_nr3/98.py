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
#include <cstring>
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
typedef long long i64; typedef unsigned long long u64;
typedef vector<int> VI; typedef vector<VI> VVI; typedef vector<string> VS;
typedef pair<int, int> P; typedef vector<P> VP; typedef vector<VP> VVP;

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

const int MAX_S = 128;
const int MOD = 1000003;
int R, C;
char cc[MAX_S][MAX_S];
bool dir[MAX_S][MAX_S];

inline int normalize(int r, int R)
{
    if ( r < 0 ) return r+R;
    if ( r >= R ) return r-R;
    return r;
}

pair<int, int> get_dst(int r, int c)
{
    int dr, dc;
    switch ( cc[r][c] ) {
    case '|': dr = 1; dc = 0; break;
    case '-': dr = 0; dc = 1; break;
    case '\\': dr = 1; dc = 1; break;
    case '/': dr = 1; dc = -1; break;
    default: abort();
    }
    if ( dir[r][c] ) {
        dr = -dr;
        dc = -dc;
    }
    return make_pair(normalize(r+dr, R),
                     normalize(c+dc, C));
}

bool good_in(int r0, int c0)
{
    int cnt = 0;
    forNF ( dr, -1, 2 ) forNF ( dc, -1, 2 ) {
        if ( dr == 0 && dc == 0 ) continue;
        pair<int, int> dst = get_dst(normalize(r0+dr, R),
                                     normalize(c0+dc, C));
        if ( dst.first == r0 && dst.second == c0 ) {
            if ( ++cnt > 1 ) return 0;
        }
    }
    return cnt == 1;
}

bool good(int bb)
{
    forN ( r, R ) forN ( c, C ) {
        dir[r][c] = bb & 1;
        bb >>= 1;
    }
    forN ( r, R ) forN ( c, C ) {
        if ( !good_in(r, c) ) return 0;
    }
    return 1;
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
        cin >> R >> C >> skip_endl;
        forN ( i, R ) {
            cin >> cc[i] >> skip_endl;
            assert((int)strlen(cc[i]) == C);
        }
        
        // error check
        if ( !cin ) { cout << "Error parsing input" << endl; return 1; }
        // main code
        
        int ret = 0;
        int M = R*C;
        forN ( bb, 1<<M ) {
            if ( good(bb) ) {
                ++ret;
                if ( ret == MOD ) ret = 0;
            }
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << ret;
        cout << endl;
    }
}
