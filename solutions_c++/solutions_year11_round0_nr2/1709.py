#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

typedef pair<char,char> pc;

const int num_let = 'Z' - 'A' + 1;

int let_pos( char c1, char c2 ) {
	return ( c1 - 'A' ) * num_let + ( c2 - 'A' );
}

string solve( int C, map<pc,char> combine, int D, vector<bool> opposed, int N, string invoked ) {
	string res = "";
	for( int i = 0; i < (int)invoked.length(); i++ ) {
		res += invoked[i];
		int last = res.length() - 1;
		// combine
		if( res.length() == 1 ) continue;
		map<pc,char>::iterator it;
		it = combine.find( pc(res[last-1],res[last]) );
		if( it != combine.end() ) { 
			res.erase( last-1, 2 );
			res += it->second;
			continue;
		}
		// oppose
		for( int j = 0; j < (int)res.length()-1; j++ )
			if( opposed[let_pos(res[j], invoked[i])] ) {
				res.clear();
				break;
			}
	}
	return res;
}

int main( int argc, char **argv ) {
	int T, C, D, N;
	fstream fs_in( argv[1], ios_base::in );
	fstream fs_out( argv[2], ios_base::out );
	fs_in >> T;
	for( int i = 0; i < T; i++ ) {
		fs_in >> C;
		map<pc,char> combine;
		for( int j = 0; j < C; j++ ) {
			string s;
			fs_in >> s;
			combine.insert( pair<pc,char>( pc( s[0], s[1] ), s[2] ) );
			combine.insert( pair<pc,char>( pc( s[1], s[0] ), s[2] ) );
		}

		fs_in >> D;
		vector<bool> opposed( num_let * num_let, false );
		for( int j = 0; j < D; j++ ) {
			string s;
			fs_in >> s;
			opposed[let_pos(s[0],s[1])] = true;
			opposed[let_pos(s[1],s[0])] = true;
		}

		fs_in >> N;
		string invoked;
		fs_in >> invoked;

		string res = solve( C, combine, D, opposed, N, invoked );
		fs_out << "Case #" << i+1 << ": [";
		for( int j = 0; j < (int)res.length(); j++ ) {
			fs_out << res[j];
			if( j < (int)res.length()-1 ) fs_out << ", ";
		}
		fs_out << "]" << endl;
	}
	fs_in.close();
	fs_out.close();
	return 0;
}