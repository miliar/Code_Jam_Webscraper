#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
#include <cstring>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;

string in[4] = {
"ejp mysljylc kd kxveddknmc re jsicpdrysi"
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
"de kr kd eoya kw aej tysr re ujdr lkgc jv"
"y qeez"
};

string out[4] = {
"our language is impossible to understand"
"there are twenty six factorial possibilities"
"so it is okay if you want to just give up"
"a zooq"
};

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    map<char,char> translate;
    forn(i,4) forn(j,si(in[i])) {
    	translate[in[i][j]] = out[i][j];
    }
    D(si(translate))
    forall(it,translate) cerr << it->first << ' ' << it->second << endl;

    int ncas; cin >> ncas; scanf("\n");
    forn(cas,ncas) {    	
    	cout << "Case #" << cas+1 << ": ";
    	string s, res; getline(cin, s);
    	forn(i,si(s)) res += translate[s[i]];
    	cout << res << endl;

    }
}
