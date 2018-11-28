#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector< pair< char, size_t > > presses_data;

size_t run_case( presses_data & presses ) {
	struct robot {
		size_t pos, time; // last known position & time

		robot(): pos(1), time(0) {}
	};
	robot o, b;

	for( presses_data::const_iterator it=presses.begin(), end=presses.end(); it!=end; ++it ) {
		robot * curr, * other;
		if( it->first == 'O' ) {
			curr = &o;
			other = &b;
		} else {
			curr = &b;
			other = &o;
		}

		size_t dist = abs( (int)curr->pos - (int)it->second );

		curr->time = max( other->time+1, curr->time + dist + 1 );
		curr->pos = it->second;
	}

	return max( o.time, b.time );
}

void all_cases( istream & in, ostream & out ) {
	size_t cases_count;
	in >> cases_count;

	for( size_t i=1; i<=cases_count; ++i ) {
		size_t press_count;
		in >> press_count;

		presses_data presses;

		for( size_t j=0; j<press_count; ++j ) {
			char robot;
			size_t button;
			in >> robot >> button;
			presses.push_back( make_pair( robot, button ) );
		}
		out << "Case #" << i << ": " << run_case( presses ) << endl;
	}
}

int main() {
	all_cases( ifstream( "in.txt" ), ofstream( "out.txt" ) );
	return 0;
}
