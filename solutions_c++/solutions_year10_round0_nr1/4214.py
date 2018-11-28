#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

/*
Problem

The Snapper is a clever little gadget that, on one side, plugs into a power socket and, on the other side, exposes a power socket for plugging in a light or other device.

When the Snapper is in the ON state and is receiving power from the input socket, then the connected device is receiving power as well. When you snap your fingers, the Snapper toggles between the ON and OFF states. Of course, snapping your fingers only has an effect if the Snapper is plugged in and is receiving power from the socket.

In hopes of destroying the universe by means of a singularity, I have purchased N Snapper devices and chained them together by plugging the first one into a power socket, the second one into the first one, and so on. The light is plugged into the Nth Snapper.

Initially, all the Snappers are in the OFF state, so only the first one is receiving power from the socket, and the light is off. I snap my fingers once, which toggles the first Snapper into the ON state and gives power to the second one. I snap my fingers again, which toggles both Snappers and then promptly cuts power off from the second one, leaving it in the ON state, but with no power. I snap my fingers the third time, which toggles the first Snapper again and gives power to the second one. Now both Snappers are in the ON state, and if my light is plugged into the second snapper it will be on.

I keep doing this for hours. Will the light be on or off after I have snapped my fingers K times? The light is on if and only if it's receiving power from the Snapper it's plugged into.

Input

The first line of the input gives the number of test cases, T. T lines follow. Each one contains two integers, N and K.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either "ON" or "OFF", indicating the state of the light bulb.

Limits

1 ≤ T ≤ 10,000.

Small dataset

1 ≤ N ≤ 10;
0 ≤ K ≤ 100;

Large dataset

1 ≤ N ≤ 30;
0 ≤ K ≤ 108;
*/


typedef std::vector<std::string> StringVector;
int getInt( std::istream &is );
bool getStrings( std::istream &is, StringVector &strings );
int lastWithPower( std::vector<bool> &snappers );


int main( int argc, char *argv[] )
{
    if( argc < 2 )
    {
        std::cerr << "Usage: " << argv[0] << " <input file>" << std::endl;
        return -1;
    }

    for( int i = 1; i < argc; ++i )
    {
        std::ifstream ifs( argv[i] );
        if( ifs.good() )
        {
            int numberOfCases = getInt( ifs );
            for( int caseNum = 1; caseNum <= numberOfCases; ++caseNum )
            {
                int numSnappers;
                int numSnaps;
                bool lightOn = false;

                if( !(ifs >> numSnappers) || !(ifs >> numSnaps) )
                {
                    std::cerr << "Unable to read N and K for case #" << caseNum << std::endl;
                    return -1;
                }
                std::string nl;
                std::getline( ifs, nl ); // skip the newline so we're ready for the next test case

                std::vector<bool> snappers( numSnappers, false );

                for( ; numSnaps > 0; --numSnaps )
                {
                    int last = lastWithPower( snappers );

                    for( int i = 0; i <= last; ++i )
                    {
                        snappers[i] = !snappers[i];
                    }
                }
                if( (lastWithPower( snappers ) == (numSnappers-1))
                    && snappers[ snappers.size() - 1 ] )
                    lightOn = true;
                std::cout << "Case #" << caseNum << ": " << (lightOn?"ON":"OFF") << std::endl;
            }
        }
    }

    return 0;
}

int lastWithPower( std::vector<bool> &snappers )
{
    int last; // last one with power
    for( int i = 0; i < snappers.size(); ++i )
    {
        last = i;
        if( !snappers[i] )
            break;
    }
    return last;
}

int getInt( std::istream &is )
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
    int count = getInt( is );
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

