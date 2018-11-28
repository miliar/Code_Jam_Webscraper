#include<stdio.h>

int main()
{
	freopen("snap.in","r",stdin);
	freopen("snap.out","w",stdout);
	
	int t,n,k;
	
	scanf("%d",&t);
	
	for( int i=1; i<=t; ++i) {
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i);
		if( k%(1<<n)==(1<<n)-1 )
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
