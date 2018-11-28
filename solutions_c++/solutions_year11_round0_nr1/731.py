#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int testCaseCount = 0;
    scanf( "%d", &testCaseCount );
    for ( int caseId=1; caseId <= testCaseCount; caseId++)
    {
        int allBtnCount = 0;
        printf("Case #%d:",caseId);
        scanf( "%d", &allBtnCount );

        char robot;
        int btnId = 0;

        int bPos = 1;
        int oPos = 1;

        int bActionPoint = 0;
        int oActionPoint = 0;

        int ans = 0;

        for ( int i = 0; i < allBtnCount; ++i )
        {
            scanf( " %c %d", &robot, &btnId );
            if ( robot=='O' ){
                int diff = abs( btnId - oPos ) - oActionPoint;
                if ( diff < 0 )
                {
                    diff = 0;
                }
                ans += diff + 1;
                oPos = btnId;
                oActionPoint = 0;
                bActionPoint += 1 + diff;
            }
            else
            {
                int diff = abs( btnId - bPos ) - bActionPoint;
                if ( diff < 0 )
                {
                    diff = 0;
                }
                ans += diff + 1;
                bPos = btnId;
                bActionPoint = 0;
                oActionPoint += 1 + diff;
            }
        }

        printf(" %d\n", ans);

        fflush(stdout);
    }
    return 0;

}
