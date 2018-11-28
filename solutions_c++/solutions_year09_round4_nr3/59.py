#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <complex>
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

typedef complex<double> P;
int N, K;
int pp[128][32];

bool xx[128][128];

bool conflict(int i, int j)
{
    int pd = pp[i][0] - pp[j][0];
    if ( !pd ) return 1;
    forNF ( k, 1, K ) {
        int d = pp[i][k] - pp[j][k];
        if ( pd > 0 && d <= 0 ||
             pd < 0 && d >= 0 ) return 1;
    }
    return 0;
}

const int POW_3_16 = 43046721;
int cc[POW_3_16];

int go(const int cb[])
{
    int key = 0;
    int last_0 = -1, last_1 = -1;
    int nb[16];
    forN ( i, N ) {
        nb[i] = cb[i];
        key = key*3+cb[i];
        if ( cb[i] == 0 ) last_0 = i;
        if ( cb[i] == 1 ) last_1 = i;
    }
    //TR(A(cb,N)|last_0|last_1|key);
    int& ret = cc[key];
    if ( ret >= 0 ) return ret;
    if ( last_0 < 0 ) {
        return ret = 0;
    }
    if ( last_1 < 0 ) {
        nb[last_0] = 1;
        ret = 1 + go(nb);
    }
    else {
        ret = 999999999;
        forN ( i, N ) {
            if ( nb[i] == 0 ) {
                forN ( j, N ) {
                    if ( nb[j] == 1 && xx[i][j] ) goto bad;
                }
                nb[i] = 1;
                ret <?= go(nb);
                nb[i] = 0;
            bad:;
            }
        }
        forN ( i, N ) {
            if ( nb[i] == 1 ) nb[i] = 2;
        }
        ret <?= go(nb);
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
        cin >> N >> K >> skip_endl;
        forN ( i, N ) {
            forN ( j, K ) cin >> pp[i][j];
            cin >> skip_endl;
        }

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        forN ( i, N ) forN ( j, i ) {
            xx[i][j] = xx[j][i] = conflict(i, j);
        }

        //TR(N);
        memset(cc, -1, sizeof(cc));
        assert(N <= 16);
        int cb[16] = {};
        int out = go(cb);

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << out;
        cout << endl;
    }
}
