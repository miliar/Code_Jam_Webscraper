#include <string>
#include <fstream>
#include <set>
#include <vector>

void createSet(
		std::vector< std::string >& engines,
		std::set< std::string >& eSet
) {
	for( unsigned int i = 0; i < engines.size(); i++ ) {
		eSet.insert( engines[ i ] );
	}
}


int getNumberOfSwitches(
		std::vector< std::string >& engines,
		std::vector< std::string >& queries
) {
	// create set
	std::set< std::string > eSet;
	createSet( engines, eSet );

	// count
	int cnt = 0;
	for( unsigned int i = 0; i < queries.size(); i++ ) {
		eSet.erase( queries[ i ] );

		if( eSet.size() == 0 ) {
			cnt++;
			createSet( engines, eSet );
			eSet.erase( queries[ i ] );
		}
	}

	return cnt;
}

void saveTheUniverse( const char* path ) {
	// buffer
	char buff[ 4096 ];

	// file path
	std::string inPath = path;
	std::string outPath = inPath + ".out";

	// open the file
	std::ifstream ifs( inPath.c_str() );
	std::ofstream ofs( outPath.c_str() );

	int c = 1;
	int eCnt = 0;
	int qCnt = 0;
	int step = 0;
	std::vector< std::string > engines;
	std::vector< std::string > queries;

	while( !ifs.eof() ) {
		// read line
		ifs.getline( buff, 4096 );

		// save the universe	
		if( step == 0 ) {	// get the number of tests
			step = 1;
		}
		else if( step == 1 ) {	// get the number of engines
			engines.clear();
			eCnt = atoi( buff );
			step = 2;
		}
		else if( step == 2 ) {	// get engine
			engines.push_back( buff );
			if( (int)engines.size() >= eCnt ) {
				step = 3;
			}
		}
		else if( step == 3 ) {	// get the number of queries
			queries.clear();
			qCnt = atoi( buff );
			step = 4;
		}
		else if( step == 4 ) {	// get query
			std::string q = buff;
			queries.push_back( q );

			if( (int)queries.size() >= qCnt ) {	// output
				int sCnt = getNumberOfSwitches( engines, queries );
				ofs << "Case #" << c << ": " << sCnt << std::endl;

				printf( "Case %d Done!\n", c );
				step = 1;
				c++;
			}
		}
	}

	ifs.close();
	ofs.flush();
	ofs.close();
}


int main(int argc, char** argv )
{
	saveTheUniverse( argv[ 1 ] );
	return 0;
}
