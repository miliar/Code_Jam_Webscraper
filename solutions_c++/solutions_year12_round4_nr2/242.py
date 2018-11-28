#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;

int N ;
double X , Y ;
pair<double , int> Cir[1009] ;
pair<double , double> ans[1009] ;

#define MP make_pair
#define R first
#define id second

int main() {
	freopen( "B2.in" , "r" , stdin ) ;
	freopen( "B2.out", "w" , stdout) ;
	int Test ; cin >> Test ;
	for ( int t = 1 ; t <= Test ; t ++ ) {
		cin >> N >> X >> Y ;
		for ( int i = 1 ; i <= N ; i ++ ) { cin >> Cir[i].R ; Cir[i].id = i ; }
		sort( Cir+1 , Cir+N+1 ) ;
		Cir[0] = Cir[N] ;
		
		double maxr = Cir[0].R ;
		for ( int i = 1 ; i < N ; i ++ ) maxr = max( maxr , Cir[i].R ) ;
		
		double xx = 0.000 , rr = 0.000 ;
		
		ans[Cir[0].id] = MP(0.000 , 0.000) ;
		for ( int i = 1 ; i < N ; i ++ ) {
			xx = xx + Cir[i-1].R + Cir[i].R ;
			if ( xx > max(X,Y) ) { xx = 0.000 , rr += maxr*2 ; }
			if ( X >= Y ) { ans[Cir[i].id] = MP(xx , rr) ; if ( xx > X || rr > Y ) cout << "\nERROR\n" ; }
			else          { ans[Cir[i].id] = MP(rr , xx) ; if ( rr > X || xx > Y ) cout << "\nERROR\n" ; }
		}
		printf( "Case #%d:" , t ) ;
		for ( int i = 1 ; i <= N ; i ++ ) printf( " %.10lf %.10lf" , ans[i].first , ans[i].second ) ;
		puts("") ;
	}
}