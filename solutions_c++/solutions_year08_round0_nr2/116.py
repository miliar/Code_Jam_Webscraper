#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

typedef pair<int,int> pii;
typedef pair<pii,int> pipii;

int main()
{
	int ncase;
	scanf( "%d", &ncase );

	FOR(tcase,1,ncase) {
		int T, na, nb;
		scanf( "%d %d %d", &T, &na, &nb );

		vector <pipii> v;

		int a, b, c, d;
		REP(i,na+nb) {
			scanf( "%d:%d %d:%d", &a, &b, &c, &d );
			v.push_back(make_pair(pii(a*60+b, c*60+d),i>=na));
		}

		sort(v.begin(),v.end());
		
		int train[2][2405] = { 0 };
		REP(i,v.size()) {
			train[ v[i].second][v[i].first.first]--;
			train[!v[i].second][v[i].first.second + T]++;
		}
		
		int ans[2] = { 0 };
		REP(i,2) REP(j,2400) train[i][j] += train[i][j-1];
		REP(i,2) REP(j,2400) ans[i] = min(ans[i], train[i][j]);

		printf( "Case #%d: %d %d\n", tcase, -ans[0], -ans[1] );
	}
	
	return 0;
}
