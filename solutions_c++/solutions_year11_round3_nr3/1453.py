#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <list>
using namespace std;
list<int> num[10002];
__int64 ss[10002];
bool    mark[10002];

void init()
{
    int i=0, j;
    for(i=1; i<10002; i++)
    {
        for(j=i; j<10002;j+=i)
        {
            num[j].push_front(i);
        }
    }
};

__int64 getlarge(__int64 high, __int64 low, __int64 number)
{
    if( number <= high )
    {
        if(number == high)
            return high;
        __int64 rt = (high/number)*number;
        if(rt < low)
            return -1;
        return rt;
    }
    else
    {
        list<int>::iterator it;
        for(it = num[number].begin(); it != num[number].end(); it++)
        {
            __int64 rt = *it;
            if( rt >= low && rt <= high)
                return rt;
        }
        return -1;
    }
    return -1;
}

int main()
{
    int t;
    int ck;
   freopen("C-small-attempt1.in","r",stdin);
    freopen("google1.out","w",stdout);
        init();
    scanf("%d",&t);
    __int64 mx;
    bool bFind;
    for (ck = 0; ck < t; ck++)
    {
        __int64 n, l, h;
        int i, j;
        bFind = false;
        scanf("%lld%lld%lld",&n,&l,&h);
        memset(mark,0,sizeof(mark));
        for( i=0; i<n; i++)
        {
            scanf("%lld",&ss[i]);
        }
        for(i=l; i<=h; i++)
        {
            for(j=0; j<n; j++)
            {
                bool check = false;
                if(ss[j] >= i)
                {
                    if(ss[j]%i == 0)
                        check = true;
                }
                else
                {
                    if(i%ss[j]== 0)
                        check = true;
                }   
                if(check == false)
                    break;
            }
            if(j>=n)
            {
                bFind = true;
                break;
            }
        }
        if(!bFind)
            printf("Case #%d: NO\n",ck+1);
        else
            printf("Case #%d: %d\n",ck+1,i);
    }
}