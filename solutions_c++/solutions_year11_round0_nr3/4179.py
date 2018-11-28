#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>

#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <iomanip>
#include <ctime>

using namespace std;

int coin[1100];

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);

    int i,j,test,Case=1,n,sum,cnt;

    scanf("%d",&test);
    while(test--)
    {
        scanf("%d",&n);
        sum=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&coin[i]);
            sum=sum+coin[i];
        }
        sort(&coin[0],&coin[n]);

        cnt=0;
        for(i=0;i<n;i++)
        {
            cnt=cnt^coin[i];
        }
        if(cnt==0)
        {
            sum=sum-coin[0];
            printf("Case #%d: %d\n",Case++,sum);
        }
        else
        {
            printf("Case #%d: NO\n",Case++);
        }
    }

    return 0;
}
