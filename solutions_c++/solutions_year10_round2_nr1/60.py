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

int N, M;
set<string> dd;
set<string> dc;

int main(int argc, const char** argv)
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    forN ( nc, num_cases ) {
        // parse input
        cin >> N >> M >> skip_endl;
        dd.clear();
        dc.clear();
        string d;
        forN ( i, N ) {
            cin >> d >> skip_endl;
            dd.insert(d);
        }
        forN ( i, M ) {
            cin >> d >> skip_endl;
            dc.insert(d);
        }

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        if ( (int)dd.size() != N || (int)dc.size() != M ) cout << "Dups" << endl;
        // main code

        int out = 0;
        forIter ( i, dc ) {
            d = *i + '/';
            forEach ( j, d ) {
                if ( j && d[j] == '/' ) {
                    string s = d.substr(0, j);
                    if ( dd.insert(s).second )
                        ++out;
                }
            }
        }

        // output
        cout << "Case #"<<nc+1<<": "<<out;
        cout << endl;
    }
}
