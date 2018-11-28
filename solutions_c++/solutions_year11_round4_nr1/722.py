#include <cstdio>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

const double eps = 1e-9;

struct tdata { int b, e, w; };
bool operator < (const tdata &a, const tdata &b) { return a.b < b.b; }

struct segment { int b, e; double w; bool move; };
bool operator < (const segment &a, const segment &b) { return a.w - eps > b.w; }

int main()
{
	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		int    x, n;
		double s, r, t;
		tdata  arr[1005];
		scanf( "%d %lf %lf %lf %d", &x, &s, &r, &t, &n );
		REP(i,n) scanf( "%d %d %d", &arr[i].b, &arr[i].e, &arr[i].w );
		
		sort(arr,arr+n);
		priority_queue <segment> pq;

		int curr = 0;
		REP(i,n) {
			if ( curr != arr[i].b ) pq.push((segment){curr,arr[i].b,s,false});
			pq.push((segment){arr[i].b,arr[i].e,s+arr[i].w,true});
			curr = arr[i].e;
		}
		if ( curr != x ) pq.push((segment){curr,x,s,false});

		double ans = 0;
		while ( !pq.empty() ) {
			segment p = pq.top(); pq.pop();
			double len = p.e - p.b;
			if ( t < eps ) {
				ans += len / p.w;
				continue;
			}

			double run  = p.move ? r + p.w - s : r;
			double need = len / run;
			
			if ( t <= need + eps ) {
				double one = run * t;
				double two = len - one;
				ans += one / run + two / p.w;
				t = 0;
			}
			else {
				ans += need;
				t   -= need;
			}
		}
		
		printf( "Case #%d: %.9Lf\n", tcase, ans );
	}
	return 0;
}
