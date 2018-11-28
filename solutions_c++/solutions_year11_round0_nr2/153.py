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

vector<string> cc;
vector<string> dd;

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
        cc.clear();
        dd.clear();
        int C;
        cin >> C;
        forN ( i, C ) {
            string s;
            cin >> s;
            assert(s.size() == 3);
            cc.push_back(s);
        }
        cin >> C;
        forN ( i, C ) {
            string s;
            cin >> s;
            assert(s.size() == 2);
            dd.push_back(s);
        }
        string inv;
        cin >> C >> inv >> skip_endl;
        assert((int)inv.size() == C);

        // error check
        if ( !cin ) {
            cout << "Error parsing input" << endl;
            return 1;
        }
        // main code
        
        vector<char> cur;
        forIter ( i, inv ) {
            cur.push_back(*i);
        repeat:
            if ( cur.size() >= 2 ) {
                char c1 = cur.end()[-1];
                char c2 = cur.end()[-2];
                forIter ( i, cc ) {
                    const string& s = *i;
                    if ( s[0] == c1 && s[1] == c2 || s[0] == c2 && s[1] == c1 ) {
                        cur.pop_back();
                        cur.back() = s[2];
                        goto repeat;
                    }
                }
                forIter ( i, dd ) {
                    const string& s = *i;
                    if ( c1 == s[0] && find(cur.begin(), cur.end()-1, s[1]) != cur.end()-1 ||
                         c1 == s[1] && find(cur.begin(), cur.end()-1, s[0]) != cur.end()-1 ) {
                        cur.clear();
                        break;
                    }
                }
            }
        }

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << "[";
        forEach ( i, cur ) {
            if ( i ) cout << ", ";
            cout << cur[i];
        }
        cout << "]";
        cout << endl;
    }
}
