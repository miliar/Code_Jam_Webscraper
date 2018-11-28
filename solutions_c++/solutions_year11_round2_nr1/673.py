#include <fstream>
#include <vector>
#include <string>

using namespace std;

vector<double> solve( int N, vector<string> s ) {
	vector< vector<double> > wp( N );
	for( int i = 0; i < N; i++ ) 
		wp[i].resize( N );

	for( int i = 0; i < N; i++ ) {
		int games = 0, wins = 0;
		for( int j = 0; j < N; j++ ) {
			if( s[i][j] != '.' ) games++;
			if( s[i][j] == '1' ) wins++;
		}
		wp[i][i] = (double)wins/games;
		for( int j = 0; j < N; j++ ) {
			if( i == j ) continue;
			if( s[i][j] == '.' ) wp[i][j] = wp[i][i];
			if( s[i][j] == '1' ) wp[i][j] = (double)(wins-1)/(games-1);
			if( s[i][j] == '0' ) wp[i][j] = (double)wins/(games-1);
		}
	}

	vector<double> owp( N );
	for( int i = 0; i < N; i++ ) {
		owp[i] = 0.0;
		int opp = 0;
		for( int j = 0; j < N; j++ ) 
			if( s[i][j] != '.' ) {
				owp[i] += wp[j][i];
				opp++;
			}
		owp[i] /= opp;
	}

	vector<double> oowp( N );
	for( int i = 0; i < N; i++ ) {
		int opp = 0;
		for( int j = 0; j < N; j++ ) 
			if( s[i][j] != '.' ) {
				oowp[i] += owp[j];
				opp++;
			}
		oowp[i] /= opp;
	}

	vector<double> rpi( N );
	for( int i = 0; i < N; i++ )
		rpi[i] = wp[i][i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25;
	return rpi;
}

int main( int argc, char **argv ) {
	int T, N;
	fstream fs_in( argv[1], ios_base::in );
	fstream fs_out( argv[2], ios_base::out );
	fs_in >> T;
	for( int i = 0; i < T; i++ ) {
		fs_in >> N;
		vector<string> s( N, "" );
		for( int j = 0; j < N; j++ ) 
			fs_in >> s[j];
		vector<double> res = solve( N, s );
		fs_out << "Case #" << i+1 << ":" << endl;
		for( int j = 0; j < N; j++ )
			fs_out << res[j] << endl;
	}
	fs_in.close();
	fs_out.close();
	return 0;
}