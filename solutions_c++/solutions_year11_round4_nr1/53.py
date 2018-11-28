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
        int X, S, R, T, N;
        cin >> X >> S >> R >> T >> N >> skip_endl;
        assert(X >= 1);
        assert(T >= 1);
        assert(1 <= S && S < R && R <= 100);
        assert(N >= 1);
        vector<pair<int, int> > ww(N+1);
        forN ( i, N ) {
            int B, E;
            cin >> B >> E >> ww[i].first >> skip_endl;
            assert(B < E);
            assert(ww[i].first >= 1 && ww[i].first <= 100);
            ww[i].second = E-B;
            X -= E-B;
            assert(X >= 0);
        }
        // error check
        if ( !cin ) { cout << "Error parsing input" << endl; return 1; }
        // main code

        ww[N].first = 0;
        ww[N].second = X;
        sort(ALL(ww));
        double rem = T;
        double total = 0;
        forN ( i, N+1 ) {
            int w = ww[i].first;
            int L = ww[i].second;
            double rt = double(L)/(w+R);
            double tr = min(rem, rt);
            rem -= tr;
            total += tr;
            double sL = L - tr*(w+R);
            total += sL/(w+S);
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << fixed << setprecision(9) << total;
        cout << endl;
    }
}
