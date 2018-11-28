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

#define MAX 300
#define eps 1e-8
struct info { 
	int id;
	int val;
};
int test_case;
int N,s;
vector< struct info > v;

bool cmp( struct info a , struct info b ) {
	return a.val > b.val;
}

double ans[ MAX ];


/*int ok( double d, int id ) {
	int n = v.size() ;
	d = d / 100.0;
	double score = ( ( double ) s * d ) + ( double ) v[ id ].val ;
	double d2 = ( 1.0 - d ) / ( double ) ( n - 1 ) ;
	double t ;
	int cnt = 0;
	for( int i = 0; i < N; i ++ ) {
		if( i == id ) continue;
		double scoreK = ( ( double ) s * ( d2 ) ) + ( double ) v[ i ].val ;
		if( scoreK - score < eps  ) continue; ; 
		if( scoreK + eps < score ) continue;
		cnt ++ ;
	}

	bool flag = false;
	if( cnt == n - 1 ) return -1;
	int k ;
	for( int j = 0; j < N; j ++ ) {
		if( j == id ) continue;
		double scoreK = ( ( double ) s * ( 1.0 - d ) ) + ( double ) v[ j ].val ;
		if( scoreK - score < eps ) continue;
		if( scoreK + eps < score ) continue;
		for( int k = 0; k < N; k ++ ) {
			if( k == id || k == j ) continue;
			t = v[ k ].val;
			if( t - score < eps ) continue;
			if( t + eps < score ) continue;
			flag = true;
		}

	}
	
	if( !flag ) return 0;
	return -1;
}*/

int ok( double d , int id ) {
	int n = v.size() ;
	d = d / 100.0;
	double score = ( ( double ) s * d ) + ( double ) v[ id ].val ;
	double left = 1 - d ;
	for( int i = 0; i < N; i ++ ) {
		if( i == id ) continue;
		double var = ( score - ( double ) v[ i ].val ) / ( double ) s;
		if( var + eps < 0.0 ) continue;
	//	if( id == 1 ) printf("%lf %lf\n", d, var );
		if( left - var < eps ) return 0;
		if( left + eps < var ) return 0;
		left -= var;
	}

	return -1;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("outlarge.txt", "w", stdout);
	int i;
	scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		scanf("%d", &N);
		struct info a;
		s = 0;
		v.clear();
		for( i = 0; i < N; i ++ ) {
			scanf("%d", &a.val );
			s += a.val ;
			a.id = i ;
			v.push_back( a );
		
		}

		printf("Case #%d:", caseId );
		sort( v.begin() , v.end() , cmp );
		for( i = 0; i < N; i ++ ) {
			double lo = 0.0;
			double hi = 100.0;
			double ret = 0.0;
			while( lo + eps <= hi ) {
				double mid = ( lo + hi ) / 2.0;
			//	printf("%lf\t", mid );
				int vOk = ok( mid, i ) ;
			//	printf("%d\n", vOk );
				if( vOk == 0  ) {
					hi = mid ;
					ret = mid;
				//	printf("%lf ", ret );
				}
				else lo = mid;
			}

			ans[ v[ i ].id ] = ret ;
		}

		for( i = 0; i < N; i ++ ) printf(" %lf", ans[ i ] + eps );
		printf("\n");
	}

	return 0;
}