#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

char a[105][20];
char b[50];
int len[105];

int main()
{
	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		printf( "Case #%d:", tcase );
		int n, m;
		scanf( "%d %d", &n, &m );
		REP(i,n) scanf( "%s", a[i] );
		REP(i,n) len[i] = strlen(a[i]);
		REP(_,m) {
			scanf( "%s", b );
			int cnt[105] = {0};
			REP(i,n) {
				int used = 0;
				int can  = n;
				bool ok[20] = {false};
				bool con[105]; memset(con,true,sizeof(con));
				bool udah[256] = {false};
				REP(k,n) if ( len[i] != len[k] ) con[k] = false, can--;
				REP(j,26) {
					if ( can == 1 ) break;
					bool go = false;
					REP(k,n) {
						if ( !con[k] ) continue;
						bool ada = false;
						REP(x,len[i]) if ( a[k][x] == b[j] ) ada = true;
						go = ada;
						if ( go ) break;
					}
					udah[b[j]] = true;
					bool hadoh = false;
					if ( go ) {
						bool ada = false;
						REP(x,len[i]) if ( a[i][x] == b[j] ) ok[x] = true, ada = true, hadoh = true;
						if ( !ada ) used++;
						REP(k,n) {
							bool masih = true;
							REP(x,len[k]) {
								if ( ok[x] && a[k][x] != a[i][x] ) masih = false;
								if ( !ok[x] && udah[a[k][x]] ) masih = false;
							}
							if ( con[k] && !masih ) con[k] = false, can--;
						}
						if ( !ada )
						REP(k,n) REP(x,len[k]) if ( a[k][x] == b[j] ) {
							if ( con[k] ) con[k] = false, can--;
						}
					}
					if ( can == 1 ) break;
				}
				cnt[i] = used;
			}
			
			int hi = 0;
			REP(i,n) if ( cnt[hi] < cnt[i] ) hi = i;
			printf( " %s", a[hi] );
		}
		puts( "" );
	}
	return 0;
}
