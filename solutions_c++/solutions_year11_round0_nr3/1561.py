#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>

using namespace std;

int i,ti,tn,n,sum,sumXor,minV,a[1002];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tn);
    for (ti = 1; ti <= tn; ti++)
    {
        scanf("%d",&n);
        sum = 0; sumXor = 0; minV = 10000001;
        for (i = 1; i <= n; i++)
        {
            scanf("%d",&a[i]);
            sum += a[i];
            sumXor = sumXor ^ a[i];
            if (a[i] < minV) minV = a[i];
        }
        if (sumXor != 0) printf("Case #%d: NO\n",ti);
        else printf("Case #%d: %d\n",ti,sum-minV);
    }
}
