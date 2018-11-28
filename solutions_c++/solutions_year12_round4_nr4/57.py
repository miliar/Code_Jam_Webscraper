#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <cmath>
#include <numeric>
#include <complex>
#include <algorithm>
#include <functional>
#include <cctype>
#include <cstring>
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
typedef long long i64; typedef unsigned long long u64;
typedef vector<int> VI; typedef vector<VI> VVI; typedef vector<string> VS;

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

/////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////

const int MAX_N = 8;
const int MAX_D = 10;
int R, C;
struct Map {
    unsigned char r[MAX_N];
    void clear() { forN ( i, MAX_N ) r[i] = 0; }
    void set(int i, int j) {
        assert(i >= 0 && i < R);
        assert(j >= 0 && j < C);
        r[i] |= 1<<j;
    }
    bool get(int i, int j) const {
        assert(i >= 0 && i < R);
        assert(j >= 0 && j < C);
        return (r[i] & (1<<j)) != 0;
    }
    bool operator<(const Map& m) const { return memcmp(r, m.r, R) < 0; }
    int size() const {
        int ret = 0;
        forN ( i, R ) {
            unsigned c = r[i];
            assert((c & -(1<<C))==0);
            ret += __builtin_popcount(c);
        }
        return ret;
    }
    bool empty_above(int i) const { forNF ( j, i+1, R ) if ( r[j] ) return 0; return 1; }
    bool inside(const Map& ms) const { forN ( j, R ) if ( r[j] & ~ms.r[j] ) return 0; return 1; }
};
ostream& operator<<(ostream& out, const Map& m)
{
    forN ( i, R ) {
        out << '\n';
        forN ( j, C ) out << ".#"[m.get(i, j)];
    }
    return out << '\n';
}
Map m;
int rr[MAX_D], cc[MAX_D];
int dc[MAX_D];
bool dl[MAX_D];

int fill(Map& ms, int i, int j)
{
    if ( m.get(i, j) ) return 0;
    if ( ms.get(i, j) ) return 0;
    ms.set(i, j);
    int ret = 1;
    if ( j > 0 ) ret += fill(ms, i, j-1);
    if ( j < C-1 ) ret += fill(ms, i, j+1);
    if ( i > 0 ) ret += fill(ms, i-1, j);
    return ret;
}

set<Map> vv;
deque<Map> qq;

inline unsigned left(unsigned m, unsigned m0)
{
    m <<= 1;
    m0 <<= 1;
    m0 |= 1;
    unsigned r = ((m>>1)&~m0) | (((m>>1)&m0)<<1);
    r >>= 1;
    return r;
}

inline unsigned right(unsigned m, unsigned m0)
{
    m0 |= -(1<<C);
    unsigned r = ((m<<1)&~m0) | (((m<<1)&m0)>>1);
    return r;
}

Map left(const Map& ms)
{
    Map mr;
    forN ( i, R ) mr.r[i] = left(ms.r[i], m.r[i]);
    return mr;
}

Map right(const Map& ms)
{
    Map mr;
    forN ( i, R ) mr.r[i] = right(ms.r[i], m.r[i]);
    return mr;
}

Map down(const Map& ms)
{
    Map mr;
    mr.clear();
    forN ( i, R ) {
        unsigned r = ms.r[i];
        if ( i == R-1 ) {
            mr.r[i] |= r;
        }
        else {
            unsigned x = m.r[i+1];
            mr.r[i] |= r & x;
            mr.r[i+1] |= r & ~x;
        }
    }
    return mr;
}

bool check(int d, const Map& ms)
{
    assert(ms.empty_above(rr[d]));
    if ( ms.size() == 1 ) {
        assert(ms.get(rr[d], cc[d]));
        return 1;
    }
    vv.clear();
    qq.clear();
    vv.insert(ms);
    qq.push_back(ms);
    while ( !qq.empty() ) {
        const Map& m0 = qq.front();
        {
            Map m = left(m0);
            assert(m.size());
            if ( m.size() == 1 ) {
                return 1;
            }
            if ( vv.insert(m).second ) qq.push_back(m);
        }
        {
            Map m = right(m0);
            assert(m.size());
            if ( m.size() == 1 ) {
                return 1;
            }
            if ( vv.insert(m).second ) qq.push_back(m);
        }
        {
            Map m = down(m0);
            assert(m.size());
            if ( m.inside(ms) ) {
                if ( m.size() == 1 ) {
                    return 1;
                }
                if ( vv.insert(m).second ) qq.push_back(m);
            }
        }
        qq.pop_front();
    }
    return 0;
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
        R -= 2;
        C -= 2;
        assert(R > 0);
        assert(C > 0);
        {
            m.clear();
            forN ( i, MAX_D ) rr[i] = -1;
            string r;
            cin >> r >> skip_endl;
            assert(r == string(C+2, '#'));
            forN ( i, R ) {
                cin >> r >> skip_endl;
                assert(r.size() == C+2u);
                assert(r[0] == '#');
                assert(r[C+1] == '#');
                forN ( j, C ) {
                    char c = r[j+1];
                    assert(c == '#' || c == '.' || isdigit(c));
                    if ( c == '#' )
                        m.set(i, j);
                    if ( isdigit(c) ) {
                        rr[c-'0'] = i;
                        cc[c-'0'] = j;
                    }
                }
            }
            cin >> r >> skip_endl;
            assert(r == string(C+2, '#'));
        }

        forN ( d, MAX_D ) {
            if ( rr[d] < 0 ) break;
            Map ms;
            ms.clear();
            assert(ms.size() == 0);
            dc[d] = fill(ms, rr[d], cc[d]);
            assert(ms.size() == dc[d]);
            dl[d] = check(d, ms);
        }
        
        // output
        cout << "Case #"<<nc+1<<":";
        cout << endl;
        forN ( d, MAX_D ) {
            if ( rr[d] < 0 ) break;
            cout << d << ": " << dc[d] << " " << (dl[d]? "Lucky": "Unlucky") << endl;
        }
    }
}
