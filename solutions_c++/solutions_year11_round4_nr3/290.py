// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 1000010
using namespace std;
typedef long long LL;
int pp[N],ps[N]={2},pk=1;
void make_p() {
	for ( int i=3; i<1000; i+=2 )
		if ( !pp[i] )
			for ( int j=i*i; j<N; j+=i+i )
				pp[j]=1;
	for ( int i=3; i<N; i+=2 )
		if ( !pp[i] ) ps[pk++]=i;
}
int cal( LL n, int p ) {
	int r=0;
	while ( n>=p ) {
		r++;
		n/=p;
	}
	return r;
}
LL sqr( LL x ) { return x*x; }
int main()
{
	make_p();
	int T,cas=0,i;
	LL n,ans;
	scanf("%d",&T);
	while ( T-- ) {
		scanf("%I64d",&n);
		ans=1;
		for ( i=0; i<pk && sqr(ps[i])<=n; i++ ) {
			ans+=cal(n,ps[i])-1;
			//printf("%d: %d\n",ps[i],cal(n,ps[i]));
		}
		if ( n==1 ) ans=0;
		printf("Case #%d: %I64d\n",++cas,ans);
	}
	return 0;
}
