#include <cstdio>
#include <queue>
#include <numeric>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)


int main()
{
	int ncase;
	scanf( "%d", &ncase );
	FOR(tcase,1,ncase) {
		int n;
		int arr[2000];
		int cost[2000];
		scanf( "%d", &n );
		REP(i,1<<n) scanf( "%d", &arr[i] );
		REP(i,(1<<n)-1) scanf( "%d", &cost[i] );

		REP(i,1<<n) arr[i] = n - arr[i];
		int ans = 0;
		queue <pair<int,int> > q; q.push(make_pair(0,(1<<n)-1));
		while ( !q.empty() ) {	
			pair<int,int> p = q.front(); q.pop();
			if ( accumulate(arr+p.first,arr+p.second+1,0) != 0 ) {
				ans++;
				FOR(i,p.first,p.second) arr[i] = max(0,arr[i]-1);
				int mid = (p.first + p.second) / 2;
				q.push(make_pair(p.first,mid));
				q.push(make_pair(mid+1,p.second));
			}
		}
	
		printf( "Case #%d: %d\n", tcase, ans );
	}
	return 0;
}
