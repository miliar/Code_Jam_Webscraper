#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int test;
	
//	freopen("A-large.in", "r", stdin );
//	freopen("b.txt", "w", stdout );
	
	scanf("%d",&test );
	for( int te= 1; te<= test; ++te ){
		int n, k;
		scanf("%d%d",&n,&k );
		
		int nn= 1<<n;
		k%= nn;
		
		printf("Case #%d: ", te );
		if( k== nn- 1 ) puts("ON");
		else puts("OFF");
	}
	
	return 0;
}
