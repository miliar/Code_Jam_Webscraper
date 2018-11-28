#include<iostream>
#include<cmath>
#include<vector>
#include<set>
#include<cstdio>
#include<queue>
#include<stack>
#include<list>
#include<map>
#include<string>
#include<cstring>
#include<sstream>

using namespace std;

#define MAX 16
#define pb push_back
#define mem( a, i ) memset( a, i, sizeof( a ) ) 

int N;
int can[ MAX ];
vector< int > P;
vector< int > S;
int test_case;
int s1,s2;

bool ok(){
	int sum1, sum2,i,j;
	sum1 = sum2 = 0;
	for( i = 0; i < 20; i ++ ) {
		int b = 0;
		for( j = 0; j < S.size(); j ++ ) {
			if( S[ j ] & ( 1 << i ) ) b ++; 
			
			
		}

	//	printf("%d\t", b );
		if( b % 2 == 1 ) sum1 |= ( 1 << i ) ;
	}

	for( i = 0; i < 20; i ++ ) {
		int b = 0; 
		for( j = 0; j < P.size(); j ++ ) {
			if( P[ j ] & ( 1 << i ) ) b ++;
		}

		if( b % 2 == 1 ) sum2 |= ( 1 << i );
	}
	
	

	
//	printf("%d %d\t", sum1,sum2);
	return sum1 == sum2;

}

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i,j;
	scanf( "%d", &test_case );
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		scanf( "%d", &N );
		for( i = 0; i < N; i ++ ) {
			scanf( "%d", &can[ i ] );
		}
		int ans = 0;
		for( i = 1; i < ( 1 << N ) ; i ++ ) {
			s1 = s2 = 0;
			S.clear();
			P.clear();
			for( j = 0; j < N; j ++ ) {
				if( i & ( 1 << j ) ){ S.pb( can[ j ] ); s1 += can[ j ] ; }
				else { P.pb( can[ j ] ); s2 += can[ j ] ; }
							
			}

			if( ok() && S.size() > 0 && P.size() > 0 ) {
				if( s1 > ans ) ans = s1;
				if( s2 > ans ) ans = s2;
			}
		}

		if( ans == 0 ) printf("Case #%d: NO\n", caseId );
		else printf("Case #%d: %d\n", caseId, ans );
	}
	return 0;
}