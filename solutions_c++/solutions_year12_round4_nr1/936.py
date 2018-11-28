#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <iostream>
#define ll long long
using namespace std;

ll d[10002],l[10002];
ll D;

ll maxD[10002];
int N;
bool solve()
{
    maxD[1]=d[1];
    ll currmaxx = maxD[1];
    if(d[1]+maxD[1]>=D)
        return true;
    for(int i=2;i<=N;i++)
    {
        maxD[i]=-1;
        for(int j=1;j<=i-1;j++)
        {
            if(d[j]+maxD[j]>=d[i])
                maxD[i]=max(maxD[i],  min(d[i]-d[j], l[i])); 
        }
        
        if(maxD[i]==-1)
            return false;
        if(d[i]+maxD[i]>=D)
            return true;
    }
    if(d[N]+maxD[N]>=D)
        return true;
    return false;
           
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d",&N);
        for(int i=1;i<=N;i++)
            scanf("%lld%lld",&d[i],&l[i]);
        scanf("%lld",&D);
        if(solve())
            printf("Case #%d: YES\n",t);
        else
            printf("Case #%d: NO\n",t);
     
        
        
    }
}