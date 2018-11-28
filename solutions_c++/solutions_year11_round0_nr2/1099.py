#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

struct case_data {
	map< pair< char, char >, char > combinations;
	set< pair< char, char > > oppositions;
	string invocation;
};

pair< char, char > order_pair( char c1, char c2 ) {
	if( c1 < c2 ) {
		return make_pair( c1, c2 );
	} else {
		return make_pair( c2, c1 );
	}
}

vector< char > run_case( case_data & data ) {
	vector< char > stack;

	for( string::const_iterator it=data.invocation.begin(), end=data.invocation.end(); it!=end; ++it ) {
		stack.push_back( *it );

		/* check for combinations*/
		bool need_check = true;
		while( need_check ) {
			need_check = false;
			size_t size = stack.size();
			if( size > 1 ) {
				pair< char, char > top = order_pair( stack[size-1], stack[size-2] );
				map< pair< char, char >, char >::iterator find = data.combinations.find( top );
				if( find != data.combinations.end() ) {
					// combination found !
					stack.pop_back();
					stack.pop_back();
					stack.push_back( find->second );
					need_check = true;
				}
			}
		}

		/* check for oppositions */
		char top = stack.back();
		for( vector< char >::iterator it=stack.begin(), end=stack.end()-1; it!=end; ++it ) {
			pair< char, char > test = order_pair( top, *it );
			if( data.oppositions.find( test ) != data.oppositions.end() ) {
				// opposition found, clearing stack
				stack.clear();
				break;
			}
		}
	}

	return stack;
}

string format_stack( vector< char > & stack ) {
	string res = "[";

	for( vector< char >::iterator it=stack.begin(), end=stack.end(); it!=end; ) {
		res.push_back( *it );
		if( ++it == end ) {
			break;
		}
		res += ", ";
	}

	res += "]";

	return res;
}

void all_cases( istream & in, ostream & out ) {
	size_t cases_count;
	in >> cases_count;

	for( size_t i=1; i<=cases_count; ++i ) {
		case_data data;
		size_t comb_count, opp_count, inv_count;

		in >> comb_count;
		for( size_t j=0; j<comb_count; ++j ) {
			string comb;
			in >> comb;
			data.combinations.insert( make_pair( order_pair( comb[0], comb[1] ), comb[2] ) );
		}

		in >> opp_count;
		for( size_t j=0; j<opp_count; ++j ) {
			string opp;
			in >> opp;
			data.oppositions.insert( order_pair( opp[0], opp[1] ) );
		}

		in >> inv_count;
		string inv;
		in >> inv;
		if( inv.length() != inv_count ) {
			// This should never happen
			throw "Panic !!!";
		}

		data.invocation = inv;

		out << "Case #" << i << ": " << format_stack( run_case( data ) ) << endl;
	}
}

int main() {
	all_cases( ifstream( "in.txt" ), ofstream( "out.txt" ) );
	return 0;
}
