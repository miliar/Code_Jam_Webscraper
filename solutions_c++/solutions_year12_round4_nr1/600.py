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


const int MAX_N = 20000;
int N, D;
int xx[MAX_N];
int ll[MAX_N];
int ww[MAX_N];

int main(int argc, const char** argv)
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    int part_cases = 0;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        cin >> N >> skip_endl;
        assert(N < MAX_N);
        forN ( i, N ) {
            cin >> xx[i] >> ll[i] >> skip_endl;
            ww[i] = 0;
        }
        cin >> D >> skip_endl;
        
        // error check
        if ( !cin ) { cout << "Error parsing input" << endl; return 1; }

        // main code
        bool reach = false;
        ww[0] = xx[0];
        forN ( i, N ) {
            int x = xx[i], w = ww[i];
            if ( x+w >= D ) { reach = 1; break; }
            forNF ( j, i+1, N ) {
                if ( xx[j] > x+w ) break;
                ww[j] = max(ww[j], min(ll[j], xx[j]-x));
            }
        }


        // output
        cout << "Case #"<<nc+1<<": ";
        cout << (reach? "YES": "NO");
        cout << endl;
    }
}
