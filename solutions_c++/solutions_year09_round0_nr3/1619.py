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

const char w[] = "welcome to code jam";
const int W = 19;
int N;
char s[512];
int cc[512][32];
const int MOD = 10000;

int go(int p, int k)
{
    if ( s[p] != w[k] ) return 0;
    if ( k == 18 ) return 1;
    if ( cc[p][k] >= 0 ) return cc[p][k];
    int ret = 0;
    forNF ( j, p+1, N ) ret += go(j, k+1);
    return cc[p][k] = ret % MOD;
}

int main()
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    forN ( nc, num_cases ) {
        string str = get_str();
        N = str.size();
        copy(ALL(str), s);

        memset(cc, -1, sizeof(cc));
        int count = 0;
        forN ( i, N ) count += go(i, 0);
        count %= MOD;
        cout << "Case #"<<nc+1<<": ";
        cout<<setfill('0')<<setw(4)<<count;
        cout<<endl;
    }
}
