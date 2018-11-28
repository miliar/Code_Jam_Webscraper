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
#include <cstring>
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

/////////////////////////////////////////////////////////////////////////////

const int MAX_N = 1024;
const int MAX_V = 10240;
int N;
map<int, int> vv;
int vc[MAX_V];
int rc[MAX_V];
int ac[MAX_V];

bool good(int m)
{
    copy(vc, vc+MAX_V, rc);
    fill_n(ac, MAX_V, 0);
    //TR(m|A(vc, 20));
    forNF ( i, 1, MAX_V ) {
        if ( vc[i] > vc[i-1] ) {
            int c = vc[i]-vc[i-1];
            forN ( j, m ) {
                rc[i+j] -= c;
                if ( rc[i+j] < 0 ) return 0;
            }
            ac[i+m] = c;
        }
    }
    //TR(A(rc, 20));
    //TR(A(ac, 20));
    int c = 0;
    forN ( i, MAX_V ) {
        c += ac[i];
        if ( c > rc[i] ) c = rc[i];
        if ( c < rc[i] ) return 0;
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
        cin >> N;
        vv.clear();
        forN ( i, N ) {
            int v;
            cin >> v;
            assert(v >= 1 && v <= MAX_V);
            vv[v] += 1;
        }

        // error check
        if ( !cin ) {
            cout << "Error parsing input" << endl;
            return 1;
        }
        // main code

        int ret;
        if ( !N ) {
            ret = 0;
        }
        else {
            memset(vc, 0, sizeof(vc));
            forIter ( i, vv ) {
                vc[i->first] += i->second;
            }
            int a = 1, b = MAX_N+1;
            while ( a < b-1 ) {
                int m = (a+b)>>1;
                bool g = good(m);
                //TR(m|g);
                if ( g )
                    a = m;
                else
                    b = m;
            }
            ret = a;
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << ret;
        cout << endl;
    }
}
