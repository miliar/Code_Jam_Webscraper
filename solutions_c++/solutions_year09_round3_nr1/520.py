#include <cstdio>
#include <map>
#include <cstring>
using namespace std;
typedef unsigned long long ull;

ull power( ull a, ull n )
{
    ull rez = 1;
    ull pot = a;

    while( n > 0 )
    {
        if( n % 2 == 1 )
            rez*=pot;
        pot*=pot;
        n/=2;
    }

    return rez;
}
ull compute( const char* pcNumber )
{
    int znakCyfra[ 256 ];
    int pierwszaWolna = 0;
    for( int i=0; i<256; i++ ) znakCyfra[ i ] = -1;
    
    znakCyfra[ pcNumber[ 0 ] ] = 1;
    const int SZ = strlen( pcNumber );

    for( int iCharPtr = 1; iCharPtr < SZ; iCharPtr++ )
    {
        if( znakCyfra[ pcNumber[ iCharPtr ] ] != -1 )
            continue;
        else
        {
            if( pierwszaWolna == 1 )
                pierwszaWolna++;
            znakCyfra[ pcNumber[ iCharPtr ] ] = pierwszaWolna++;
        }
    }

    ull res = 0;
    ull base;
    if( pierwszaWolna == 0 || pierwszaWolna == 1 )
        base = 2;
    else
        base = pierwszaWolna;
    for( int iCharPtr = 0; iCharPtr < SZ; iCharPtr++ )
    {
        const ull cyfra = znakCyfra[ pcNumber[ SZ-1 - iCharPtr ] ];
        res += ( cyfra * power( base ,iCharPtr ) );
    }
    return res;

}
int main()
{
    int iTests;
    scanf( "%d", &iTests);
    for( int iTestCnt = 1; iTestCnt <= iTests; iTestCnt++ )
    {
        char acNumber[62];
        scanf( "%s", acNumber );
        printf( "Case #%d: %llu\n", iTestCnt, compute( acNumber ) );
    }
    return 0;
}