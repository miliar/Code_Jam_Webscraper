#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n , s , run , m;
double t;

vector < pair < int , int > > a;

void read() {
	int i;
	int l , r , sp;
	int last = 0;
	
	a.clear();
	
	scanf ( "%d%d%d%lf%d" , &n , &s , &run , &t , &m );
	for (i = 1; i <= m; i++) {
		scanf ( "%d%d%d" , &l , &r , &sp );
		
		a.push_back ( make_pair ( s , l - last ) );
		a.push_back ( make_pair ( s + sp , r - l ) );
		last = r;
	}
	
	a.push_back ( make_pair ( s , n - last ) );
}

double go ( double sp , double run , double dist ) {
	double ans = 0;
	
// 	printf ( "%lf  %lf     %lf    %lf %lf\n" , dist , dist / (sp + run) , sp + run , sp , run );
	
	if ( dist / (sp + run) < t + 1e-9 ) {
		ans = dist / (sp + run);
		t -= ans;
	} else {
		dist -= t * (sp + run);
		ans = t + dist / sp;
		t = 0;
	}
	
	return ans;
}

void solve() {
	double ans = 0;
	int i;
	
	run -= s;
	sort ( a.begin() , a.end() );
	for (i = 0; i < (int)a.size(); i++)
		ans += go ( a[i].first , run , a[i].second );
	
	printf ( "%.9lf\n" , ans );
}

int main() {
	int cases , i;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d: " , i );
		solve();
		
// 		break;
	}
	
	return 0;
}
