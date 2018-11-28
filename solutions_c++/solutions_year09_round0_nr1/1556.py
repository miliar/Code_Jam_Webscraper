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

int L, D, N;
char ww[5000][16];

int main()
{
    int num_cases = 1;
    //cin >> num_cases >> skip_endl;
    forN ( nc, num_cases ) {
        cin>>L>>D>>N;
        forN ( i, D ) cin >> ww[i];
        cin>>skip_endl;
        if ( !cin ) { cout << "failed read" << endl; return 1; }

        int w[16];
        forN ( i, N ) {
            forN ( j, L ) {
                char c;
                cin >> c;
                int b = 0;
                if ( c == '(' ) {
                    do {
                        b |= 1<<(c-'a');
                        cin >> c;
                    } while ( c != ')' );
                }
                else {
                    b = 1<<(c-'a');
                }
                w[j] = b;
            }
            cin >> skip_endl;

            int count = 0;
            forN ( k, D ) {
                bool match = 1;
                forN ( j, L )
                    if ( !(w[j] & (1<<(ww[k][j]-'a'))) ) {
                        match = 0;
                        break;
                    }
                count += match;
            }
            cout << "Case #"<<i+1<<": "<<count;
            cout << endl;
        }
    }
}
