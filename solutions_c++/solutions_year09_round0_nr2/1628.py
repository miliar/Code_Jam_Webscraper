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

int I, J;
int mm[128][128];
int nb;
int ll[128][128];

const int DI[4] = { -1, 0, 0, 1 };
const int DJ[4] = { 0, -1, 1, 0 };

int go(int i0, int j0)
{
    if ( ll[i0][j0] >= 0 ) return ll[i0][j0];
    int bi = -1, bj = -1, bm = mm[i0][j0];
    forN ( d, 4 ) {
        int i = i0 + DI[d];
        int j = j0 + DJ[d];
        if ( unsigned(i) >= unsigned(I) || unsigned(j) >= unsigned(J) || mm[i][j] >= bm )
            continue;
        bm = mm[i][j];
        bi = i;
        bj = j;
    }
    return ll[i0][j0] = bi < 0? nb++: go(bi, bj);
}

int main()
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    forN ( nc, num_cases ) {
        cin>>I>>J;
        cin>>skip_endl;
        forN ( i, I ) {
            forN ( j, J ) {
                cin >> mm[i][j];
            }
            cin >> skip_endl;
        }
        if ( !cin ) { cout << "failed read" << endl; return 1; }

        memset(ll, -1, sizeof(ll));
        nb = 0;
        forN ( i, I ) forN ( j, J ) {
            if ( ll[i][j] < 0 ) go(i, j);
        }
        cout << "Case #"<<nc+1<<":"<<endl;
        forN ( i, I ) {
            forN ( j, J ) {
                if ( j ) cout << ' ';
                cout << char('a'+ll[i][j]);
            }
            cout << endl;
        }
    }
}
