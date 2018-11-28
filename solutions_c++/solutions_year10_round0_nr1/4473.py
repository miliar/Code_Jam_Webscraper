#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<queue>
#include<set>
#include<map>
using namespace std;
const int INF=0x7fffffff;
const double eps=(1.0e-9);
const double PI=atan2(0.0,-1.0);
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out_A_small.txt","w",stdout);
    __int64 cas,n,k;
    scanf("%I64d",&cas);
    __int64 base2[50];
    base2[0]=1;
    int i;
    for(i=1;i<=30;i++)
    {
        base2[i]=base2[i-1]*2;
    }
    for(i=1;i<=cas;i++)
    {
        scanf("%I64d%I64d",&n,&k);
        if(k%base2[n]==base2[n]-1)
        {
            printf("Case #%d: ON\n",i);
        }
        else
        {
            printf("Case #%d: OFF\n",i);
        }
    }
    return 0;
}

             
