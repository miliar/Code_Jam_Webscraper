#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
const int INF = 0x7fffffff;

int licz( const int* permutation, const vector<int>& viPrisoners, int iCells )
{
    int iRes = 0;
    bool bPrisoners[ 100 ];
    for( int i=0; i<iCells; i++ ) bPrisoners[ i ] = true;
    
    for( unsigned int uiCnt = 0; uiCnt < viPrisoners.size(); uiCnt++ )
    {
        const int iCurrPrison = viPrisoners[ permutation[ uiCnt ] - 1];
        int iLewyIndex = iCurrPrison - 2;
        int iPrawyIndex = iCurrPrison;
        bPrisoners[ iCurrPrison - 1 ] = false;
        while( iLewyIndex >= 0 && bPrisoners[ iLewyIndex ] == true )
        {
            iRes++;
            iLewyIndex--;
        }

        while( iPrawyIndex < iCells && bPrisoners[ iPrawyIndex ] == true )
        {
            iRes++;
            iPrawyIndex++;
        }
    }

    return iRes;
}
int compute( int iCells, const vector<int>& viPrisoners )
{
    int permutation[5] = {1,2,3,4,5};
    int res = INF;
    do
    {
        //for( int i=0; i<viPrisoners.size(); i++ ) printf("%d ", permutation[i] );
        //printf("\n");
        res = min( res, licz( permutation, viPrisoners, iCells ) );
    }while( next_permutation( permutation, permutation+viPrisoners.size() ) );

    return res;

}
int main()
{
    int iTests;
    scanf( "%d", &iTests );
    for( int iTestCnt = 1; iTestCnt <= iTests; iTestCnt++ )
    {
        int iCells, iPrisonersNum;
        scanf( "%d%d", &iCells, &iPrisonersNum );
        vector<int> viPrisoners;
        for( int iPriCnt = 0; iPriCnt < iPrisonersNum; iPriCnt++ )
        {
            int iTemp;
            scanf( "%d", &iTemp );
            viPrisoners.push_back( iTemp );
        }
        printf("Case #%d: %d\n", iTestCnt, compute( iCells, viPrisoners ) );
    }
}

