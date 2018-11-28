#include <iomanip>
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
#define D(a) cout << #a << "=" << a << endl;
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
typedef vector<pii> vpii;

#define MAXD 5002
#define MAXL 20
#define MAXC 30
int L,D;
string w[MAXD];
bool good[MAXL][MAXC];

void readToken(int i) {
	char c; cin >> c;
	if (c == '(') for (;;) {
		cin >> c; if (c == ')') return;
		good[i][c-'a'] = true;
	}
	good[i][c-'a'] = true;
}

bool match(int i) {
	string& word = w[i];
	forn(ind,L) if (!good[ind][word[ind]-'a']) return false;
	return true;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int ncas;
	cin >> L >> D >> ncas;
	forn(i,D) cin >> w[i];

	forsn(cas,1,ncas+1) {
		memset(good,0,sizeof good);
		forn(i,L) readToken(i);
		int res = 0;
		forn(i,D) res += match(i);
		cout << "Case #" << cas << ": " << res << endl;
	}
}
