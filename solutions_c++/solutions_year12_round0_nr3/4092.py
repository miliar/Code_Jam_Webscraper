#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <functional>
#include <utility>//pair
#include <iomanip>
using namespace std;

bool f[2000005];

int main()
{\
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int i,n,a,b,t,m,len,cou,len1,k,ca = 1;
    long long ans;
    scanf("%d",&n);
    while(n--)
    {
        ans = 0;
        memset(f,0,sizeof(f));
        scanf("%d%d",&a,&b);
        for( i = a; i <= b; ++i)
        {
            cou = 1;
            if(!f[i])
            {
                f[i] = 1;
                cou = 1;
                m = i;
                len = 0;
                while(m)
                {
                    m /= 10;
                    len++;
                }
                k = i;
                while(1)
                {
                    if(m == i) break;
                    m = k;
                    t = m % 10;
                    m /= 10;
                    m = t * (int)pow(10.0,len*1.0 - 1) + m;
                    len1 = 0;
                    k = m;
                    if(!f[m] && m <= b && m >= a)
                    {
                        while(m)
                        {
                            m /= 10;
                            len1++;
                        }
                        if(len1 == len)
                        {
                            f[k] = 1;
                            cou++;
                        }    
                    }
                }    
            }
            ans += cou * (cou - 1) / 2;
        }
        printf("Case #%d: %d\n",ca++,ans);
    }
    return 0;
}










