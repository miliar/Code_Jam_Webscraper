#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>

typedef std::vector<std::pair<int,int> > TripVector;

int getCount( std::istream &is );
bool getTimes( std::istream &is, int count, TripVector &times );
void printTimes( std::ostream &os, const TripVector &times );
void sortTimes( TripVector &times );
void checkTimes( const TripVector &A, const TripVector &B, int turnAround, int &startB );

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
                int turnAround;
                int NA, NB;

                if( ifs >> turnAround && ifs >> NA && ifs >> NB  )
                {
                    TripVector Atrips;
                    TripVector Btrips;
                    if( getTimes( ifs, NA, Atrips ) && getTimes( ifs, NB, Btrips ) )
                    {
                        int startA = Atrips.size();
                        int startB = Btrips.size();

                        if( 0 == NA ) startB = Btrips.size();
                        if( 0 == NB ) startA = Atrips.size();
                        if( (NA > 0) && (NB > 0) )
                        {
                            sortTimes( Atrips );
                            sortTimes( Btrips );
                            checkTimes( Atrips, Btrips, turnAround, startB );
                            checkTimes( Btrips, Atrips, turnAround, startA );
                        }
                        std::cout << "Case #" << caseNum << ": " << startA << " " << startB << std::endl;
                    }
                    else
                    {
                        std::cerr << "Error reading trip data for case #" << caseNum << std::endl;
                    }
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

int getTime( std::istream &is )
{
    int hours;
    int minutes;
    char colon;

    if( is >> hours && is >> colon && is >> minutes && (colon == ':') )
        return (hours * 60) + minutes;

    return -1;
}

bool getTimes( std::istream &is, int count, std::vector< std::pair<int,int> > &times )
{
    for( int i = 0; i < count; ++i )
    {
        int start = getTime( is );
        int finish = getTime( is );
        times.push_back( std::pair<int,int>( start, finish ) );
    }
    return true;
}

static bool sortTimePairs( const std::pair<int,int> &lhs, const std::pair<int,int> &rhs )
{
    if( lhs.first == rhs.first )
        return lhs.second < rhs.second;
   return lhs.first < rhs.first;
}

void sortTimes( TripVector &times )
{
    for( int i = 0; i < times.size(); ++i )
    {
        std::sort( times.begin(), times.end(), sortTimePairs );
    }
}

std::string timeToString( int time )
{
    int hours = time / 60;
    int minutes = time - (hours * 60);
    std::stringstream str;
    str << ((hours < 10)?"0":"") << hours << ":" << ((minutes < 10)?"0":"") << minutes;
    return str.str();
}

void printTimes( std::ostream &os, const TripVector &times )
{
    for( int i = 0; i < times.size(); ++i )
    {
        int start = times[i].first;
        int end = times[i].second;
        os << timeToString( start ) << " " << timeToString( end ) << std::endl;
    }
}

void checkTimes( const TripVector &A, const TripVector &B, int turnAround, int &startB )
{
    TripVector Btimes( B );
    for( int ia = 0; ia < A.size(); ++ia )
    {
        int endTime = A[ia].second + turnAround;
        for( int ib = 0; ib < Btimes.size(); ++ib )
        {
            if( endTime <= Btimes[ib].first )
            {
                TripVector::iterator itRemove = Btimes.begin() + ib;
                Btimes.erase(itRemove);
                --ib;
                --startB;
                break;
            }
        }
    }
}
