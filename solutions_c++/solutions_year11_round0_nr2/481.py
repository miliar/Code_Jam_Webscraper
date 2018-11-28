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

const int MAXC = 255;

int n;
string s;
char comb[MAXC][MAXC];
bool opose[MAXC][MAXC];
vector<char> res;

void init() {
	fill(comb[0],comb[MAXC],-1);
	fill(opose[0],opose[MAXC],false);
	res.clear();
}


void push(char c) {
	char cmb;
	if (res.empty() || (cmb = comb[c][res.back()]) == -1) {
		forn(i,si(res)) if (opose[c][res[i]]) {
			res.clear();
			return;
		}
		res.pb(c);
	}
	else {
		res.pop_back();
		res.pb(cmb);
	}
}

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int ncas; cin >> ncas;
    forn(cas,ncas) {    	
    	cout << "Case #" << cas+1 << ": ";
    	init();

    	int c; cin >> c; forn(_,c) {
    		string x; cin >> x;
    		comb[x[0]][x[1]] = comb[x[1]][x[0]] = x[2];
    	}

    	int d; cin >> d; forn(_,d) {
    		string x; cin >> x;
    		opose[x[0]][x[1]] = opose[x[1]][x[0]] = true;
    	}

    	cin >> n >> s;
    	forn(i,n) push(s[i]);

    	cout << '[';
    	forn(i,si(res)) {
    		if (i) cout << ", ";
    		cout << res[i];
    	}
    	cout << ']' << endl;

    }
}
