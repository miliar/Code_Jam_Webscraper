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

int R, K, N;
VI gg;

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
        cin >> R >> K >> N >> skip_endl;
        gg.resize(N);
        forN ( i, N ) {
            cin >> gg[i];
        }
        cin >> skip_endl;

        // error check
        if ( !cin ) cout << "Error parsing input" << endl;
        // main code

        i64 out = 0;
        VI tt(N, -1);
        int p = 0;
        vector<i64> tout;
        forN ( t, R ) {
            tout.push_back(out);
            if ( tt[p] >= 0 ) {
                int pt = tt[p];
                int dt = pt - t;
                i64 dout = tout[pt] - out;
                int rem = R - t;
                out += rem / dt * dout;
                rem %= dt;
                out += tout[pt+rem]-tout[pt];
                break;
            }
            tt[p] = t;
            int s = 0;
            int c = 0;
            while ( c < N && s + gg[p] <= K ) {
                ++c;
                s += gg[p];
                if ( ++p == N ) p = 0;
            }
            out += s;
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << out;
        cout << endl;
    }
}
