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

/////////////////////////////////////////////////////////////////////////////

const int MAX_S = 512;
int R, C, D;
int ww[MAX_S][MAX_S];
int ss[MAX_S][MAX_S];
int ssr[MAX_S][MAX_S];
int ssc[MAX_S][MAX_S];

inline int get(const int ss[MAX_S][MAX_S], int r0, int c0, int re, int ce)
{
    return ss[re][ce]-ss[r0][ce]-ss[re][c0]+ss[r0][c0];
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
        cin >> R >> C >> D >> skip_endl;
        string s;
        forN ( r, R ) {
            cin >> s >> skip_endl;
            assert((int)s.size() == C);
            copy(ALL(s), ww[r]);
        }

        // error check
        if ( !cin ) {
            cout << "Error parsing input" << endl;
            return 1;
        }
        // main code
        forN ( r, R+1 ) ss[r][0] = ssr[r][0] = ssc[r][0] = 0;
        forN ( c, C+1 ) ss[0][c] = ssr[0][c] = ssc[0][c] = 0;
        forN ( r, R ) forN ( c, C ) {
            ss[r+1][c+1] = ss[r+1][c]+ss[r][c+1]-ss[r][c]+ww[r][c];
            ssr[r+1][c+1] = ssr[r+1][c]+ssr[r][c+1]-ssr[r][c]+ww[r][c]*r;
            ssc[r+1][c+1] = ssc[r+1][c]+ssc[r][c+1]-ssc[r][c]+ww[r][c]*c;
        }

        int max_K = 0;
        for ( int K = min(R, C); K>=3; --K ) {
            for ( int r0 = 0; r0+K <= R; ++r0 ) {
                for ( int c0 = 0; c0+K <= C; ++c0 ) {
                    int sum      = get(ss, r0, c0, r0+K, c0+K);
                    int sum_by_r = get(ssr, r0, c0, r0+K, c0+K);
                    int sum_by_c = get(ssc, r0, c0, r0+K, c0+K);
                    for ( int r = r0; r < r0+K; r += K-1 ) {
                        for ( int c = c0; c < c0+K; c += K-1 ) {
                            int w = ww[r][c];
                            sum -= w;
                            sum_by_r -= r*w;
                            sum_by_c -= c*w;
                        }
                    }
                    if ( sum_by_r*2 == (2*r0+K-1)*sum &&
                         sum_by_c*2 == (2*c0+K-1)*sum ) {
                        max_K = K;
                        goto found;
                    }
                }
            }
        }
    found:;

        // output
        cout << "Case #"<<nc+1<<": ";
        if ( max_K )
            cout << max_K;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }
}
