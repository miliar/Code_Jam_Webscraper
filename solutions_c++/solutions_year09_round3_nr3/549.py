#include <stdio.h>
#include <string.h>

int N, P, Q, q[1000], st[1000], viz[1000], r[1010], sum, min;

void back(int k)
{
     int i, j;
     if (k > Q-1)
     {  
        memset(r, 0, sizeof(r));
        sum = 0;
        for (i = 0; i < Q; i++)
        {
            r[ q[ st[i] ] ] = 1;
            j = q[ st[i] ] -1;
            while (!r[j] && j >= 1)     
                  j--;
            sum += q[ st[i] ] - 1 - j; 
            
            j = q[ st[i] ] +1;
            while (!r[j] && j <= P)
                  j++;
            sum += j - q[ st[i] ]-1;        
        }
        if (sum < min)
               min = sum;
        return;
     } 
     for (i = 0; i < Q; i++)
         if (!viz[i])
         {
            
            st[k] = i;
            viz[i] = 1;
            back(k+1);
            viz[i] = 0;
         }
}

int main()
{
    int test, i;
    freopen("date.in", "rt", stdin);
    freopen("date.out", "wt", stdout);
    scanf("%d", &N);
    for (test = 1; test <= N; test++)
    {
        scanf("%d %d", &P, &Q);
        for (i = 0; i < Q; i++)
            scanf("%d", &q[i]);
        min = Q*P;
        memset(viz, 0, sizeof(viz));
        back(0);
        printf("Case #%d: %d\n", test, min);
    }
    return 0;
}
