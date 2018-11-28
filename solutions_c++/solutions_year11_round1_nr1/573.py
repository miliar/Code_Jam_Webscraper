#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <stack>
#include <algorithm>
using namespace std;


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //
    int Tests;
    scanf("%d",&Tests);
    for(int Test=1;Test<=Tests;Test++)
    {
        printf("Case #%d: ", Test);
        //
        long long n,pd,pg;
        scanf("%lld%lld%lld",&n,&pd,&pg);
        if(pg==0)
            printf("%s\n", pd==0 ? "Possible" : "Broken");
        else if(pg==100)
            printf("%s\n", pd==100 ? "Possible" : "Broken");
        else
        {
            int x=100;
            long long t=pd;
            if(t%2==0)
            {
                t/=2;
                x/=2;
            }
            if(t%2==0)
            {
                t/=2;
                x/=2;
            }
            if(t%5==0)
            {
                t/=5;
                x/=5;
            }
            if(t%5==0)
            {
                t/=5;
                x/=5;
            }
            printf("%s\n", x<=n ? "Possible" : "Broken");
        }
    }
    return 0;
}
