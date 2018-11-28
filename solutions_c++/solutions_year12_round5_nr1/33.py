// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#define SZ(x) ((int)(x).size())
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
using namespace std;
#define N 1010
int n,l[N],p[N],s[N];
bool cp( int a, int b ) {
	double ta=1.0/(1-0.01*p[b])*(l[b]+1.0*l[a]/(1-0.01*p[a]));
	double tb=1.0/(1-0.01*p[a])*(l[a]+1.0*l[b]/(1-0.01*p[b]));
	if ( fabs(ta-tb)<1e-9 ) return a<b;
	else return ta<tb;
}
int main()
{
	int t,cs=0;
	scanf("%d",&t);
	while ( t-- ) {
		scanf("%d",&n);
		for ( int i=0; i<n; i++ ) scanf("%d",l+i);
		for ( int i=0; i<n; i++ ) scanf("%d",p+i);
		for ( int i=0; i<n; i++ ) s[i]=i;
		sort(s,s+n,cp);
		printf("Case #%d:",++cs);
		for ( int i=0; i<n; i++ ) printf(" %d",s[i]);
		puts("");
	}
	return 0;
}
