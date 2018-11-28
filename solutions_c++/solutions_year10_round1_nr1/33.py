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

const int MAXN = 50 + 10;

int n,k;
char t[MAXN][MAXN], t2[MAXN][MAXN];

int check(const string& s, char c) {
	int len = si(s), racha = 0;
	forn(i,len) {
		if (s[i] == c) racha++;
		else racha = 0;
		if (racha >= k) return true;
	}
	return false;
}

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int ncas; cin >> ncas;
    forn(cas,ncas) {
    	cout << "Case #" << cas+1 << ": ";
    	cin >> n >> k;
    	forn(i,n) forn(j,n) cin >> t[i][j];

    	memset(t2,'.',sizeof t2);
    	forn(i,n) {
    		int p = n;
    		dforsn(j,0,n) if (t[i][j] != '.')
    			t2[i][--p] = t[i][j];
    	}

//    	forn(i,n) { forn(j,n) cout << t2[i][j]; cout << endl; }

    	int res = 0;
    	forn(i,n) {
    		string s,t;
    		forn(j,n) {
    			s += t2[i][j];
    			t += t2[j][i];
    		}
    		if (check(s,'R')) res |= 1;
    		if (check(t,'R')) res |= 1;
    		if (check(s,'B')) res |= 2;
    		if (check(t,'B')) res |= 2;
    	}

    	map<int,string> ss, sr;
    	forn(i,n) forn(j,n) {
    		ss[i+j] += t2[i][j];
    		sr[i-j] += t2[i][j];
    	}
    	forall(it,ss) {
    		if (check(it->second,'R')) res |= 1;
    		if (check(it->second,'B')) res |= 2;
    	}
    	forall(it,sr) {
			if (check(it->second,'R')) res |= 1;
			if (check(it->second,'B')) res |= 2;
		}

    	if (res == 0) cout << "Neither" << endl;
    	else if (res == 1) cout << "Red" << endl;
    	else if (res == 2) cout << "Blue" << endl;
    	else cout << "Both" << endl;
	}
    return 0;
}
