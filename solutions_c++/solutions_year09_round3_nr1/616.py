#include <stdio.h>
#include <string.h>

int N, test, n, i, v[100], xd;
long long num, put;
char x[100];

int main()
{
    freopen("date.in", "rt", stdin);
    freopen("date.out", "wt", stdout);

    scanf("%d", &N);
    
    for (test = 1; test <= N; test++)
    {
        scanf("%s", x);
        n = strlen(x);
        
        memset(v, 0, sizeof(v));
    
        xd = 1;
        for (i = 0; i < n; i++)
        {
            if (x[i] >= '0' && x[i] <= '9')
               if (!v[x[i] - '0'])
                  v[x[i] - '0'] = xd++;
            if (x[i] >= 'a' && x[i] <= 'z')
               if (!v[x[i] - 'a' +11])
                  v[x[i] - 'a' +11] = xd++;
        }
        for (i = 0; i <= 36; i++)
        {
         //   printf("%d %d\n", i, v[i]);
            if (v[i] >= 2)
               if (v[i] == 2)
                  v[i] = 0;
               else
                   v[i]--;
                   }
        if (xd > 2)           
           xd--; 
        num = 0;
        put = 1;
        for (i = n-1; i >= 0; i--, put*=xd)
        {
            //printf("%ld", num);
            if (x[i] >= '0' && x[i] <= '9')
               num += v[x[i] - '0'] * put;
            if (x[i] >= 'a' && x[i] <= 'z')
               num += v[x[i] - 'a' +11] * put;
        }
        printf("Case #%d: %lli\n", test, num);   
    }
    return 0;
}
