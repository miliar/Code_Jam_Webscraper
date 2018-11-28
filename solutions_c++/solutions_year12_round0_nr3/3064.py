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

int test_case;
int A,B;

bool isOK( int a, int b ) {
	int A = a;
	int d[ 10 ];
	int length = 0;
	while( a > 0 ) {
		d[ length ++ ] = a % 10;
		a /= 10;
	}

	int t[ 10 ];
	int z = 0;
	int i,j,cnt;
	for( i = length - 1; i >= 0; i -- ) t[ z ++ ] = d[ i ];
	for( i = 1 ; i < length; i ++ ) {
		int v = 0;
		for( j = i, cnt = 0; cnt < length; cnt ++ , j = ( j + 1 ) % length ) {
			v *= 10;
			v += t[ j ];
			//if( A == 12 && b == 21 ) printf("%d\t", v );
		}


		//if( A == 12 ) printf("%d\t", length );
		if( v == b ){
			return true;
		}
	}

	return false ;
}

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output_small.txt", "w", stdout);
	scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		scanf("%d %d", &A, &B);
		int ans = 0;
		for( int i = A; i < B; i ++ ) {
			for( int j = i + 1; j <= B; j ++ ) {
				if( isOK( i,j ) ) ans ++ ;
			}
		}

		printf("Case #%d: %d\n", caseId,ans );
	}
	return 0;
}