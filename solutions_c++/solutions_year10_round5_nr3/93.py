#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdlib>

#define INF 2000000000

using namespace std;

long long t,iii;
long long n,i,j,p,v,ans,tmp1;
long long m[5000005];
set<long long> S;
set<long long>::iterator it;

int main()
{
    scanf("%I64d",&t);
    for(iii=0;iii<t;iii++)
    {
        scanf("%I64d",&n);
        for(i=0;i<=5000000;i++)
        {
            m[i]=0;
        }
        for(i=0;i<n;i++)
        {
            scanf("%I64d %I64d",&p,&v);
            p+=2500000;
            m[p]=v;
            if(v>1)
            {
                S.insert(p);
            }
        }
        ans=0;
        while(!S.empty())
        {
            it=S.begin();
            tmp1=(*it);
            S.erase(it);
            ans+=(m[tmp1]/2);
            m[tmp1-1]+=(m[tmp1]/2);
            m[tmp1+1]+=(m[tmp1]/2);
            m[tmp1]%=2;
            if(m[tmp1+1]>1)
            S.insert(tmp1+1);
            if(m[tmp1-1]>1)
            S.insert(tmp1-1);
        }
        printf("Case #%I64d: %I64d\n",iii+1,ans);
    }
    return 0;
}
