#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

typedef long long LL;
const int max_n = 1005;
int rank[max_n], pr[max_n];
int link(int x, int y) {
	if ( rank[x] == rank[y] ) rank[x]++;
	if ( rank[x] > rank[y] ) pr[y] = x; else pr[x] = y;
}
int find(int x) {
	if ( x != pr[x] ) pr[x] = find(pr[x]);
	return pr[x];
}

bool isp[max_n + 5];
vector <int> v;
void sieve() {
	memset(isp,true,sizeof(isp));
	isp[0] = isp[1] = false;
	for ( int i = 2; i < max_n/i; i++ ) if ( isp[i] ) 
		for ( int j = i+i; j < max_n; j+=i ) isp[j] = false;
	for ( int i = 0; i < max_n; i++ ) if ( isp[i] ) v.push_back(i);
}

int main()
{
	int ncase;
	scanf( "%d", &ncase );

	sieve();

	FOR(tcase,1,ncase) {
		int a, b, p;
		scanf( "%d %d %d", &a, &b, &p );
		REP(i,max_n) rank[i] = 0, pr[i] = i;

		int ans = b - a + 1;
		REP(i,v.size()) if ( v[i] >= p ) {
			int x = (a + v[i] - 1) / v[i] * v[i];
			FOR(j,a,b) if ( j % v[i] == 0 )  {
				if ( find(x-a) != find(j-a) ) {
					link(find(x-a),find(j-a));
					ans--;
				}
			}
		}

		printf( "Case #%d: %d\n", tcase, ans );
	}
	
	return 0;
}
