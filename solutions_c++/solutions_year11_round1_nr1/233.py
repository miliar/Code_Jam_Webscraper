#include <fstream>
#include <string>

using namespace std;

bool do_case( size_t n, size_t pd, size_t pg ) {
	size_t m = 100;

	if( pg == 100 ) {
		return pd == 100;
	}

	if( pg == 0 ) {
		return pd == 0;
	}

	for( size_t div=2; div<100; ++div ) {
		if( m % div == 0 && pd % div == 0 ) {
			pd /= div;
			m /= div;
			--div;
		}
	}

	return m <= n;
}

int main() {
	ifstream in( "a_in.txt" );
	ofstream out( "a_out.txt" );

	size_t cases_count;
	in >> cases_count;

	for( size_t i=1; i<=cases_count; ++i ) {
		size_t n, pd, pg;
		string s;
		in >> s >> pd >> pg;

		n = atoi( s.c_str() );

		out << "Case #" << i << ": "  << ( do_case( n, pd, pg ) ? "Possible" : "Broken" ) << endl;
	}

	return 0;
}
