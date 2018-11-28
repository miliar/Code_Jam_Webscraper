#include <stdio.h>

struct snapper
{
       bool state, has_power;
};

int main(void)
{
    int T, N, K;
    int t, n, k;
    struct snapper S[31];
    
    scanf("%d", &T);
    for(t = 1;t <= T;t++)
    {
        scanf("%d%d", &N, &K);
        
        for(n = 0;n < N+1;n++)
        {
            S[n].state = false;
            S[n].has_power = false;
        }
        S[0].has_power = true;
        
        for(k = 0;k < K;k++)
        {
            for(n = 0;n < N;n++)
                if(S[n].has_power)
                    S[n].state = !S[n].state;
            for(n = 0;n < N;n++)
                if(S[n].has_power && S[n].state == true)
                    S[n+1].has_power = true;
                else
                    S[n+1].has_power = false;

        }
        
        printf("Case #%d: ", t);
        if(S[N].has_power)
            printf("ON\n");
        else
            printf("OFF\n");
    }
    
    return(0);
}
