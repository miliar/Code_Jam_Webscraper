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

const int
	MAXN = 10000 + 100,
	MAXL = 30;

int n, mask[MAXN][MAXL], desc[MAXN][MAXL], letters[MAXN], pos[MAXN][MAXL];
string w[MAXN];

void init() {
	forn(i,n) {
		letters[i] = 0;
		forn(j,MAXL) {
			mask[i][j] = 0;
			pos[i][j] = 0;
		}
	}
}

int p;
bool comp(int i, int j) { return desc[i][p] < desc[j][p]; }
bool eq(int i, int j) { return desc[i][p] == desc[j][p]; }

int ord[MAXN];
void binsort(int a, int b, int p) {
	if (p >= 27) return;

	::p = p; sort(ord+a,ord+b,comp);
//	forsn(i,a,b) cerr  << ord[i] << ' '; cerr << endl;

	for (int ai = a; ai < b; ) {
		::p = p;
		int bi; for (bi = ai; bi < b && eq(ord[bi],ord[ai]); bi++);
//		cerr << "ai,bi = " << ai << ' ' << bi << endl;

		int mask = 0;
		forsn(i,ai,bi) mask |= letters[ord[i]];
		forsn(i,ai,bi) pos[ord[i]][p] = mask;
		binsort(ai,bi,p+1);
		ai = bi;

	}

}

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int ncas; cin >> ncas;
    forn(cas,ncas) {    	
    	cout << "Case #" << cas+1 << ":";

    	int m;
    	cin >> n >> m;
    	init();

    	forn(i,n) {
    		string s; cin >> s; w[i] = s;
    		desc[i][0] = si(s);
    		forn(j,si(s)) {
    			int cid = s[j]-'a';
    			mask[i][cid] |= 1<<j;
    			letters[i] |= 1<<cid;
    		}
    	}

//    	cerr << mask[2]['t'-'a'] << ' ' << mask[3]['t'-'a'] << endl;


    	forn(i,m) {
    		string s; cin >> s;
    		forn(j,26) {
    			char c = s[j];
    			forn(k,n) desc[k][j+1] = mask[k][c-'a'];
    		}
//    		forn(k,n) { forn(j,27) cerr << desc[k][j] << ' '; cerr << endl; }
//    		cerr << endl;

    		forn(i,n) ord[i] = i;
    		binsort(0,n,0);

    		int maxP = -1, ind = -1;
    		forn(i,n) {
    			int p = 0;
    			forn(j,26) {
    				if (pos[i][j] & (1<<(s[j]-'a'))) {p++; } // cerr << s[j] << ' ' << w[i] << endl; }

    			}
    			p -= __builtin_popcount(letters[i]);

    			if (p > maxP) { maxP = p; ind = i; }
    		}
    		cout << ' ' << w[ind];
    	}

    	cout << endl;
    }
}
