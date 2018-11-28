#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    int i,n,test,Case=1,m,x,k,cnt;

    scanf("%d",&test);
    while(test--)
    {
        scanf("%d %d",&n,&k);
        m=1<<n;
        //printf("%d\n",m);
        x=k%m;
        cnt=0;
        while(x)
        {
            if(x%2==1)
                cnt++;
            x/=2;
        }
        if(cnt == n)
            printf("Case #%d: ON\n",Case++);
        else printf("Case #%d: OFF\n",Case++);
    }

    return 0;
}
