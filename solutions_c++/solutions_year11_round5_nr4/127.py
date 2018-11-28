// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#define N 200
using namespace std;
typedef long long LL;
char s[N];
char* bin_str( LL m ) {
	static char ret[N];
	int len=0;
	while ( m ) {
		ret[len++]='0'+(m&1);
		m>>=1;
	}
	ret[len]=0;
	reverse(ret,ret+len);
	return ret;
}
int main()
{
	int T,cas=0;
	LL n,msk,m;
	scanf("%d",&T);
	while ( T-- ) {
		scanf("%s",s);
		n=msk=0;
		for ( int i=0; s[i]; i++ ) {
			if ( s[i]=='1' ) n=n*2+1;
			else n=n*2;
			if ( s[i]!='?' ) msk=msk*2+1;
			else msk=msk*2;
		}
		for ( m=(LL)(sqrt(n)); ((m*m)&msk)!=n; m++ );
		printf("Case #%d: %s\n",++cas,bin_str(m*m));
	}
	return 0;
}
