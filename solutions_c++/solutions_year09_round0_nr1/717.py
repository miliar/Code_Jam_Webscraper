#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

int iWordLength;
int iWordsNumber;
int iTestsNumber;
vector<string> vsAllWords;

//#define GAWKOWSKI_DEBUG

bool match( const string& sPattern, const string& sWord )
{
    int iStartChar = 0;
    for( unsigned int iCharCnt = 0; iCharCnt < sWord.size(); iCharCnt++ )
    {
        if( sPattern[ iStartChar ] != '(' )
        {
            if( sPattern[ iStartChar ] != sWord[ iCharCnt ] )
                return false;
            else
                iStartChar++;
        }
        else
        {
            iStartChar++;
            bool bWas = false;
            while( sPattern[ iStartChar ] != ')' )
            {
                if( sPattern[ iStartChar ] == sWord[ iCharCnt ] )
                {
                    bWas = true;
                }
                iStartChar++;
            }
            iStartChar++;
            if( bWas == false )
                return false;
        }
    }
    return true;
}
int howManyMatch( const string& sPattern )
{
    int iRez = 0;
    for( unsigned int iWordCnt = 0; iWordCnt < vsAllWords.size(); iWordCnt++ )
    {
        if( match( sPattern, vsAllWords[ iWordCnt ] ) == true )
            iRez++;
    }
    return iRez;
}
int main()
{
    #ifdef GAWKOWSKI_DEBUG
    assert( match("abc", "abd" ) == false );
    assert( match("a", "b" ) == false );
    assert( match("a", "a" ) == true );
    assert( match("(bcdea)", "a") == true );
    assert( match("(bcdefghij)","a") == false );

    assert( match("(ab)(bc)(ca)", "abc") == true );
    assert( match("(ab)(bc)(ca)", "bbc") == true );
    assert( match("(ab)(bc)(ca)", "acd") == false );
    assert( match("(ab)(bc)(ca)", "aaa") == false );
    assert( match("(ab)(bc)(ca)", "cba") == false );
    #else
    char acLiniaWejscia[ 500 ];
    char acWord[ 20 ];
    gets( acLiniaWejscia );
    sscanf( acLiniaWejscia, "%d%d%d", &iWordLength, &iWordsNumber, &iTestsNumber );

    for( int iWordCnt = 0; iWordCnt < iWordsNumber; iWordCnt++ )
    {
        gets( acLiniaWejscia );
        sscanf( acLiniaWejscia, "%s", acWord );
        vsAllWords.push_back( string( acWord ) );

    }
    for( int iTestCnt = 0; iTestCnt < iTestsNumber; iTestCnt++ )
    {
        gets( acLiniaWejscia );
        printf( "Case #%d: %d\n", iTestCnt+1, howManyMatch( string( acLiniaWejscia) ) );
    }
    #endif
    return 0;
}
