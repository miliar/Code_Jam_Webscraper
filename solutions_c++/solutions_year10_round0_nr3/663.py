// by shik
// it can be solved in O(n)
// but i'm lazy =P
#include <iostream>
using namespace std;
int main()
{
	long long t,T,r,k,n,g[1000],nxt[1000],len[1000],sum[1000],val[1000],vis[1000],cyc[1000],i,j,L,s;
	long long ans;
	scanf("%I64d",&T);
	for ( t=1; t<=T; t++ ) {
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		for ( i=0; i<n; i++ ) scanf("%I64d",g+i);
		for ( i=0; i<n; i++ ) {
			s=g[i];
			for ( j=(i+1)%n; j!=i&&s+g[j]<=k; j=(j+1)%n ) s+=g[j];
			nxt[i]=j;
			val[i]=s;
		}
		memset(cyc,0,sizeof(cyc));
		for ( i=0; i<n; i++ ) {
			memset(vis,0,sizeof(vis));
			for ( j=i; !vis[j]; j=nxt[j] ) vis[j]=1;
			if ( i==j ) cyc[i]=1;
		}
		for ( i=0; i<n; i++ ) {
			if ( !cyc[i] ) continue;
			s=val[i]; L=1;
			for ( j=nxt[i]; j!=i; j=nxt[j],L++ ) s+=val[j];
			len[i]=L;
			sum[i]=s;
		}
		ans=i=0;
		while ( r>0 ) {
			if ( !cyc[i] || (cyc[i]&&r<len[i]) ) {
				ans+=val[i];
				i=nxt[i];
				r--;
			} else {
				ans+=sum[i]*(r/len[i]);
				r%=len[i];
			}
		}
		printf("Case #%I64d: %I64d\n",t,ans);
	}
	return 0;
}
