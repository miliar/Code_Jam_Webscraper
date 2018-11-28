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
#include <cfloat>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

int vs[204],c;
double d, ps[204];

bool equal(double a, double b){
	return fabs(a-b) < 1e-8;
}

bool puede(double t){
	double ult = ps[0] - t;
	
	forn(i, c) forn(j, vs[i]){
		if(i == 0 && j == 0) continue;
//		cout << ps[i] << endl;
		double yo, dist = fabs(ult+d - ps[i]);
//		cout << ult << " " << i << " " << j << " " << dist << endl;
		if(ult+d < ps[i]-t || equal(ult+d, ps[i]-t))
			yo = ps[i]-t;
		else if(dist > t && !equal(dist, t))
			return false;
		else{
//			cout << "fruteo" << endl;
			yo = ult+d;
		}
		
		ult = yo;
	}
	return true;
}

int main()
{
#ifdef _TAVO92_
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
#endif

	int t;
	cin >> t;
	forn(p,t){
		printf("Case #%i: ", p+1);
		cin >> c >> d;
		
		forn(i,c)
			cin >> ps[i] >> vs[i];
		
		double mi = 0.0, ma = DBL_MAX, mid, best = ma;
		
		while(!equal(mi, ma)){
			mid = (mi+ma)/2.0;
			
//			cout << mi << " " << ma << endl;
			
			if(puede(mid)){
				ma = mid;
				best = mid;
			}else
				mi = mid;
		}
//		cout << puede(2) << endl;
		cout << best << endl;
	}

	return 0;
}
