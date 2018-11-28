#include <algorithm>
#include <vector>
#include <cassert>
#include <cstring>
#include <string>
using namespace std;
int iLines;
bool jestDobry( int etap, const string& s )
{
    for( int i=etap+1; i<s.size(); i++ )
    {
        if( s[ i ] == '1' )
            return false;
    }
    return true;
}
int licz( vector<string>& vsMacierz )
{
    int iOdp = 0;
    const int KONIEC = vsMacierz.size();
    for( int i=0; i<KONIEC; i++ )
    {
        for( int j=0; j<vsMacierz.size(); j++ )
        {
            if( jestDobry( i, vsMacierz[ j ] ) )
            {
                iOdp += j;
                //swap( vsMacierz[i], vsMacierz[j] );
                vsMacierz.erase( vsMacierz.begin() + j );
                break;
            }
        }
    }
    return iOdp;
}
int main()
{
    int iTests;
    scanf( "%d\n", &iTests );
    for( int iTestCnt = 1; iTestCnt <= iTests; iTestCnt++ )
    {
        scanf( "%d\n", &iLines );
        int iTemp;
        char cInput[ 45 ];

        vector<string> vsMacierz;
        for( int iWiersz = 0; iWiersz < iLines; iWiersz++ )
        {
            gets( cInput );
            string sTemp( cInput );
            vsMacierz.push_back( sTemp );

        }
        printf( "Case #%d: %d\n", iTestCnt, licz( vsMacierz ) );

    }
}

