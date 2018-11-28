using namespace std;

#include <iostream>
#include <string>
#include <map>
#include <list>
#include <iostream>
#include <vector>


void solvecase( int curcase )
{
    int nSwaps = 0; 
    int totalChicks = 0; 
    int nImpossible = 0; 

    int N , K , B , T; 

    std::cin >> N; 
    std::cin >> K;
    std::cin >> B; 
    std::cin >> T; 

    int ii, jj; 

    std::vector< int > positions; 
    std::vector< int > velocities; 
    std::vector< float > neededtime; 

    float time; 
    
    totalChicks = N; 
    for( ii = 0; ii < N; ++ii ){
        std::cin >> jj; 
        positions.push_back( jj );
    }
    
    for( ii = 0; ii < N; ++ii ){
        std::cin >> jj; 
        velocities.push_back( jj );
        time = ( (float)( B - positions[ii] ) / velocities[ii] ); 
        if( time > T ) 
            ++nImpossible; 
            
        neededtime.push_back( time ); 
    }

    if( totalChicks - nImpossible < K ){
        std::cout << "Case #" << (curcase +1) << ": IMPOSSIBLE" << std::endl;
        return; 
    }

    std::vector< float >::reverse_iterator rit; 
    int partialsum = 0; 
    rit = neededtime.rbegin(); 

    int entered = 0;  
    while( rit != neededtime.rend() && 
           entered < K )
    {
        time = *rit; 
        if( time <= T ){
            nSwaps += partialsum;
            ++entered; 
        }else{
            ++partialsum; 
        }
        rit++; 
    }

    std::cout << "Case #" << (curcase +1) << ": " << nSwaps << std::endl;
}


int main( int argc, char* argv[] )
{

    int ncases, curcase;

    std::cin >> ncases; 

    for( curcase = 0; curcase < ncases; ++curcase ){
        solvecase( curcase ); 
    }

    return 0;
}
