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

const int MAX = 2048;
int K;
char vv[MAX][MAX];

bool symmetric(int k, int i0, int j0)
{
    forNF ( i1, i0-k+1, i0+k ) {
        if ( unsigned(i1) >= unsigned(MAX) ) continue;
        forNF ( j1, j0-k+1, j0+k ) {
            if ( unsigned(j1) >= unsigned(MAX) ) continue;
            char c = vv[i1][j1];
            if ( c == ' ' ) continue;
            int i2 = 2*i0-i1;
            if ( unsigned(i2) < unsigned(MAX) &&
                 vv[i2][j1] != ' ' && vv[i2][j1] != c )
                return 0;
            int j2 = 2*j0-j1;
            if ( unsigned(j2) < unsigned(MAX) &&
                 vv[i1][j2] != ' ' && vv[i1][j2] != c )
                return 0;
        }
    }
    return 1;
}

int cost(int k)
{
    return k*k;
}

int main(int /*argc*/, const char** /*argv*/)
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    forN ( nc, num_cases ) {
        // parse input
        cin >> K >> skip_endl;
        memset(vv, ' ', sizeof(vv));
        assert(2*K-1 < MAX);
        forN ( i, 2*K-1 ) {
            string s = get_str();
            assert(s.size() == 2U*K-1-abs(i-K+1));
            copy(ALL(s), vv[i]);
            forN ( j, 2*K-1-abs(i-K+1) ) {
                if ( ((i+j+K)&1) && j >= abs(i-K+1) )
                    assert(vv[i][j] >= '0' && vv[i][j] <= '9');
                else
                    assert(vv[i][j] == ' ');
            }
        }

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        int out = 0;
        if ( !symmetric(K, K-1, K-1) ) {
            forN ( d, 2*K+1 ) {
                forN ( i, d ) {
                    if ( symmetric(K+d, K-1-d+i, K-1-i) ||
                         symmetric(K+d, K-1+i, K-1-d+i) ||
                         symmetric(K+d, K-1+d-i, K-1+i) ||
                         symmetric(K+d, K-1-i, K-1+d-i) ) {
                        out = cost(K+d) - cost(K);
                        goto done;
                    }
                }
            }
        done:;
        }

        // output
        cout << "Case #"<<nc+1<<": "<<out;
        cout << endl;
    }
}
