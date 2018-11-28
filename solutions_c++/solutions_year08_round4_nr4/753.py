#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)

const int inf = 0x7fffffff;

int  k;
char s[100000];
char t[100000];

int eval(string x) {
	int ret = 1;
	REP(i,x.size()-1) if ( x[i] != x[i+1] ) ret++;
	return ret;
}

int main()
{
	int ncase;
	scanf( "%d", &ncase );

	FOR(tcase,1,ncase) {
		scanf( "%d %s", &k, s );
		vector <int> v;
		REP(i,k) v.push_back(i);
		int ans = inf;
		do {
			REP(i,strlen(s)) t[i] = s[(i/k*k)+v[i%k]];
			t[strlen(s)] = 0;
			ans = min(ans, eval(t) );
		} while ( next_permutation(v.begin(),v.end()) );
		printf( "Case #%d: %d\n", tcase, ans );
	}
	
	return 0;
}
