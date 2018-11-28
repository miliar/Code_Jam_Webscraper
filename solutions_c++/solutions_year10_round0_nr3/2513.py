#include <cstdio>
#include <cstring>
#include <numeric>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)

int main()
{
	int ncase;
	scanf( "%d", &ncase );
	FOR(tcase,1,ncase) {
		int r, k, n, arr[1005];
		scanf( "%d %d %d", &r, &k, &n );
		REP(i,n) scanf( "%d", &arr[i] );
		
		int all = accumulate(arr,arr+n,0);
		if ( all <= k ) {
			printf( "Case #%d: %d\n", tcase, all * r );
			continue;
		}

		bool used[100005] = {false};
		int  f[100005];
		int  c[100005];
		memset(f,-1,sizeof(f));
		memset(c,0,sizeof(c));
		f[0] = 0; used[0] = true;
		int x = 0, t = 0;
		while ( true ) {
			int p = 0;
			while ( p + arr[t % n] <= k ) p += arr[t % n], t++;
			c[x] = p;
			f[++x] = t % n;
			if ( used[t % n] ) break;
			used[t % n] = true;
		}
		
		int ans = 0, i = 0;
		while ( f[i] != t % n ) ans += c[i++], r--;
		int loop = -1, j = i;
		while ( f[j] != -1 ) j++, loop++;
		int sum = 0;
		FOR(x,i,j-1) sum += c[x];
		
		ans += (r / loop) * sum;
		r %= loop;
		FOR(x,i,j-1) {
			if ( r == 0 ) break;
			ans += c[x]; r--;
		}

		printf( "Case #%d: %d\n", tcase, ans );
	}
	return 0;
}
