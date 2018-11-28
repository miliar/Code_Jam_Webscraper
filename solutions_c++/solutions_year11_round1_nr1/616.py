#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;
long long n;
long long pd,pg;
int cases = 1;
int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);
    long long  t;
    long long i;
    cin>>t;
    bool flag;
    while(t--)
    {
        flag = 1;
        cin>>n>>pd>>pg;
        if(pg==100 && pd!=100) flag = 0;
        if(pg==0 && pd!=0) flag = 0;
        if(n<100)
        {
            for(i=1;i<=n;i++)
            {
                if(i*pd%100==0)
                    break;
            }
            if(i==n+1) flag = 0;
        }
        if(flag) printf("Case #%d: Possible\n",cases++);
        else printf("Case #%d: Broken\n",cases++);
    }
	return 0;
}
