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

#define MAX 105
int score[ MAX ];
int S,p,N;
int test_case;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i;
	scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		scanf("%d %d %d", &N, &S, &p);
		int one = 0;
		int ans = 0;
		for( i = 0; i < N; i ++ ) {
			scanf("%d", &score[ i ] );
			if( ( p * 3 ) <= score[ i ] ){
				ans ++ ;
				continue;
			}

			int v = ( p * 3 ) - score[ i ] ;
			if( v == 2 || v == 1 ){
				ans ++ ;
				continue;
			}

			if( p - 2 >= 0 ) {
				if( ( p + p + p - 3 ) == score[ i ] ) one ++ ;
				else if( ( p + p + p - 2 ) == score[ i ] ) one ++ ;
				else if( ( p + p + p - 4 ) == score[ i ] ) one ++ ;
			}



		}

		if( one <= S ) {
			ans += one;
			S -= one;
		}
		
		else {
			ans += S;
			S = 0;
		}

		

		printf("Case #%d: %d\n", caseId, ans );

	}



	return 0;
}