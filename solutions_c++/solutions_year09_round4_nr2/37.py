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

int R, C, F;

char b[64][64];

const int INF = 999999999;
int cc[64][64][128];

inline int drop(int r, int c)
{
    while ( b[r+1][c] == '.' ) ++r;
    return r;
}

int go(int r, int c, int xx)
{
    assert(b[r+1][c] == '#');
    int& ret = cc[r][c][xx+64];
    if ( ret >= 0 ) return ret;
    if ( r == R-1 ) {
        return ret = 0;
    }
    ret = INF;
    int c1 = c, c2 = c;
    if ( xx < 0 ) c1 += xx;
    if ( xx > 0 ) c2 += xx;
    while ( b[r][c1-1] == '.' ) --c1;
    while ( b[r][c2+1] == '.' ) ++c2;
    int m1 = c;
    int m2 = c;
    while ( m1 > c1 && b[r+1][m1-1] == '#' ) --m1;
    while ( m2 < c2 && b[r+1][m2+1] == '#' ) ++m2;
    TR(r|c|xx|c1|c2|m1|m2);
    if ( m1 > c1 ) {
        int r1 = drop(r, m1-1);
        TR(r1);
        if ( r1 <= r+F ) ret <?= go(r1, m1-1, 0);
    }
    if ( m2 < c2 ) {
        int r1 = drop(r, m2+1);
        TR(r1);
        if ( r1 <= r+F ) ret <?= go(r1, m2+1, 0);
    }
    forNF ( d1, m1, m2+1 ) forNF ( d2, d1, m2+1 ) {
        if ( m1 < d1 ) {
            int r1 = drop(r+1, d1);
            TR(m1|m2|r1);
            if ( r1 <= r+F ) ret <?= d2-d1+1+go(r1, d1, r1==r+1? d2-d1: 0);
            TR(ret);
        }
        if ( m2 > d2 ) {
            int r1 = drop(r+1, d2);
            TR(m1|m2|r1);
            if ( r1 <= r+F ) ret <?= d2-d1+1+go(r1, d2, r1==r+1? d1-d2: 0);
            TR(ret);
        }
    }
    return ret;
}

int main()
{
    //init_table();
    
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    
    forN ( nc, num_cases ) {
        // parse input
        cin >> R >> C >> F >> skip_endl;
        forN ( r, R ) {
            b[r][0] = '#';
            string s = get_str();
            assert((int)s.size() == C);
            copy(ALL(s), b[r]+1);
            b[r][C+1] = '#';
            b[r][C+2] = 0;
        }
        memset(b[R], '#', sizeof(b[R]));
        b[R][C+2] = 0;
        forN ( r, R+1 ) {
            TR(b[r]);
        }
        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        memset(cc, -1, sizeof(cc));

        int out = go(0, 1, 0);

        // output
        cout << "Case #"<<nc+1<<": ";
        if ( out == INF ) cout << "No";
        else cout << "Yes " << out;
        cout << endl;
    }
}
