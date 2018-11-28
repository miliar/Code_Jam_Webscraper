#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

size_t run_case( vector< size_t > & numbers ) {
	size_t xored = 0;
	size_t fl = numbers.front();
	size_t sum = 0;
	for( vector< size_t >::const_iterator it=numbers.begin(), end=numbers.end(); it!=end; ++it ) {
		xored ^= *it;
		sum += *it;
		fl = min( fl, *it );
	}
	if( xored != 0 ) {
		return 0;
	} else {
		return sum - fl;
	}
}

void all_cases( istream & in, ostream & out ) {
	size_t cases_count;
	in >> cases_count;

	for( size_t i=1; i<=cases_count; ++i ) {
		size_t numbers_count;
		in >> numbers_count;

		vector< size_t > numbers;

		for( size_t j=0; j<numbers_count; ++j ) {
			size_t number;
			in >> number;
			numbers.push_back( number );
		}

		size_t res = run_case( numbers );
		out << "Case #" << i << ": ";
		if( res ) {
			out << res;
		} else {
			out << "NO";
		}
		out << endl;
	}
}

int main() {
	all_cases( ifstream( "c_in.txt" ), ofstream( "c_out.txt" ) );
	return 0;
}
