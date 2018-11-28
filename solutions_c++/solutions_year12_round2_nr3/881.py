#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<list>
#include<string>
#include<cstring>
#include<cstdlib>
#include<set>
#include<map>
#include<vector>
using namespace std;

#define MAX 2000005

int mp[ MAX ];
int test_case;
vector< int > v;
int N;



int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i,j;
	scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		scanf("%d", &N);
		int a;
		v.clear();
		memset( mp, -1, sizeof( mp ) ) ;
		for( i = 0; i < N; i ++ ) {
			scanf("%d", &a);
			v.push_back( a ) ;
		}

		bool ok = false;
		printf("Case #%d:\n", caseId );
		for( i = 1; i < ( 1 << N ) ; i ++ ) {
	//		printf("%d\t", i );
			int s = 0;
			for( j = 0; j < N; j ++ ) {
				if( ( i & ( 1 << j ) ) != 0 ) {
					s += v[ j ];
				}
			}

			if( mp[ s ] == -1 ) mp[ s ] = i ;
						
		}



		for( i = 1; i < ( 1 << N ) ; i ++ ) {
			int s = 0;
			for( j = 0; j < N; j ++ ) {
				if( ( i & ( 1 << j ) ) != 0 ) {
					s += v[ j ];
				}
			}

			if( mp[ s ] != -1 ) {
				int val = mp[ s ] ;
				if( val != i ) {
					int cnt = 0;
					for( j = 0; j < N;  j ++ ) {
						if( ( i & ( 1 << j ) ) != 0 ){
							if( cnt ++ ) printf(" " );
							printf("%d", v[ j ] );
						}
							
						
					}
					printf("\n");
					cnt = 0;
					for( j = 0; j < N; j ++ ) {
						if( ( ( val & ( 1 << j ) ) != 0 ) ){
							if( cnt ++ ) printf(" " );	
							printf("%d", v[ j ] );
						}
					}


					printf("\n");
					ok = true;
					break ;

				}
			}


		}

		if( !ok ) printf(" Impossible\n");

	}
	return 0;
}