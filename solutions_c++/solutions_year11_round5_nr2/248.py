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

const int MAXN = 10000 + 100;

int n, cnt[MAXN];

int last[MAXN];
int cnt2[MAXN];

bool process(int i, int x) {
	forsn(j,i,i+x) if (cnt2[j] == 0) return false;

	forsn(j,i,i+x) cnt2[j]--;
	last[i+x]++;
	return true;
}


bool pos(int x) {
	copy(cnt,cnt+MAXN,cnt2);
	fill(last,last+MAXN,0);

	forn(i,MAXN) while (cnt2[i] && process(i,x));
	forn(i,MAXN) while (last[i]) {
		last[i]--;
		for (int j = i; j < MAXN && cnt2[j]; j++) cnt2[j]--;
	}
	forn(i,MAXN) if (cnt2[i]) return false;
	return true;
}


int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int ncas; cin >> ncas;
    forn(cas,ncas) {    	
    	cout << "Case #" << cas+1 << ": ";
    	cin >> n; fill(cnt,cnt+MAXN,0);
    	forn(_,n) { int x; cin >> x; cnt[x]++; }

    	int lo = 0, hi = n+1;
    	while (lo + 1 < hi) {
    		int mi = (lo + hi) / 2;
    		if (pos(mi)) lo = mi; else hi = mi;
    	}
    	cout << lo << endl;
    }
}
