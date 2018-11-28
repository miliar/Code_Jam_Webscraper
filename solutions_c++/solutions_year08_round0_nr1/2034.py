#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
#include <set>

using namespace std;

int main( int argc, char* argv[] ){
	int num_cases;
	string line;
  	ifstream is( "input/A-large.in" );
	if( !is.eof() ){
		getline( is, line );
	    istringstream iss( line );
		iss >> num_cases;
	}

	ofstream os( "output.txt" );
	for( int i = 1; i <= num_cases; ++i ){
		// Read engines.
		getline( is, line );
		int num_engines;
		istringstream iss( line );
		iss >> num_engines;

		vector< string > engines;
		for( int j = 0; j < num_engines; ++j ){
			getline( is, line );
			engines.push_back( line );
		}

		// Read queries.
		getline( is, line );
		int num_queries;
		istringstream isss( line );
		isss >> num_queries;

		vector< string > queries;
		string current_engine( "" );
		set< string > buf;
		int num_switches = -1;
		for( int k = 0; k < num_queries; ++k ){
			getline( is, line );
			queries.push_back( line );
			buf.insert( line );
			if( num_switches < 0 && buf.size() == num_engines ){
				current_engine = line;
				num_switches = 0;
			}
		}

		// Number of unique queries is larger than number of engines.
		if( num_switches == 0 ){
			int q = 0;
			while( q < num_queries ){
				buf.clear();
				if( current_engine == queries[ q ] ){
					++num_switches;
					int x = q;
					while( x < num_queries && buf.size() < num_engines ){
						buf.insert( queries[ x ] );
						++x;
					}	
					if( buf.size() == num_engines ){
						current_engine = queries[ x - 1 ];
					} else if( x == num_queries ){
						// Find engine which is not in buf.
						for( int e = 0; e < num_engines; ++e ){
							if( buf.find( engines[ e ] ) == buf.end() ){
								current_engine = engines[ e ];
								break;
							}
						}
					}
				}
				++q;
			}
		}
		
		num_switches = ( num_switches < 0 ? 0 : num_switches );
		os << "Case #" << i << ": " << num_switches << endl;
	}	
	is.close();
	os.close();
	return 0;
}

