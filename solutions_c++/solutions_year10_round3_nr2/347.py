#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int L, P, C;
__int64  binary[31];
__int64  bb[31];

int main(){
	int test;
	
	freopen("B.in", "r", stdin );
	freopen("b.txt", "w", stdout );
	
	for( int i= 0; i<= 30; ++i ) bb[i]= 1<<i;
	
	scanf("%d",&test );
	for( int te= 1; te<= test; ++te ){
		scanf("%d%d%d", &L, &P, &C );
		
		binary[0]= 1;
		for( int i= 1; i<= 30; ++i )
		binary[i]= binary[i-1]* C;
		
		
		int pos;
		for( int i= 0; i<= 30; ++i )
		if( (__int64)L * binary[i]>= P ){
			pos= i; break;
		}
		
		int ans= 0;
		for( int i= 0; i<= 30; ++i )
		if( bb[i]>= pos ) { ans= i; break; }
		
		printf("Case #%d: %d\n", te, ans );
	}
	
	return 0;
}
