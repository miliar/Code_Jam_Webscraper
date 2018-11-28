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

#define MAX 105
#define pb push_back
#define mem( a, i ) memset( a, i, sizeof( a ) ) 
#define eps 1e-8

int test_case, N;
vector< string > tab;
double WP[ MAX ];
int P[ MAX ];
int Cnt[ MAX ];
double OWP[ MAX ];
double OOWP[ MAX ];


void wp( ) {
	for( int i = 0; i < N; i ++ ) {
		int cnt = 0;
		int p = 0;
		for( int j = 0; j < N; j ++ ) {
			if( tab[ i ][ j ] == '1' ) p ++;
			if( tab[ i ][ j ] != '.' ) cnt ++;
		}

		WP[ i ] = ( double ) p / ( double ) cnt ;
		P[ i ] = p;
		Cnt[ i ] = cnt;
	}
}


void owp(){
	for( int i = 0; i < N; i ++ ) {
		int p, cnt;
		double res = 0.0;
		int v = 0;
		for( int j = 0; j < N; j ++ ) {
			if( i == j ) continue;
			if( tab[ j ][ i ] == '.' ) continue;
			p = P[ j ];
			cnt = Cnt[ j ];
			if( tab[ j ][ i ] == '1' ) p --;
			if( tab[ j ][ i ] != '.' ){ cnt --; v ++ ; }
			res += ( double ) p / ( double ) cnt;
		//	if( i == 1 ) printf("%d %d\n", p, cnt );
		}
		
	//	printf("%lf\n", res );
		OWP[ i ] = res / ( double ) v ;
		

	}

}

void oowp(){
	for( int i = 0; i < N; i ++ ) {
		int v = 0;
		double res = 0.0;
		for( int j = 0; j < N; j ++ ) {
			if( tab[ i ][ j ] != '.' ) {
				v ++;
				res += OWP[ j ];
			}
		}

		OOWP[ i ] = res / ( double ) v;
	}
}


int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i;
	scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		string inp;
		tab.clear();
		scanf("%d", &N);
		for( i = 0; i < N; i ++ ) {
			cin >> inp;
			tab.pb( inp );
		}

		wp();
		owp();
		oowp();
		double ans;
		printf("Case #%d:\n", caseId );
		for( i = 0; i < N; i ++ ) {
		//	printf("%lf\t", OWP[ i ] );
			ans = ( 0.25 * WP[ i ] ) + ( 0.50 * OWP[ i ] ) + ( 0.25 * OOWP[ i ] ) + eps;
			printf("%lf\n", ans );
		}

	}
	return 0;
}