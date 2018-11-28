#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <iostream>
#include <vector>
#include <string>

typedef uint64_t UINT64;
typedef uint16_t UINT16;

typedef std::vector< UINT64 > NumberQueue;


int main( void )
{
	
    UINT64		total		 = 0;		// result Y
    UINT16		index		 = 1;		// result X
    UINT64		dayRoller	 = 0;		// R
    UINT64		oneTimeLimit = 0;		// N
    UINT64		T			 = 0;
    UINT16		maxRide      = 0;		// k

    std::cin >> T;
	

    do {
		
        std::cin >> dayRoller;
        std::cin >> maxRide;
        std::cin >> oneTimeLimit;
		
        NumberQueue crewNumber( oneTimeLimit, 0 );
        NumberQueue::iterator iter;
		

        for (  iter = crewNumber.begin(); iter != crewNumber.end(); ++iter ) {
            std::cin >> *iter;
        }
		

        iter = crewNumber.begin();

        for (  UINT16 testLoop = 0; testLoop < dayRoller; ++testLoop ) {
			
            UINT64 crew = 0;
			NumberQueue::iterator start = iter;
			
            while( ( crew + *iter ) <= maxRide ) {
                crew += *iter;

                ++iter;
                if ( iter == crewNumber.end() ) {
                    iter = crewNumber.begin();
                }
				
				if ( start == iter ) {
					break;
				}
            }
            total += crew;
        }
		
        printf( "Case #%d: %lld\n", index, total );
        total = 0;
        ++index;
		
    } while ( (index - 1 ) != T );
	
    return EXIT_SUCCESS;
	
}

