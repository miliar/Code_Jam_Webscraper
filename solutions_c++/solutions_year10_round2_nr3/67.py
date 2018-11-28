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

const int MOD = 100003;
const int MAX = 512;
int cc[MAX][MAX];
int cc2[MAX][MAX];

int choose(int n, int k)
{
    if ( cc2[n][k] >= 0 ) return cc2[n][k];
    int r = 0;
    if ( !k || k == n ) {
        r = 1;
    }
    else {
        r = choose(n-1,k-1) + choose(n-1,k);
        r %= MOD;
    }
    return cc2[n][k] = r;
}

int go(int n, int k)
{
    if ( cc[n][k] >= 0 ) return cc[n][k];
    int r;
    if ( k == 1 ) {
        r = 1;
    }
    else {
        r = 0;
        forNF ( i, 1, k ) {
            if ( n-k < k-i ) continue;
            r += i64(go(k, i))*choose(n-k-1,k-i-1)%MOD;
            r %= MOD;
        }
    }
    return cc[n][k] = r;
}

int n;

int main(int argc, const char** argv)
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    int part_cases = 0;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    
    memset(cc, -1, sizeof(cc));
    memset(cc2, -1, sizeof(cc2));
    
    forN ( nc, num_cases ) {
        // parse input
        cin >> n >> skip_endl;

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        int out = 0;
        forNF ( i, 1, n ) {
            out += go(n, i);
        }
        out %= MOD;

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << out;
        cout << endl;
    }
}
