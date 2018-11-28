#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int main()
{
    freopen("A-small-attempt6.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    long long n;
    int w,p1,p2,i,c=1,j;
    bool f;
    scanf("%d",&w);
    while(w--)
    {
        scanf("%lld%d%d",&n,&p1,&p2);
        if(n<100)
        {
            f=0;
            for( i=0; i<=n; ++i)
            {
                for( j=0; j<=i; ++j)
                {
                    if(i==0 || j==0) 
                    {
                        if(p1==0) f=1;
                    }    
                    else if((j*100)%i==0 && p1==(j*100/i)) 
                    {
                        f=1;
                        break;
                    }    
                }    
            }
            if(!f)
            {
                printf("Case #%d: Broken\n",c++);
                continue;
            } 
        }
        if(p1!=100 && p2==100) printf("Case #%d: Broken\n",c++);
        else if(p1!=0 && p2==0) printf("Case #%d: Broken\n",c++);
        else printf("Case #%d: Possible\n",c++);
    }
    return 0;
}









