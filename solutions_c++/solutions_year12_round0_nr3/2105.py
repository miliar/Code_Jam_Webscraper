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
using namespace std;
long long tenpow[20];
int numdigs(int x)
{
    int d=0;
    while(x)
    {
        d++;
        x/=10;
    }
    return d;
}
int main()
{
    tenpow[0]=1;
    for(int i=1;i<=15;i++)
        tenpow[i]=tenpow[i-1]*10;
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int low,high;
        scanf("%d%d",&low,&high);
        int d=numdigs(low);
        long long numpairs=0;
        for(int n=low;n<=high;n++)
        {
            set<int> currset;
            for(int pivot=1;pivot<=d-1;pivot++)
            {
                int m = n/tenpow[pivot]+tenpow[d-pivot]*(n%tenpow[pivot]);
                if(m>n && m<=high)
                    currset.insert(m);
            }
            numpairs+=currset.size();
        }
        printf("Case #%d: %lld\n",t,numpairs);
    }
}