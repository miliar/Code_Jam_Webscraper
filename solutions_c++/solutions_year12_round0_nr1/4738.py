#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename T> T abs(T a) { return a < 0 ? -a : a; }
template<typename T> T sqr(T a) { return a*a; }

const int INF = (int)1e9;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

map<char, char> r, d;

int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "rt", stdin);
        //freopen("output.txt", "wt", stdout);
    #endif

    /*
    r['y'] = 'a';
    r['e'] = 'o';
    r['q'] = 'z';

    d['a'] = 'y';
    d['e'] = 'o';
    d['z'] = 'q';

    string a, b;
    getline(cin, a);
    getline(cin, b);

    forn(i, sz(a)){
        if(isalpha(a[i])){
            r[a[i]] = b[i];
            d[b[i]] = a[i];
        }
    }

    for(char c = 'a'; c <= 'z'; ++c){
        if(!r.count(c))
            cerr << "r " << c << endl;
        if(!d.count(c))
            cerr << "d " << c << endl;
        printf("r[\'%c\']=\'%c\';\n", c, r[c]);
    } 
    */

    r['a']='y';
    r['b']='h';
    r['c']='e';
    r['d']='s';
    r['e']='o';
    r['f']='c';
    r['g']='v';
    r['h']='x';
    r['i']='d';
    r['j']='u';
    r['k']='i';
    r['l']='g';
    r['m']='l';
    r['n']='b';
    r['o']='k';
    r['p']='r';
    r['q']='z';
    r['r']='t';
    r['s']='n';
    r['t']='w';
    r['u']='j';
    r['v']='p';
    r['w']='f';
    r['x']='m';
    r['y']='a';
    r['z']='q';

    int n;
    string s;

    cin >> n;
    getline(cin, s);

    forn(i, n){
        getline(cin, s);
        printf("Case #%d: ", i + 1);

        forn(j, sz(s)){
            if(isalpha(s[j]))
                printf("%c", r[s[j]]);
            else
                printf("%c", s[j]);
        }
        puts("");
    }

    return 0;
}
