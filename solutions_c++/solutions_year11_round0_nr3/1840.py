#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <functional>
#include <stack>
#include <cmath>
#define MMset(a,b) memset(a,b,sizeof(a))
#define max(a,b)   ((a)>(b)?(a):(b))
#define min(a,b)   ((a)<(b)?(a):(b))
#define eps 1e-8
using namespace std;
int T,N;
int main()
{
    
    freopen("C-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d",&N);
        int num,mins=0x7fffffff,sum=0,ans=0;
        for (int i=0;i<N;i++)
        {
            scanf("%d",&num);
            ans^=num;
            sum+=num;
            mins=min(num,mins);
        }
        if (!ans) printf("Case #%d: %d\n",cas,sum-mins);
        else      printf("Case #%d: NO\n",cas);
    }
}
