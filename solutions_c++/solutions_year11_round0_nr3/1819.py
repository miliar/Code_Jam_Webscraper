#include <fstream>
#include <vector>

using namespace std;

bool solve( int N, vector<int> c, int& sum ) {
	int xor_sum = 0;
	int min = c[0];
	sum = 0;
	for( int i = 0; i < N; i++ ) {
		xor_sum ^= c[i];
		sum += c[i];
		if( c[i] < min ) 
			min = c[i];
	}
	if( xor_sum ) return false;
	sum -= min;
	return true;
}

int main( int argc, char **argv ) {
	int T, N;
	fstream fs_in( argv[1], ios_base::in );
	fstream fs_out( argv[2], ios_base::out );
	fs_in >> T;
	for( int i = 0; i < T; i++ ) {
		fs_in >> N;
		vector<int> c( N );
		for( int j = 0; j < N; j++ ) 
			fs_in >> c[j];
		int res;
		bool ok = solve( N, c, res );
		fs_out << "Case #" << i+1 << ": ";
		if( ok ) fs_out << res << endl;
			else fs_out << "NO" << endl;
	}
	fs_in.close();
	fs_out.close();
	return 0;
}