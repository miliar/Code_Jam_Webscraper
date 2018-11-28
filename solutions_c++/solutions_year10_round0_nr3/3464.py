#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

/*

iProblem

Roller coasters are so much fun! It seems like everybody who visits the theme park wants to ride the roller coaster. Some people go alone; other people go in groups, and don't want to board the roller coaster unless they can all go together. And everyone who rides the roller coaster wants to ride again. A ride costs 1 Euro per person; your job is to figure out how much money the roller coaster will make today.

The roller coaster can hold k people at once. People queue for it in groups. Groups board the roller coaster, one at a time, until there are no more groups left or there is no room for the next group; then the roller coaster goes, whether it's full or not. Once the ride is over, all of its passengers re-queue in the same order. The roller coaster will run R times in a day.

For example, suppose R=4, k=6, and there are four groups of people with sizes: 1, 4, 2, 1. The first time the roller coaster goes, the first two groups [1, 4] will ride, leaving an empty seat (the group of 2 won't fit, and the group of 1 can't go ahead of them). Then they'll go to the back of the queue, which now looks like 2, 1, 1, 4. The second time, the coaster will hold 4 people: [2, 1, 1]. Now the queue looks like 4, 2, 1, 1. The third time, it will hold 6 people: [4, 2]. Now the queue looks like [1, 1, 4, 2]. Finally, it will hold 6 people: [1, 1, 4]. The roller coaster has made a total of 21 Euros!

Input

The first line of the input gives the number of test cases, T. T test cases follow, with each test case consisting of two lines. The first line contains three space-separated integers: R, k and N. The second line contains N space-separated integers gi, each of which is the size of a group that wants to ride. g0 is the size of the first group, g1 is the size of the second group, etc.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of Euros made by the roller coaster.

Limits

1 ≤ T ≤ 50.
gi ≤ k.

Small dataset

1 ≤ R ≤ 1000.
1 ≤ k ≤ 100.
1 ≤ N ≤ 10.
1 ≤ gi ≤ 10.
Large dataset

1 ≤ R ≤ 108.
1 ≤ k ≤ 109.
1 ≤ N ≤ 1000.
1 ≤ gi ≤ 107.
*/


typedef std::vector<std::string> StringVector;
int getInt( std::istream &is );
bool getStrings( std::istream &is, StringVector &strings );


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
                int R;
                int k;
                int N;

                if( !(ifs >> R) || !(ifs >> k) || !(ifs >> N) )
                {
                    std::cerr << "Unable to read values for case #" << caseNum << std::endl;
                    return -1;
                }
                std::string nl;
                std::getline( ifs, nl ); // skip the newline

                std::vector<int> groups(N,0);
                int total = 0;
                for( int i = 0; i < N; ++i )
                {
                    int group;
                    if( !(ifs >> group ) )
                    {
                        std::cerr << "Unable to read values for case #" << caseNum << std::endl;
                        return -2;
                    }
                    groups[i] = group;
                    total += group;
                }
                std::getline( ifs, nl ); // skip the newline

                int euros = 0;

                if( total <= k )
                {
                    euros = R * total;
                }
                else
                {
                    int head = 0;
                    for( ; R > 0; --R )
                    {
                        int cnt = 0;
                        bool full = false;
                        while( !full )
                        {
                            int grp = groups[head];
                            if( (cnt + grp) <= k )
                            {
                                cnt += grp;
                                euros += grp;
                                ++head;
                                if( head >= N )
                                    head = 0;
                            }
                            else
                            {
                                full = true;
                            }
                        }
                    }
                }
                std::cout << "Case #" << caseNum << ": " << euros << std::endl;
            }
        }
    }

    return 0;
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

