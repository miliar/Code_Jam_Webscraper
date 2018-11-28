/* 
 * File:   main.cpp
 * Author: Administrator
 *
 * Created on 2011年5月21日, 上午8:58
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define ALL(c) (c).begin(),(c).end()
#define FIL(c,n) memset(c,n,sizeof(c))

int gcd(int a,int b)
{
    if(!b)
        return a;
    return gcd(b,a%b);
}

int main()
{
    int t;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int pd,pg;
        long long n;
        printf("Case #%d: ",i+1);
        scanf("%I64d%d%d",&n,&pd,&pg);
        if(pg==100||pg==0)
        {
            if(pd!=pg)
                puts("Broken");
            else
                puts("Possible");
            continue;
        }
        int d=gcd(100,pd);
        d=100/d;
        if(d<=n)
            puts("Possible");
        else
            puts("Broken");
    }
    return 0;
}

