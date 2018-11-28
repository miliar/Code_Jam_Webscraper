#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

double run_case( vector< size_t > & numbers ) {
	double res = 0;
	for( size_t i=0, size=numbers.size(); i<size; ++i ) {
		if( numbers[i] != i+1 ) {
			res += 1;
		}
	}
	return res;
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

		out << "Case #" << i << ": " << run_case( numbers ) << endl;
	}
}

int main() {
	all_cases( ifstream( "d_in.txt" ), ofstream( "d_out.txt" ) );
	return 0;
}
