#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

const int MAX_N = 100;
const int dirH[] = {-1, +0, +0, +1};
const int dirW[] = {+0, -1, +1, +0};

int Graf[ MAX_N ][ MAX_N ];
char Result[ MAX_N ][ MAX_N ];
int iCurrHeight, iCurrWidth;
int iFirstFreeLetter;
vector< pair<int,int> > vpiiHistory; // (h,w)

void readTest()
{
    scanf( "%d%d", &iCurrHeight, &iCurrWidth );
    for( int iH = 0; iH < iCurrHeight; iH++ )
    {
        for( int iW = 0; iW < iCurrWidth; iW++ )
            scanf( "%d", &Graf[ iH ][ iW ] );
    }
}
void go( int iHeight, int iWidth )
{
    vpiiHistory.push_back( make_pair(iHeight, iWidth) );
    
    int iCurrMin = Graf[ iHeight ][ iWidth ];
    int iWhereCurrMin = -1;
    
    for( int iDirCnt = 0; iDirCnt < 4; iDirCnt++ )
    {
        const int iNewH = iHeight+dirH[ iDirCnt ];
        const int iNewW = iWidth+dirW[ iDirCnt ];
        
        if( iNewH >= 0 && iNewH < iCurrHeight  && iNewW >= 0 && iNewW < iCurrWidth )
        {
            if( iCurrMin > Graf[ iNewH ][ iNewW ] )
            {
                iCurrMin = Graf[ iNewH ][ iNewW ];
                iWhereCurrMin = iDirCnt;
            }
        }
    }
    if( iWhereCurrMin == -1 )
    {
        for( unsigned int iCurrPair = 0; iCurrPair < vpiiHistory.size(); iCurrPair++ )
            Result[ vpiiHistory[ iCurrPair].first ][ vpiiHistory[ iCurrPair ].second ]
                    = 'a' + iFirstFreeLetter;
        vpiiHistory.clear();
        iFirstFreeLetter++;
    }
    else
    {
        const int iNewH = iHeight+dirH[ iWhereCurrMin ];
        const int iNewW = iWidth+dirW[ iWhereCurrMin ];
        
        if( Result[ iNewH ][ iNewW ] == 0 )
            go( iNewH, iNewW );
        else
        {
            for( unsigned int iCurrPair = 0; iCurrPair < vpiiHistory.size(); iCurrPair++ )
                Result[ vpiiHistory[ iCurrPair].first ][ vpiiHistory[ iCurrPair ].second ]
                    = Result[ iNewH ][ iNewW ];
            vpiiHistory.clear();
        }
    }
}
void compute()
{
    memset( Result, 0, sizeof(Result) );
    iFirstFreeLetter = 0;
    
    for( int iH = 0; iH < iCurrHeight; iH++ )
    {
        for( int iW = 0; iW < iCurrWidth; iW++ )
        {
            if( Result[ iH ][ iW ] != 0 )
                continue;
            assert( vpiiHistory.size() == 0 );
            go( iH, iW );
        }
    }
}
void writeResult( int iWhichTest )
{
    printf( "Case #%d:\n", iWhichTest + 1 );
    for( int iH = 0; iH < iCurrHeight; iH++ )
    {
        for( int iW = 0; iW < iCurrWidth - 1; iW++ )
            printf( "%c ", Result[ iH ][ iW ] );
        printf( "%c\n", Result[ iH ][ iCurrWidth -1 ] );
    }
}
int main()
{
    int iTest;
    scanf( "%d", &iTest );
    for( int iTestCnt = 0; iTestCnt < iTest; iTestCnt++ )
    {
        readTest();
        compute();
        writeResult( iTestCnt );
    }
    return 0;
}
