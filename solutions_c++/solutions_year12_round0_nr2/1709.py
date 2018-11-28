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

inline istream& skip_endl(istream& in = cin)
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


const int INF = 999999999;
const int MAX_N = 128;
int N, S, p;
VI ss;
int cc[MAX_N][MAX_N];
int can[31][2];

int go(int N, int S)
{
    int& ret = cc[N][S];
    if ( ret != -1 ) return ret;
    if ( S > N ) ret = -INF;
    else if ( N == 0 ) ret = 0;
    else {
        int s = ss[N-1];
        ret = go(N-1, S) + can[ss[N-1]][0];
        if ( S && can[s][1] >= 0 )
            ret = max(ret, go(N-1, S-1) + can[s][1]);
    }
    return ret;
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
        cin >> N >> S >> p;
        ss.resize(N);
        forN ( i, N ) cin >> ss[i];
        skip_endl();

        // error check
        if ( !cin ) {
            cout << "Error parsing input" << endl;
            return 1;
        }
        // main code

        memset(cc, -1, sizeof(cc));
        memset(can, -1, sizeof(can));
        forN ( s, 31 ) {
            forN ( s1, 11 ) forN ( s2, 11 ) {
                int s3 = s-s1-s2;
                if ( s3 < 0 || s3 > 10 ) continue;
                if ( abs(s1-s2) > 2 ) continue;
                if ( abs(s1-s3) > 2 ) continue;
                if ( abs(s2-s3) > 2 ) continue;
                int surp = 0;
                if ( abs(s1-s2) == 2 ) surp = 1;
                if ( abs(s1-s3) == 2 ) surp = 1;
                if ( abs(s2-s3) == 2 ) surp = 1;
                can[s][surp] = max(can[s][surp], max(s1, max(s2, s3)) >= p? 1: 0);
            }
        }
        int ret = go(N, S);

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << ret;
        cout << endl;
    }
}
