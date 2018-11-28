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
#define oo 1000000000
using namespace std;

map<int, int > allsums;
int N;
int S[600];
void printmask(int m)
{
    for(int i=0;i<N;i++)
        if((m>>i)&1)
            printf("%d ",S[i]);
    printf("\n");
}

void solve()
{
    allsums.clear();
    for(int mask=1;mask<(1<<N);mask++)
    {
        int summ=0;
        for(int j=0;j<N;j++)
            if((mask>>j)&1)
                summ+=S[j];
        if(allsums.find(summ)!=allsums.end())
        {
            printmask(allsums[summ]);
            printmask(mask);
            return;
        }
        allsums[summ]=mask;
    }
    printf("IMPOSSIBLE\n");
}


int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d",&N);
        printf("Case #%d:\n",t);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&S[i]);
        }
        solve();

        
        
    }
}
