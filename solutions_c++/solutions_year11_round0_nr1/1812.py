#include <fstream>
#include <vector>

using namespace std;

int solve( int N, vector< pair<char,int> > b ) {
	int posO = 1;
	int posB = 1;
	int res = 0;
	for( int i = 0; i < N; i++ ) {
		char c = b[i].first;
		int num = b[i].second;
		int j;
		if( c == 'O' ) {
			int time = abs( b[i].second - posO ) + 1;
			posO = b[i].second;
			res += time;
			for( j = i+1; j < N; j++ )
				if( b[j].first == 'B' ) break;
			if( j < N ) {
				if( abs( b[j].second - posB ) < time ) posB = b[j].second;
				else if( b[j].second > posB ) posB += time;
				else posB -= time;
			}
		}
		else {
			int time = abs( b[i].second - posB ) + 1;
			posB = b[i].second;
			res += time;
			for( j = i+1; j < N; j++ )
				if( b[j].first == 'O' ) break;
			if( j < N ) {
				if( abs( b[j].second - posO ) < time ) posO = b[j].second;
				else if( b[j].second > posO ) posO += time;
				else posO -= time;
			}
		}

	}
	return res;
}

int main( int argc, char **argv ) {
	int T, N;
	fstream fs_in( argv[1], ios_base::in );
	fstream fs_out( argv[2], ios_base::out );
	fs_in >> T;
	for( int i = 0; i < T; i++ ) {
		fs_in >> N;
		vector< pair<char,int> > b( N );
		for( int j = 0; j < N; j++ ) {
			char c;
			int num;
			fs_in >> c >> num;
			b[j] = pair<char,int>( c, num );
		}
		int res = solve( N, b );
		fs_out << "Case #" << i+1 << ": " << res << endl;
	}
	fs_in.close();
	fs_out.close();
	return 0;
}