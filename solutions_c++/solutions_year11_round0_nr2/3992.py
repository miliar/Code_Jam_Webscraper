#include "stdio.h"
#include "stdlib.h"

const int numLetters = 26;

static int mapCharacterToIndex(const char capitalLetter) {
    return capitalLetter - 'A';
}

void main() {
    const int maxT = 100;
    const int maxC = 36;
    const int maxD = 28;
    const int maxN = 100;

    FILE *input = fopen( "input.txt", "rt" );
    FILE *output = fopen( "output.txt", "wt" );

    int T;
    fscanf( input, "%i\n", &T );

    for( int t = 0 ; t < T ; t++ ) {
        char combineMap[numLetters][numLetters] = { 0 };
        bool opposedPairTable[numLetters][numLetters] = { false };

        char invokeList[maxN+1] = {0};
        int invokeListSize = 0;

        // read configuration
        {
            int C;
            fscanf( input, "%i", &C );

            for( int c = 0 ; c < C ; c++ ) {
                char combineTriple[4];
                fscanf( input, "%3s", combineTriple );

                const int elementA = mapCharacterToIndex(combineTriple[0]);
                const int elementB = mapCharacterToIndex(combineTriple[1]);
                combineMap[ elementA ][ elementB ] = combineMap[ elementB ][ elementA ] = combineTriple[2];
            }

            int D;
            fscanf( input, "%i", &D );
    
            for( int d = 0 ; d < D ; d++ ) {
                char opposedPair[3];
                fscanf( input, "%2s", opposedPair );

                const int elementA = mapCharacterToIndex(opposedPair[0]);
                const int elementB = mapCharacterToIndex(opposedPair[1]);

                opposedPairTable[elementA][elementB] = opposedPairTable[elementB][elementA] = true;
            }

            int N;
            fscanf( input, "%i", &N );

            fscanf( input, "%s", invokeList );
            invokeListSize = N;
        }

        char elementList[ maxN ];
        int elementListSize = 0;

        int elementCounter[ numLetters ] = { 0 };

        for( int n = 0 ; n < invokeListSize ; n++ ) {
            // invoke element (elementListSize points to new element)
            elementList[elementListSize] = invokeList[n];

            // combine to new pair?
            if( elementListSize > 0 ) {
                const int elementA = mapCharacterToIndex(elementList[elementListSize-1]);
                const int elementB = mapCharacterToIndex(elementList[elementListSize]);
                const char combineElement = combineMap[elementA][elementB];

                if( combineElement ) {
                    // remove previous to last element (decrease counter)
                    {
                        const int element = mapCharacterToIndex( elementList[--elementListSize] );
                        elementCounter[ element ]--;
                    }

                    // (elementListSize points to current element)
                    elementList[elementListSize] = combineElement;
                }
            }

            // increase element counter for the current element
            {
                const int element = mapCharacterToIndex( elementList[elementListSize] );
                elementCounter[ element ]++;
            }

            // checks the opposed list
            const int elementIndex = mapCharacterToIndex(elementList[elementListSize]);
            bool clearElements = false;

            for( int letter = 0 ; letter < numLetters ; letter++ ) {
                if( opposedPairTable[elementIndex][letter] && elementCounter[ letter ] > 0 ) {
                    clearElements = true;
                    break;
                }
            }

            if( clearElements ) {
                // (elementListSize points to next element)
                elementListSize = 0;

                // clear elementCounter
                for( int letter = 0 ; letter < numLetters ; letter++ ) {
                    elementCounter[ letter ] = 0;
                }
            }
            else {
                // (elementListSize points to next element)
                elementListSize++;
            }

            // (elementListSize points to next element)
        }

        // output result
        fprintf( output, "Case #%i: [", t + 1 );
        for( int i = 0 ; i < elementListSize - 1; i++ ) {
            fprintf( output, "%c, ", elementList[i] );
        }
        if( elementListSize > 0 ) {
            fprintf( output, "%c", elementList[elementListSize - 1] );
        }
        fprintf( output, "]\n" );
    }

    fclose( output );
    fclose( input );
}
