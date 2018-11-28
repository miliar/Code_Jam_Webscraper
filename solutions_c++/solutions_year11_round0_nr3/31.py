#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        int count;
        scanf("%d", &count);
        int i;
        int sum = 0;
        int xorsum = 0;
        int minv = 1000000000;
        for (i = 0; i < count; i++)
        {
            int p;
            scanf("%d", &p);
            sum += p;
            xorsum ^= p;
            if (minv > p)
                minv = p;
        }
        if (xorsum == 0)
        {
            printf("Case #%d: %d\n", t+1, sum - minv);
        }
        else
        {
            printf("Case #%d: NO\n", t+1);
        }
    }
    return 0;
}
