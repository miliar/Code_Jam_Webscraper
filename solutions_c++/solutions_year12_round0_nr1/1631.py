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

char g[] = "abcdefghijklmnopqrstuvwxyz";
char e[] = "    o           z       aq";

char bg[] =
    "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    "de kr kd eoya kw aej tysr re ujdr lkgc jv";
char be[] =
    "our language is impossible to understand"
    "there are twenty six factorial possibilities"
    "so it is okay if you want to just give up";

int main(int argc, const char** argv)
{
    int num_cases = 1;
    cin >> num_cases >> skip_endl;
    int part_cases = 0;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( i, 999 ) {
        if ( !be[i] ) {
            assert(!bg[i]);
            break;
        }
        if ( be[i] == ' ' ) {
            assert(bg[i] == ' ' );
            continue;
        }
        int k = bg[i] - 'a';
        assert(k >= 0 && k < 26);
        char c = be[i];
        assert(e[k] == ' ' || e[k] == c);
        e[k] = c;
    }
    TR(string(e,26));

    forN ( nc, num_cases ) {
        string s = get_str();
        
        // error check
        if ( !cin ) { cout << "Error parsing input" << endl; return 1; }

        // main code
        forEach ( i, s ) if ( s[i] != ' ' ) s[i] = e[s[i]-'a'];

        // output
        cout << "Case #"<<nc+1<<": ";
        cout << s;
        cout << endl;
    }
}
