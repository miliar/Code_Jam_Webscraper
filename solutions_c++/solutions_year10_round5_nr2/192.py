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

i64 L, N;
int bb[100];

// binary gcd
template<typename T>
T gcd(T a, T b)
{
    if ( a < 0 ) a = -a;
    if ( b < 0 ) b = -b;
    int s = 0;
    while ( a&&b ) {
        if ( a&b&1 ) {
            if ( a > b )
                a -= b;
            else
                b -= a;
        }
        if ( !((a|b)&1) ) ++s;
        if ( !(a&1) ) a >>= 1;
        if ( !(b&1) ) b >>= 1;
    }
    return (a|b)<<s;
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
        cin >> L >> N >> skip_endl;
        forN ( i, N ) {
            cin >> bb[i];
        }
        cin >> skip_endl;

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        i64 out = -1;
        int g = bb[0];
        forN ( i, N ) g = gcd(g, bb[i]);
        if ( L % g == 0 ) {
            L /= g;
            forN ( i, N ) bb[i] /= g;
            sort(bb, bb+N);
            static const int MAX = 100000;
            static unsigned cc[MAX];
            fill(cc, cc+MAX, ~1u);
            cc[0] = 0;
            forN ( i, N ) {
                int b = bb[i];
                for ( int v = b; v < MAX; ++v )
                    cc[v] <?= cc[v-b] + 1;
            }
            forN ( i, MAX ) {
                if ( i > L ) break;
                if ( cc[i] == ~1u ) continue;
                i64 o0 = cc[i];
                i64 r = L-i;
                if ( r ) {
                    forN ( j, N ) {
                        int b = bb[j];
                        if ( r % b ) continue;
                        i64 o1 = o0 + r/b;
                        if ( out < 0 || o1 < out ) {
                            TR(L|i|o0|r|j|b|o1);
                            out = o1;
                        }
                    }
                }
            }
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        if ( out < 0 )
            cout << "IMPOSSIBLE";
        else
            cout << out;
        cout << endl;
    }
}
