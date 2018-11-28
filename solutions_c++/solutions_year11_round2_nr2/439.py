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

#define MAXN 1100000
#define EPS 1.0E-8

int t,c, n;

double x[MAXN], d;

bool valid(double r) {
	double left = x[0]-r+d;
	forsn(i,1,n) {
		if 	(x[i]+r<left) return false;
		left = d+ max(x[i]-r,left);	
	}
	return true;
}

int main () {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	cin >> t;
	forn(caso,t) {
		cin >> c >> d;
		n = 0;
		forn(i,c) {
			double p;
			int v;
			cin >> p >> v;
			forn(j,v) x[n++] = p;	
		}
		
		sort(x,x+n);
			
		double mn = 0.0, mx = d*n+1000, mid = (mx+mx)*0.5;
		while(mx-mn > EPS) {
			mid = (mx+mn)*0.5;
			if (valid(mid))	mx = mid;
			else mn = mid;
		}
		cout << "Case #" << caso+1 << ": " << mid << endl;
	}

	return 0;
}
