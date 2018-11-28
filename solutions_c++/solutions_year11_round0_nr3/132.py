// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 1010
using namespace std;
int c[N];
int main()
{
	int t,cas=0;
	int n,i,sum,ans;
	scanf("%d",&t);
	while ( t-- ) {
		scanf("%d",&n);
		for ( i=0; i<n; i++ ) scanf("%d",c+i);
		sum=0;
		for ( i=0; i<n; i++ ) sum^=c[i];
		if ( sum!=0 ) {
			printf("Case #%d: NO\n",++cas);
			continue;	
		}
		sort(c,c+n);
		ans=0;
		for ( i=1; i<n; i++ ) ans+=c[i];
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
