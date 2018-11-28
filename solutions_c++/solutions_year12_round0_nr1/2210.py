#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <climits>

#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <deque>
#include <forward_list>

#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <cmath>

#include <utility>

using namespace std;

#define FOR(i,n1,n2) for(int i = n1; i < n2; ++i)
#define FORD(i,n1,n2) for(int i = n1; i >= n2; --i)
#define FORE(e,c) for(auto& e : c)
#define SZ(i) (int) i.size()
#define PB push_back
#define MT make_tuple
#define g(c,i) get<i>(c)

map<char,char> m;

int main() {
m[' ']=' ';
m['a']='y';
m['b']='h';
m['c']='e';
m['d']='s';
m['e']='o';
m['f']='c';
m['g']='v';
m['h']='x';
m['i']='d';
m['j']='u';
m['k']='i';
m['l']='g';
m['m']='l';
m['n']='b';
m['o']='k';
m['p']='r';
m['q']='z';
m['r']='t';
m['s']='n';
m['t']='w';
m['u']='j';
m['v']='p';
m['w']='f';
m['x']='m';
m['y']='a';
m['z']='q';
    int t;
    scanf("%d\n",&t);
    FOR(i,1,t+1) {
        cout << "Case #" << i << ": ";

        string s;
        getline(cin,s);
        FOR(j,0,SZ(s)) s[j]=m[s[j]];

        cout << s << endl;
    }
    /*
    while(t--) {
        string s,s2;
        getline(cin,s);
        getline(cin,s2);
        FOR(j,0,SZ(s)) {
            if (!m.count(s[j]) && m[s[j]] != s2[j])
                m[s[j]] = s2[j];
        }
    }
    FOR(i,'a','z'+1) {
        FORE(e,m) if (e.second==i) goto next;
        m['q'] = i;
        next:;
    }
    FORE(e,m) cout << "m['" << e.first << "']='" << e.second << "';" << endl;
    if (SZ(m)==27) cout << "OK" << endl;
    */
    return 0;
}

