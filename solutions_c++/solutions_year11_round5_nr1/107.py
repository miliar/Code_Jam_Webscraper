#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int ww , l , u , g;
vector < pair < double , double > > a , b , e , s;

void read() {
	int i;
	int x , y;
	
	a.clear();
	b.clear();
	
	scanf ( "%d%d%d%d" , &ww , &l , &u , &g );
	
// 	fprintf ( stderr , "%d %d %d\n" , ww , l , u );
	
	for (i = 1; i <= l; i++) {
		scanf ( "%d%d" , &x , &y );
		a.push_back ( make_pair ( x , y ) );
	}
	
	for (i = 1; i <= u; i++) {
		scanf ( "%d%d" , &x , &y );
		b.push_back ( make_pair ( x , y ) );
	}
}

inline double cross ( pair < double , double > a , pair < double , double > b , pair < double , double > c ) {
// 	printf ( "%lf %lf\n%lf %lf\n%lf %lf\n\n" , a.first , a.second , b.first , b.second , c.first , c.second );
	return (b.first - a.first) * (c.second - a.second) - (b.second - a.second) * (c.first - a.first );
}

inline double getpnt ( pair < double , double > a , pair < double , double > b , double c ) {
	return a.second + (b.second - a.second) * ((c - a.first) / (b.first - a.first));
}

void solve() {
	pair < double , double > q , w;
	double l , r , mid;
	double area = 0 , now;
	int i , j , k , d;
	
	for (i = 2; i < (int)a.size(); i++)		area += cross ( a[0] , a[i - 1] , a[i] );
	area += cross ( a[0] , a.back() , b.back() );
	for (i = (int)b.size() - 2; i >= 0; i--)		area += cross ( a[0] , b[i + 1] , b[i] );
// 	area += cross ( a[0] , b[1] , b[0] );
	
	area = fabs ( area ) / 2.;
	
	area /= (double)g;
// 	printf ( " -- %lf\n" , area );
	
	q = a[0];
	w = b[0];
	i = j = 1;
	
	for (k = 1; k < g; k++) {
		l = q.first;
		r = ww;
// 		
// 		printf ( "%lf %lf\n" , a[i].first , a[i].second );
// 		printf ( "%lf %lf\n" , b[j].first , b[j].second );
		
		for (int iter = 0; iter < 100; iter++) {
			mid = (l + r) / 2.;
// 			mid = 5.;
			
			e.clear();
			s.clear();
			now = 0;
			
			e.push_back ( q );
			s.push_back ( w );
			
			for (d = i; d < (int)a.size(); d++)
				if ( a[d].first < mid )
					e.push_back ( a[d] );
				else {
					e.push_back ( make_pair ( mid , getpnt ( a[d - 1] , a[d] , mid ) ) );
					break;
				}
				
			for (d = j; d < (int)b.size(); d++)
				if ( b[d].first < mid )
					s.push_back ( b[d] );
				else {
					s.push_back ( make_pair ( mid , getpnt ( b[d - 1] , b[d] , mid ) ) );
					break;
				}
				
// 			for (d = 0; d < (int)e.size(); d++)
// 				printf ( "%lf %lf\n" , e[d].first , e[d].second );
// 			printf ( "    ---\n" );
// 			for (d = 0; d < (int)s.size(); d++)
// 				printf ( "%lf %lf\n" , s[d].first , s[d].second );
// 			printf ( "\n" );
				
			for (d = 2; d < (int)e.size(); d++)		now += cross ( e[0] , e[d - 1] , e[d] );
			now += cross ( e[0] , e.back() , s.back() );
			for (d = (int)s.size() - 2; d >= 0; d--)		now += cross ( e[0] , s[d + 1] , s[d] );
// 			now += cross ( e[0] , s[1] , s[0] );
			
			now = fabs ( now ) / 2.;
			
// 			printf ( "%lf %lf    %lf\n" , l ,r , mid );
// 			printf ( "%lf\n" , now );
			
// 			break;
			
			if ( now > area )
				r = mid;
			else
				l = mid;
// 			printf ( "%lf %lf\n" , l , r );
		}
		
// 		printf ( "%lf %lf  %lf\n" , l , r , mid );
		
// 		break;
		
		mid = (l + r) / 2.;
		
		printf ( "%.8lf\n" , mid );
		
		for (; i < (int)a.size(); i++)
			if ( a[i].first > mid - 1e-9 ) {
				q = make_pair ( mid , getpnt ( a[i - 1] , a[i] , mid ) );
				break;
			}
				
		for (; j < (int)b.size(); j++)
			if ( b[j].first > mid + 1e-9 ) {
				w = make_pair ( mid , getpnt ( b[j - 1] , b[j] , mid ) );
				break;
			}
	}
}

int main() {
	int i , cases;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d:\n" , i );
		solve();
		
// 		break;
	}
	
	return 0;
}
