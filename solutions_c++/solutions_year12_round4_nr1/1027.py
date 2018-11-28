#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
using namespace std;

int now,nowpos;
int t,aaaa;
int n,i,j;
int d[20000];
int D;
int l[20000];
int maxlo[20000];
int maxi,nummax;
bool bisa;
int main()
{
    scanf("%d",&t);
    for (aaaa=0;aaaa<t;++aaaa)
    {
        bisa=false;
        scanf("%d",&n);
        for (i=0;i<n;++i)
        {
            scanf("%d %d",&d[i],&l[i]);
            maxlo[i]=-1;
        }
        scanf("%d",&D);
        maxlo[0]=min(l[0],d[0]);
        for (i=0;i<n;++i)
        {
            if (D-d[i]<=maxlo[i])
            {
                bisa=true;
                break;
            }
            j=i+1;
            while (d[j]-d[i]<=maxlo[i])
            {
                if (j==n)
                    break;
                maxlo[j]=max(maxlo[j],min(d[j]-d[i],l[j]));
                ++j;
            }
        }
        printf("Case #%d: ",aaaa+1);
        if (bisa)
            printf("YES\n");
        else
            printf("NO\n");
    }
}
