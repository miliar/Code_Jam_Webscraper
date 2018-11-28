#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>

typedef std::vector<std::string> StringVector;

int getCount( std::istream &is );
bool getStrings( std::istream &is, StringVector &strings );
int minimumSwitches( StringVector &engines, StringVector &queries );
int nextBest( StringVector &engines, StringVector &queries, int queryStart );

int main( int argc, char *argv[] )
{
    for( int i = 1; i < argc; ++i )
    {
        std::ifstream ifs( argv[i] );
        if( ifs.good() )
        {
            int numberOfCases = getCount( ifs );
            for( int caseNum = 1; caseNum <= numberOfCases; ++caseNum )
            {
                StringVector engines;
                StringVector queries;
                if( getStrings( ifs, engines ) && getStrings( ifs, queries ) )
                {
                    int min = minimumSwitches( engines, queries ) - 1; // don't count the first engine choice
                    std::cout << "Case #" << caseNum << ": " << min << std::endl;
                }
                else
                {
                    std::cerr << "Error reading data for case #" << caseNum << std::endl;
                }
            }
        }
        else
        {
            std::cerr << "Unable to open file: " << argv[i] << std::endl;
        }
    }
    return 0;
}

int getCount( std::istream &is )
{
    std::string line;
    std::getline( is, line );
    std::stringstream numStr( line );
    int count;
    if( numStr >> count )
        return count;

    return -1;
}

bool getStrings( std::istream &is, StringVector &strings )
{
    if( !is.good() || is.eof() ) return false;
    int count = getCount( is );
    if( -1 == count ) return false;

    for( ; count > 0; --count )
    {
        if( is.eof() ) return false;
        std::string line;
        std::getline( is, line );
        strings.push_back( line );
    }

    return true;
}

int minimumSwitches( StringVector &engines, StringVector &queries )
{
    if( 0 == queries.size() ) return 1;

    int switches = 0;
    for( int bestQ = 0; bestQ < queries.size(); )
    {
        bestQ = nextBest( engines, queries, bestQ );
        ++switches;
    }
    return switches;
}

int nextBest( StringVector &engines, StringVector &queries, int queryStart )
{
    int bestE = 0;
    int bestQ = 0;
    for( int ei = 0; ei < engines.size(); ++ei )
    {
        for( int qi = queryStart; (qi < queries.size()) && (engines[ei] != queries[qi]); ++qi )
        {
            if( qi > bestQ )
            {
                bestE = ei;
                bestQ = qi;
            }
        }
    }
    return bestQ + 1;
}
