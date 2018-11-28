#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

const int maxn = 2005;

int main()
{
	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		fprintf( stderr, "%d\n", tcase );
		int  n, m;
		int  u[maxn], v[maxn];
		bool w[maxn][maxn] = {false};
		scanf( "%d %d", &n, &m );
		REP(i,m) scanf( "%d", &u[i] );
		REP(i,m) scanf( "%d", &v[i] );
		REP(i,m) w[u[i]][v[i]] = w[v[i]][u[i]] = true;
		FOR(i,1,n-1) w[i][i+1] = w[i+1][i] = true;
		w[1][n] = w[n][1] = true;

		vector <int> room[maxn];
		int nr = 0;
		REP(bit,1<<n) {
			if ( __builtin_popcount(bit) < 3 ) continue;
			vector <int> p;
			bool in[maxn] = {false};
			REP(i,n) if( bit & (1 << i) )
				p.push_back(i+1), in[i+1] = true;;

			bool okay = true;

			bool con[maxn][maxn] = {false};
			FOR(i,1,n) FOR(j,1,n) if ( in[i] && in[j] && w[i][j] ) con[i][j] = true;
			FOR(k,1,n) FOR(i,1,n) FOR(j,1,n) if ( in[i] && in[j] && in[k] )
				con[i][j] |= con[i][k] & con[k][j];
			FOR(i,1,n) FOR(j,1,n) if ( in[i] && in[j] && !con[i][j] ) okay = false;

			int deg[maxn] = {0};
			FOR(i,1,n) FOR(j,1,n) if ( in[i] && in[j] && w[i][j] ) deg[i]++;
			FOR(i,1,n) if ( in[i] && deg[i] != 2 ) okay = false;

			int nwall = 0;
			FOR(i,1,n) FOR(j,i+1,n) if ( in[i] && in[j] && w[i][j] ) nwall++;
			if ( nwall != p.size() ) okay = false;

			if ( okay ) room[nr++] = p;
		}

		printf( "Case #%d: ", tcase );
		if ( nr == 1 ) {
			printf( "%d\n", n );
			FOR(i,1,n) printf( "%d%c", i, i==n?'\n':' ' );
		}
		else {
			int ans = 0;
			REP(i,nr) ans = max(ans,(int)room[i].size());
			while ( ans != 0 ) {
				int limit = 1; REP(_,n) limit *= ans;
				REP(bit,limit) {
					int col[maxn] = {0};
					int t = bit;
					FOR(i,1,n) col[i] = t % ans, t /= ans;

					bool okay = true;
					REP(i,nr) {
						bool ok[maxn] = {false};
						REP(j,room[i].size()) ok[col[room[i][j]]] = true;
						REP(j,ans) if ( !ok[j] ) okay = false;
						if ( !okay ) break;
					}
					
					if ( okay ) {
						printf( "%d\n", ans );
						int t = bit;
						FOR(i,1,n) printf( "%d%c", col[i] + 1, i==n?'\n':' ' );
						goto done;
					}				
				}
				ans--;
			}
		}
		done: ;
	}
	return 0;
}
