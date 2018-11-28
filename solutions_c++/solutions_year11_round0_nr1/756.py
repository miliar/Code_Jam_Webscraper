#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)


int main()
{
	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		vector <int> blue, orange, who;
		int  n, k;
		char s[5];
		scanf( "%d", &n );
		REP(_,n) {
			scanf( "%s %d", s, &k );
			if ( s[0] == 'B' ) {
				who.push_back(0);
				blue.push_back(k);
			}
			else {
				who.push_back(1);
				orange.push_back(k);
			}
		}
		int ans = 0, i = 0, a = 0, pa = 1, b = 0, pb = 1;
		while ( i < n ) {
			int ti = i;
			if      ( a < blue.size() && pa != blue[a] ) pa += blue[a] < pa ? -1 : 1;
			else if ( a < blue.size() && who[i] == 0 ) ti = i + 1, a++;;
			if      ( b < orange.size() && pb != orange[b] ) pb += orange[b] < pb ? -1 : 1;
			else if ( b < orange.size() && who[i] == 1 ) ti = i + 1, b++;
			i = ti;
			ans++;
		}
		printf( "Case #%d: %d\n", tcase, ans );
	}
	return 0;
}
