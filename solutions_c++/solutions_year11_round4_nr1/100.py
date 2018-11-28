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
typedef double tipo;

#define MAXN 1024

int T,n;

tipo r,s, t, x;
pair<tipo,tipo> w[MAXN];


int main () {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	cin >> T;
	forn(rep,T) {
		cin >> x >> s >> r >> t >> n;	
		tipo resto = x;
		r-=s;
		forn(i,n) {
			tipo u,v; cin >> u >> v >> w[i].first;
			w[i].second = v-u;	
			resto-= (v-u);
			w[i].first+= s;
		}
		w[n].second = resto;
		w[n].first = s; 
		
		n++;
		
	//	forn(i,n) cout << w[i].first << " " << w[i].second << endl;
		
		sort(w,w+n);
		
		tipo ans = 0.0;
		
		for(int i = 0; i<n; i++) {
			tipo d = min(w[i].second,t*(w[i].first+r));
			tipo timerun = d/(w[i].first+r);
			ans += timerun; t-= timerun;
			tipo timenormal = (w[i].second-d)/w[i].first;
			ans += timenormal;
		}
		cout << "Case #" << rep+1 << ": ";
		printf("%.8f\n",ans);
	}

	
	return 0;
}
