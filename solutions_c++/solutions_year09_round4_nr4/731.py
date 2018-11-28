#include <cstdio>
#include <cassert>
#include <vector>
#include <cmath>
using namespace std;
struct Plant
{
    int m_X, m_Y, m_R;
    Plant(int x, int y, int r)
    {
        m_X = x;
        m_Y = y;
        m_R = r;
    }
};
double licz( vector<Plant>& vpPlants )
{
    if( vpPlants.size() == 1 )
        return vpPlants[ 0 ].m_R;
    if( vpPlants.size() == 2 )
        return max( vpPlants[0].m_R, vpPlants[1].m_R );
    
    double dRes = 10000000.0;
    for( int i=0; i<3; i++ )
    {
        const Plant& a = vpPlants[(i+1)%3];
        const Plant& b = vpPlants[(i+2)%3];
        const int iX = a.m_X - b.m_X;
        const int iY = a.m_Y - b.m_Y;
        dRes = min( dRes,
                max( (double)vpPlants[i].m_R,  (a.m_R + b.m_R + sqrt( (double)(iX*iX)+(double)(iY*iY)) )/(double)2.0 )
                );
    }
    return dRes;
}
int main()
{
    int iCases;
    scanf( "%d", &iCases );

    for( int iCaseCnt = 1; iCaseCnt <= iCases; iCaseCnt++ )
    {
        int iPlants;
        scanf( "%d", &iPlants );
        assert( iPlants <= 3 );

        vector<Plant> vpPlants;
        for( int iPlantCnt = 0; iPlantCnt < iPlants; iPlantCnt++ )
        {
            int X,Y,R;
            scanf( "%d%d%d", &X,&Y,&R );
            Plant p(X,Y,R);

            vpPlants.push_back( p );
        }

        printf( "Case #%d: %.6lf\n", iCaseCnt, licz( vpPlants ) );
    }
    return 0;
}
