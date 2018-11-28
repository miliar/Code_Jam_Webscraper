#include <cstdio>
#include <map>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)

int s, q;
char line[200];

int main()
{
	int ncase;
	scanf( "%d\n", &ncase );

	FOR(tcase,1,ncase) {
		map <string,int> m;
		set <int> all;

		scanf( "%d%*[^\n]%*[\n]", &s );
		FOR(i,1,s) {
			gets(line);
			m[line] = i;
			all.insert(i);
		}

		int ans = 0;
		set <int> can = all;

		scanf( "%d%*[^\n]%*[\n]", &q );
		FOR(i,1,q) {
			gets(line);
			int id = m[line];
			if ( can.find(id) != can.end() ) {
				if ( can.size() == 1 ) can = all, ans++;
				can.erase(can.find(id));
			}
		}

		printf( "Case #%d: %d\n", tcase, ans );
	}
	
	return 0;
}
