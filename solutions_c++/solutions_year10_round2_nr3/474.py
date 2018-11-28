#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int n;
const int mod = 100003;
int order[501];
int cache[501][501];

bool isok( int x ) {
	if( x == 1 ) return true;
	if( order[ x ] <= 0 ) return false;
	return isok( order[x] );
}

/*
 * Diagonal sums of the "postage stamp" array: for rows n >= -1, column m >= 0 is given by F(n,m)=F(n-1,m)+F(n-2,m)+...+F(n-m,m) with F(0,m)=1 (m >= 0), F(n,m)=0 (n<0) and F(n,0)=0 (n>0). (Rows indicate the required sum, columns indicate the integers available {0,...,m}, entries F(n,m) indicate number of ordered ways sum can be achieved (eg n=3, m=2: 3=1+1+1=1+2=2+1 so F(3,2)=3 ways)).
 */

int f(int x, int y) {
	if( x == 0 && y >= 0 ) return 1;
	if( x < 0 ) return 0;
	if( x > 0 && y == 0 ) return 0;
	int &ret = cache[x][y];
	if( ret != -1 ) return ret;
	ret = 0;
	for(int i=x-1;i>=max(x-y,-1);--i) {
		ret = ( ret + f(i,y) ) % mod;
	}
	return ret;
}
int main() {
	int tn;
	scanf("%d", &tn);
	memset( cache, -1, sizeof cache );
	for(int cc=1;cc<=tn;++cc) {
		scanf("%d", &n);

		int ret = 0;

		for(int i=-1;i<=n;++i) {
			ret = ( f( i, n-1-i ) + ret ) % mod;
		}
		printf("Case #%d: %d\n", cc, ret );
	}	
}
