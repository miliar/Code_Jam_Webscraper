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
typedef long long i64; typedef unsigned long long u64;
typedef vector<int> VI; typedef vector<VI> VVI; typedef vector<string> VS;
typedef pair<int, int> P; typedef vector<P> VP; typedef vector<VP> VVP;

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

const int MAX_N = 1000000;
int sieve[MAX_N+1];

VI pp;

void init_pp()
{
    fill_n(sieve, MAX_N+1, 0);
    for ( int p = 2; p <= MAX_N; ++p ) {
        if ( !sieve[p] ) {
            pp.push_back(p);
            for ( int x = p*2, y = 2; x <= MAX_N; x += p, ++y ) {
                sieve[x] = 1;
            }
        }
    }
}

int main(int argc, const char** argv)
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    int part_cases = 0;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }

    init_pp();
    
    forN ( nc, num_cases ) {
        // parse input  
        i64 N;
        cin >> N >> skip_endl;

        // error check
        if ( !cin ) { cout << "Error parsing input" << endl; return 1; }
        // main code
        
        int spread = 0;
        if ( N > 1 ) {
            spread = 1;
            forIter ( i, pp ) {
                int p = *i;
                i64 x = i64(p)*p;
                if ( x > N ) break;
                do {
                    ++spread;
                } while ( (x*=p) <= N );
            }
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << spread;
        cout << endl;
    }
}
