#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

typedef long long LL;

const int maxn = 1005;

bool isp[maxn];
vector <int> p;
vector <pair<int,int> > f[maxn];

bool cover(int a, int b) {
	REP(i,f[a].size()) REP(j,f[b].size()) {
		if ( f[a][i].first == f[b][j].first ) {
			if ( f[a][i].second > f[b][j].second ) return true;
		}
	}
	return false;
}

int main()
{
	memset(isp,true,sizeof(isp));
	for ( int i = 2; i * i <= maxn; i++ ) if ( isp[i] )
		for ( int j = i * i; j <= maxn; j += i ) isp[j] = false;
	for ( int i = 2; i <= maxn; i++ ) if ( isp[i] ) p.push_back(i);

	for ( int i = 2; i <= maxn; i++ ) {
		int n = i;
		REP(j,p.size()) if ( n % p[j] == 0 ) {
			int a = p[j];
			int b = 0;
			while ( n % p[j] == 0 ) b++, n /= p[j];
			f[i].push_back(make_pair(a,b));
		}
	}

	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		int n, hi = 1, lo = 0;
		scanf( "%d", &n );
		if ( n == 1 ) lo = 1;
		int milo = lo;
		
		vector <int> seq, v;
		REP(i,p.size()) if ( p[i] <= n ) v.push_back(p[i]), seq.push_back(p[i]);
		REP(i,v.size()) {
			int a = p[i];
			do {
				bool found = false;
				REP(j,v.size()) if ( v[j] >= p[i] ) {
					if ( a * v[j] <= n ) seq.push_back(a*v[j]), found = true;
				}
				a *= p[i];
				if ( !found ) break;
			} while ( true );
		}

		vector <int> s;
		FOR(i,2,n) s.push_back(i);
		REP(i,s.size()) FOR(j,i+1,s.size()-1) if ( cover(s[i],s[j]) ) swap(s[i],s[j]);


		{
			int cnt[1000] = {0};
			REP(x,seq.size()) {
				int i = seq[x];
				bool call = false;
				REP(j,f[i].size()) if ( cnt[f[i][j].first] < f[i][j].second )
					cnt[f[i][j].first] = f[i][j].second, call = true;
				if ( call ) hi++;
			}
		}
		{
			int cnt[1000] = {0};
			FORD(x,seq.size()-1,0) {
				int i = seq[x];
				bool call = false;
				REP(j,f[i].size()) if ( cnt[f[i][j].first] < f[i][j].second )
					cnt[f[i][j].first] = f[i][j].second, call = true;
				if ( call ) lo++;
			}
		}
		{
			int cnt[1000] = {0};
			FORD(x,s.size()-1,0) {
				int i = s[x];
				bool call = false;
				REP(j,f[i].size()) if ( cnt[f[i][j].first] < f[i][j].second )
					cnt[f[i][j].first] = f[i][j].second, call = true;
				if ( call ) milo++;
			}
		}
		lo = min(lo,milo);
		printf( "Case #%d: %d\n", tcase, hi - lo );
		fprintf( stderr, "%d\n", tcase );
	}
	return 0;
}
