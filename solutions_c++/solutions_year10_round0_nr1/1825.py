#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    
    int T;
    int n,k;
    bool sign[35];
    scanf("%d", &T);
    for(int i=1; i<=T; i++)
    {
        scanf("%d%d", &n, &k);
/*
        for(int j=0; j<n; j++)
        {
            sign[j] = false;
        }
        for(int x=0; x<k; x++)
        {
            int y=0;
            while(sign[y] && y<n)
            {
                y++;
            }
            for(int z=0; z<n&& z<=y; z++)
            {
                sign[z] = !sign[z];
            }
        }
        int x;
        for(x=0; x<n; x++)
        {
            if(!sign[x])
            break;
        }
*/
        int sum = (int)(pow(2, n) + 0.0001);
        if(k % sum == sum - 1)
        {
           printf("Case #%d: ON\n", i);
        }
        else
        {
           printf("Case #%d: OFF\n", i);
        }
    }

    return 0;
}
