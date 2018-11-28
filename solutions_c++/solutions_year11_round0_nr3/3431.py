#include <stdio.h>

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T,a[1000];
	scanf("%d",&T);
	for ( int t =0; t<T; t++){
		int n,small=999999999,all=0;
		scanf("%d",&n);
		for ( int i=0; i<n; i++ ){
			scanf("%d",&a[i]);
			if ( a[i]<small ) small = a[i];
			all += a[i];
		}	
		int bit = a[0];
		for ( int i=1; i<n; i++ ){
			bit = bit^a[i];
		}
		if ( bit!=0 ){
			printf("Case #%d: NO\n",t+1);
		}
		else{
			printf("Case #%d: %d\n",t+1,all-small);
		}
	}
	return 0;
}
