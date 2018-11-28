#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <numeric>
#include <complex>
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
typedef long long i64; typedef unsigned long long u64;
typedef vector<int> VI; typedef vector<VI> VVI; typedef vector<string> VS;

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

/////////////////////////////////////////////////////////////////////////////

const int MAX_N = 400;
VI ee[MAX_N];
u64 tt[MAX_N];
typedef pair<int, u64> P;

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
        int N, W;
        cin >> N >> W >> skip_endl;
        forN ( i, N ) {
            ee[i].clear();
            tt[i] = 1ULL<<i;
        }
        forN ( k, W ) {
            char c;
            int i, j;
            cin >> i >> c >> j;
            assert(c == ',');
            assert(unsigned(i) < unsigned(N));
            assert(unsigned(j) < unsigned(N));
            assert(i < j);
            ee[i].push_back(j);
            ee[j].push_back(i);
            tt[j] |= 1ULL<<i;
            tt[i] |= 1ULL<<j;
        }

        // error check
        if ( !cin ) {
            cout << "Error parsing input" << endl;
            return 1;
        }
        // main code

        int d = 0;
        set<P> ss, pps;
        ss.insert(P(0, tt[0]));
        if ( !(tt[0] & 2) ) {
            for ( ;; ) {
                u64 vv = 0;
                swap(ss, pps);
                ss.clear();
                ++d;
                forIter ( k, pps ) {
                    int i = k->first;
                    u64 t = k->second;
                    forIter ( j, ee[i] ) {
                        ss.insert(P(*j, t|tt[*j]));
                        vv |= tt[*j];
                    }
                }
                if ( vv & 2 ) break;
            }
        }

        int conq = d;
        //TR(d|conq|hex|ss);
        int max_threat = 0;
        forIter ( k, ss ) {
            u64 t = k->second;
            if ( t & 2 ) {
                int threat = 1-conq;
                forNF ( i, 2, N ) {
                    if ( t & (1ULL << i) )
                        ++threat;
                }
                assert(threat >= 1);
                if ( threat > max_threat )
                    max_threat = threat;
            }
        }
        
        // output
        cout << "Case #"<<nc+1<<": ";
        cout << conq << ' ' << max_threat;
        cout << endl;
    }
}
