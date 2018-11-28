#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct point{
	int x, y;
};

int n;
point pnt[1010];

int main(){
	int test;
	
	freopen("A.in", "r", stdin );
	freopen("b.txt", "w", stdout );
	
	scanf("%d",&test );
	for( int te= 1; te<= test; ++te ){
		scanf("%d",&n );
		
		for( int i= 1; i<= n; ++i ){
			scanf("%d%d", &pnt[i].x, &pnt[i].y );
		}
		
		int ans= 0;
		for( int i= 1; i<= n; ++i ){
			for( int j= i+ 1; j<= n; ++j )
			if( ( pnt[i].x- pnt[j].x )* ( pnt[i].y- pnt[j].y )< 0 ) ans++;
		}
		
		printf("Case #%d: ", te );
		printf("%d\n", ans );
	}
	
	return 0;
}
