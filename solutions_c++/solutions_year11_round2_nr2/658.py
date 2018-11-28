#include <fstream>
#include <vector>
#include <string>

using namespace std;

const double maxt = 10e14;
const double eps = 10e-7;

bool check( int C, int D, vector<int> p, vector<int> v, double t ) {
	double prev, cur;
	prev = (double)p[0] - t + (double)D * ( v[0] - 1 );
	if( prev > (double)p[0] + t ) return false;
	prev += (double)D;
	for( int i = 1; i < C; i++ ) {
		cur = (double)p[i] - t;
		cur = max( prev, cur );
		cur += (double)D * ( v[i] - 1 );
		if( cur > (double)p[i] + t ) return false;
		cur += (double)D;
		prev = cur;
	}
	return true;
}

double solve( int C, int D, vector<int> p, vector<int> v ) {
	double low = 0.0, high = maxt;
	while( high - low > eps ) {
		double mid = ( low + high ) / 2;
		if( check( C, D, p, v, mid ) ) high = mid;
			else low = mid;
	}
	return ( low + high ) / 2;
}

int main( int argc, char **argv ) {
	int T, C, D;
	fstream fs_in( argv[1], ios_base::in );
	fstream fs_out( argv[2], ios_base::out );
	fs_in >> T;
	for( int i = 0; i < T; i++ ) {
		fs_in >> C >> D;
		vector<int> p( C );
		vector<int> v( C );
		for( int j = 0; j < C; j++ ) 
			fs_in >> p[j] >> v[j];
		check( C, D, p, v, 1.5 );
		double res = solve( C, D, p, v );
		fs_out << "Case #" << i+1 << ": " << res << endl;
	}
	fs_in.close();
	fs_out.close();
	return 0;
}