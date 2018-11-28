#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <iostream>
#include <vector>
#include <string>

typedef uint64_t UINT64;
typedef uint16_t UINT16;
typedef uint8_t  UINT8;

int main( void )
{
    UINT16		index		  = 1;		// result X
    UINT64		T			  = 0;
	UINT16		snapperNumber = 0;		// N
	UINT64		fingerTimes	  = 0;		// K
	bool		flag		  = false;
	
    std::cin >> T;
    do {
		std::cin >> snapperNumber;
		std::cin >> fingerTimes;
		flag = true;
		
		int i = 0;
		for ( i = 0; i < snapperNumber; ++i ) {
			if ( ( fingerTimes & 1 ) == 0 ) {
				flag = false;
				break;
			}
			fingerTimes >>= 1;
		}
		
        printf( "Case #%d: %s\n", index, flag ? "ON" : "OFF" );
		++index;
    } while ( (index - 1 ) != T );
	
	return EXIT_SUCCESS;
}
