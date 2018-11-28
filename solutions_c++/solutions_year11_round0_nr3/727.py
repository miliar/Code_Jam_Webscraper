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

        int sum = 0;
        int mini = 1234567;
        int myxor = 0;

        int temp;
        for (int i=0;  i<n; ++i)
        {
            scanf("%d", &temp);
            sum += temp;
            if ( temp < mini )
                mini = temp;
            myxor = myxor ^ temp;
        }
        if (myxor != 0){
            printf("Case #%d: NO\n", caseId);
        }
        else {
            printf("Case #%d: %d\n", caseId, sum - mini);
        }
    }
    return 0;

}
