#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);freopen("A-large.txt","w",stdout);
    //freopen("B-large.in","r",stdin);freopen("B-large.txt","w",stdout);
    int testCaseCount = 0;
    scanf( "%d", &testCaseCount );
    for ( int caseId=1; caseId <= testCaseCount; caseId++)
    {
        int n = 0;
        scanf("%d", &n);

        int temp;
        int ans = n;
        for (int i=1;  i<=n; ++i)
        {
            scanf("%d", &temp);
            if ( temp == i )
            {
                ans--;
            }
        }

        printf("Case #%d: %.6lf\n", caseId, (double)ans);

    }
    return 0;

}
