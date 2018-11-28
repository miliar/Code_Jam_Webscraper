#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

const double eps = 1e-6;

inline bool okay(vector <double> &arr, double d, double t) {
	double last = -1e8;
	REP(i,arr.size()) {
		if ( last + d + eps >= arr[i] + t ) return false;
		last = max(arr[i]-t,last+d);
	}
	return true;
}

int main()
{
	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		vector <double> arr;
		int c, d;
		scanf( "%d %d", &c, &d );
		REP(_,c) {
			int p, v;
			scanf( "%d %d", &p, &v );
			REP(__,v) arr.push_back(p);
		}
		sort(arr.begin(),arr.end());
		double ans, L = 0, R = 1e20;
		REP(_,100) {
			double mid = (L + R) / 2;
			if ( okay(arr,d,mid) ) ans = mid, R = mid;
			else L = mid;
		}
		printf( "Case #%d: %.8lf\n", tcase, ans );
		fprintf( stderr, "Case #%d: %.8lf\n", tcase, ans );
	}
	return 0;
}
