#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
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

const int MAX_N = 128;
int N;
char cc[MAX_N+1];

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
        cin >> cc >> skip_endl;
        N = strlen(cc);

        // error check
        if ( !cin ) {
            cout << "Error parsing input" << endl;
            return 1;
        }
        // main code

        int M = count(cc, cc+N, '?');
        i64 ret = -1;
        forN ( bb, 1<<M ) {
            i64 v = 0;
            int rbb = bb;
            forN ( i, N ) {
                char c = cc[i];
                if ( c == '?' ) {
                    c = rbb&1;
                    rbb >>= 1;
                }
                v <<= 1;
                v |= c&1;
            }
            int x = int(__builtin_sqrtl((long double)v)+.1);
            i64 x2 = x*i64(x);
            if ( x2 > v ) {
                --x;
                x2 = x*i64(x);
            }
            if ( x2 == v ) {
                ret = v;
                TR(bb|ret);
                break;
            }
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        forN ( i, N ) cout << char(((ret >> (N-1-i))&1)+'0');
        cout << endl;
    }
}
