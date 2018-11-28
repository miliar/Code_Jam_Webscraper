#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <climits>
#include <cstring>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

struct ww{
	double f, t, l;
};

bool operator<(const ww& w0, const ww& w1){
	return w0.f < w1.f;
}

double x, s, r, n;
double t;

bool equal(double a, double b){
	return fabs(a-b) < 1e-8;
}

double move(double d, double add = 0.0){
	double ti = d/(r+add);
	if(ti < t || equal(ti, t)){
		t -= ti;
	}else{
		ti = (d - (r+add)*t) / (s+add) + t;
		t = 0;
	}
	
	return ti;
}

bool used[1004];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;
	forn(p,T){
		cin >> x >> s >> r >> t >> n;
		vector<ww> walk(n);
		memset(used, 0, sizeof(used));
		
		forn(i, n)
			cin >> walk[i].f >> walk[i].t >> walk[i].l;
		sort(walk.begin(), walk.end());
		
		double ret = 0.0, pos = walk[0].f;
		
		ret += move(x-walk[n-1].t) + move(walk[0].f);
		forn(i, n-1)
			ret += move(walk[i+1].f - walk[i].t);
		
		forn(i, n){
			int mv = INT_MAX, index = 0;
			forn(j, n){
				if(!used[j] && walk[j].l < mv){
					mv = walk[j].l;
					index = j;
				}
			}
			
			used[index] = 1;
			ret += move(walk[index].t-walk[index].f, walk[index].l);
		}

		printf("Case #%i: %.9f\n", p+1, ret);
	}

	return 0;
}
