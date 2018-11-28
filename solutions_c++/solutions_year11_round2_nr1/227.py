#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
typedef long long LLD ;
const int N = 107 ;
const int M = 13 ;
int n, m ;
char c[N][N] ;
double wp[N] , opw[N] , oopw[N] ;
double win[N], lose[N], cnt[N] ;

int main() {
	int i, j, k, t, var, end ;
	double s = 0 ;

	freopen("in.txt","r",stdin ) ;
	freopen("out.txt","w",stdout ) ;

	cin >> t;
	for( var = 1 ; var <= t ; var++ ) {
		cin >> n;
		for( i = 0 ; i < n ; ++i ) {
			cin >> c[i];
			win[i] = lose[i] = 0 ;
			for( j = 0 ; j < n; ++j ) {
				if ( c[i][j] == '0' ) lose[i]++ ;
				else if ( c[i][j] == '1' ) win[i]++ ;
				else ;
			}
			cnt[i] = win[i]+lose[i] ;
			wp[i] = win[i]/(win[i]+lose[i]) ;
		}
		for( i = 0 ; i < n ; ++i ){
			opw[i] = 0 ;
			for( j = 0 ; j < n ; ++j ){
				if ( c[i][j] == '0' ){
					opw[i] += (win[j]-1)/(cnt[j]-1) ;
				}else if ( c[i][j] == '1' ){
					opw[i] += win[j]/(cnt[j]-1) ;
				}
			}
			opw[i] /= cnt[i] ;
		}
		for( i = 0 ; i < n ; ++i ){
			oopw[i] = 0 ;
			for( j = 0 ; j < n ; ++j ){
				if ( c[i][j] != '.' ){
					oopw[i] += opw[j] ;
				}
			}
			oopw[i] /= cnt[i] ;
		}
		printf("Case #%d:\n", var) ;
		
		for( i = 0 ; i < n ; ++i ){
			printf("%lf\n", 0.25 * wp[i] + 0.50 * opw[i] + 0.25 * oopw[i] ) ;
		}
	}

	return 0 ;
}
