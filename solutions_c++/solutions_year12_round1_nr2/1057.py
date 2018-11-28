#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<string>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;

#define MAX 1005

int test_case;
int N;
//int star[ MAX ][ 2 ];
bool taken[ MAX ][ 2 ];


struct info {
	int a;
	int b ;
} star[ MAX ] ;

bool cmp( struct info var1, struct info var2 ) {
	return var1.b < var2.b ;
}


int main(){
	freopen("B-large.in", "r", stdin);
	freopen("out1.txt", "w", stdout);
	int i;
    scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		scanf("%d", &N);
		for( i = 0; i < N; i ++ ) scanf("%d %d", &star[ i ].a , &star[ i ].b );
		memset( taken, false, sizeof( taken ) ) ;
		sort( star, star + N, cmp );
		int twoCnt = 0;
		int cnt = 0;
		int cur = 0;
		while( twoCnt != N ) {
			cnt ++ ;
			bool ok = false ;
			int a = -1;
			int b = -1;
			int c = -1;
			for( i = 0; i < N; i ++ ) {
				if( !taken[ i ][ 1 ] ) {
					if( !taken[ i ][ 0 ] && cur >= star[ i ].b && b == -1 ) b = i;
					
				}

				if( !taken[ i ][ 0 ] && cur >= star[ i ].a ) a = i;
				else if( !taken[ i ][ 1 ] && taken[ i ][ 0 ] && cur >= star[ i ].b ) c = i;

			}


			if( a == -1 && b == -1 && c == -1 ) break ;
			if( b != -1 ) i = b;
			else if( c != -1 ) i = c;
			else i = a;


			
			taken[ i ][ 0 ] = true;
			cur ++;
			if( i == b ) { taken[ i ][ 1 ] = true; cur ++ ; twoCnt ++ ; }
			if( i == c ) { taken[ i ][ 1 ] = true; twoCnt ++ ; } 
	//		printf("%d %d\t", i, cur );
		
		}

		if( twoCnt == N ) printf("Case #%d: %d\n", caseId, cnt );
		else printf("Case #%d: Too Bad\n", caseId );
	}

	return 0;

}