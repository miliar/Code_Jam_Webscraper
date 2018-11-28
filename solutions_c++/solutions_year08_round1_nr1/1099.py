#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>
#include <algorithm>

int getCount( std::istream &is )
{
    int cnt;
    if( is >> cnt )
        return cnt;
    return -1;
}

bool getDouble( std::istream &is, double &num )
{
    if( is >> num )
        return true;
    return false;
}

int main( int argc, char *argv[] )
{
    std::ifstream ifs( argv[1] );

    if( !ifs.good() )
    {
        std::cerr << "Error opening file: " << argv[1] << std::endl;
        return -1;
    }

    int numCases = getCount( ifs );
    for( int caseNum = 1; caseNum <= numCases; ++caseNum )
    {
        int n = getCount( ifs );
        std::vector<int> vec1;
        std::vector<int> vec2;
        for( int i = 0; i < n; ++i )
        {
            int in;
            if( !(ifs >> in) )
            {
                std::cerr << "Error reading in vector 1: " << i << std::endl;
                return -1;
            }
            vec1.push_back( in );
        }
        for( int i = 0; i < n; ++i )
        {
            int in;
            if( !(ifs >> in) )
            {
                std::cerr << "Error reading in vector 2: " << i << std::endl;
                return -1;
            }
            vec2.push_back( in );
        }

        std::sort( vec1.begin(), vec1.end(), std::less<int>() );
        std::sort( vec2.begin(), vec2.end(), std::greater<int>() );

        int sum  = 0;
        for( int i = 0; i < n; ++i )
        {
            sum += vec1[i] * vec2[i];
        }
        std::cout << "Case #" << caseNum << ": " << sum << std::endl;
    }
    return 0;
}
