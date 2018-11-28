#include <cstdio>
#include <cstring>
#include <string>
#include <cassert>
using namespace std;
const int MODULO = 10000;
const string PATTERN = "welcome to code jam";
typedef unsigned int uint;

int licz( const string& sLine )
{
    int Odp[ 501 ][ 19 ];
    memset( Odp, 0, sizeof(Odp) );
    
    for( int uiCnt = sLine.size() - 1; uiCnt >= 0; uiCnt-- )
    {
        if( sLine[ uiCnt ] == PATTERN[ 18 ] )
            Odp[ uiCnt ][ 18 ] = Odp[ uiCnt + 1][ 18 ] + 1;
        else
            Odp[ uiCnt ][ 18 ] = Odp[ uiCnt + 1 ][ 18 ];
    }

    for( int p = 17; p>=0; p-- )
    {
        int iIleZnalazlemDoTejPory = 0;
        for( int s=sLine.size()-1; s>=0; s-- )
        {
            if( sLine[s] == PATTERN[p] )
            {
                iIleZnalazlemDoTejPory += Odp[ s+1 ][ p+1 ];
                iIleZnalazlemDoTejPory %= MODULO;
                Odp[ s ][ p ] = iIleZnalazlemDoTejPory;
            }
            else
                Odp[ s ][ p ] = Odp[ s+ 1 ][ p ];
        }
    }

    return Odp[0][0];
}
int main()
{
    int iTests;
    char smiec;
    scanf( "%d%c", &iTests, &smiec );
    assert( smiec == '\n');
    char acLine[ 502 ];
    for( int iCurrTest = 0; iCurrTest < iTests; iCurrTest++ )
    {
        gets( acLine );
        printf( "Case #%d: %04d\n", iCurrTest+1, licz( string( acLine ) ) );
    }
    return 0;
}
