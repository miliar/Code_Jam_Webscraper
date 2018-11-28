#include <iostream>
#include <set>
#include <map>
#include <stdio.h>
using namespace std;
int T,n;
int a[500];
map<int,int> MAP;
int main()
{
    scanf("%d", &T);
    for(int ti=0;ti<T;ti ++)
    {
        scanf("%d", &n);
        for(int i=0;i<n;i++)
            scanf("%d", &a[i]);
        int found = 0;
        MAP.clear();
        printf("Case #%d:\n", ti+1);
        for(int i=0;i<(1<<19);i++)
        {
            int s = 0;
            for(int b=0;b<20;b++)
                if (i & ((int)1<<b)) s+=a[b];
            if (MAP.find(s)!=MAP.end())
            {
                int i1 = MAP[s];
                int u = i1 & i;
                i1 = i1 & (~u);
                int i2 = i & (~u);
                for(int j=0;j<20;j++)
                    if (i1 & (1<<j)) printf("%d ", a[j]);
                printf("\n");
                for(int j=0;j<20;j++)
                    if (i2 & (1<<j)) printf("%d ", a[j]);
                printf("\n");
                found = 1;
                break;
            }
            MAP[s] = i;
        }
        if (!found) printf("Impossible\n");
    }
    
}
