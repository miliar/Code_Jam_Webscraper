// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 1010
using namespace std;
int num[N],vis[N];
int main()
{
	int t,cas=0;
	int n,i,j,len,ans;
	scanf("%d",&t);
	while ( t-- ) {
		scanf("%d",&n);
		for ( i=1; i<=n; i++ ) scanf("%d",num+i);
		ans=0;
		memset(vis,0,sizeof(vis));
		for ( i=1; i<=n; i++ ) {
			if ( vis[i] ) continue;
			len=0;
			for ( j=i; !vis[j]; j=num[j] ) {
				vis[j]=1;
				len++;
			}
			if ( len>1 ) ans+=len;
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
/*
2 3 1
1 2 3 1/6 * 1
1 3 2 1/6 * 3
2 1 3 1/6 * 3
2 3 1 XD
3 1 2 XD
3 2 1 1/6 * 3
10/6 * 3/2
5/2
*/
