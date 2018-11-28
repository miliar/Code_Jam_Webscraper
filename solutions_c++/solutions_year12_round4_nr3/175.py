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
#include <cstring>
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
typedef pair<int,int> pii;

#define MAXN 2048

int T,n,x[MAXN], h[MAXN];


void solve(int a, int b, int prof) {
//	cout << "solving " << a <<" " << b << " "<< prof << endl;
	if (b==a) return;
	h[a] = h[b]-prof*(b-a);
	int t = a;
	while(t!=b) {
		h[x[t]] = h[b] - prof*(b-x[t]);	
		solve(t+1,x[t],prof+1);
		t = x[t];
	}	
}

int main () {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	cin >> T;
	forn(rep,T) {
		cin >> n;
		forn(i,n-1) {cin >> x[i];	x[i]--;}
		
		bool sepuede = true;
		
		forn(i,n-1) forsn(j,i+1,x[i]) if (x[j] > x[i]) sepuede = false;
		
	//	cout << endl << sepuede << endl;
		cout << "Case #" << rep+1 << ":";
		if (!sepuede) cout << " Impossible" << endl;
		else {
			h[n-1] = 999999999;
			solve(0,n-1,0);
			forn(i,n) cout << " " << h[i];
			cout << endl;
		}	
	}

	return 0;
}
