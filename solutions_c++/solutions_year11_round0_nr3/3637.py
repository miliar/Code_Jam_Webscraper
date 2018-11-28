#include <stdio.h>

int main()
{
    freopen("/Users/Payut/Documents/Programming/Exercise/Code/Candy Splitting/Candy Splitting/C-large.in","r",stdin);
    freopen("/Users/Payut/Documents/Programming/Exercise/Code/Candy Splitting/Candy Splitting/c-large-out.txt","w",stdout);
    int T, N, k, bit = 0, y,min;
    scanf("%d", &T);
    for(int t = 0 ; t<T; t++)
    {
        y = 0;
        bit = 0;
        scanf("%d", &k);
        for(int i = 1; i<=k; i++)
        {
            scanf("%d", &N);
            bit = bit ^ N;
            y+=N;
            if (i ==1)
            {
                min = N;
            }
            else
            {
                if (min >N)
                    min=N;
            }
        }
    
    
    if (bit !=0)
    {printf("Case #%d: NO\n", t+1);
        continue;}
    else
    {
        printf("Case #%d: %d\n", t+1, y-min);
    }

    }
    return 0;
}