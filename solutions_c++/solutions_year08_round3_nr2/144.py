#include <stdio.h>
#include <string.h>

#define MAX_N 32

char str[MAX_N], st[MAX_N];

int back(int s, int n)
{
    int sols = 0, i;
    
    if (s == n)
    {
       long long sum = 0, num = str[0], i = 0;
       for (; i < n && st[i] == 0; )
           num = num * 10 + str[++i];
       for (sum = num; i < n; )
       {
           int sgn = st[i] == 1 ? 1 : -1;
           num = str[++i];
           if (i < n)
           {
              for (; st[i] == 0 && i < n; )
                  num = num * 10 + str[++i];
           }

           sum += sgn * num;
       }
       
       return (((sum % 2) == 0) || ((sum % 3) == 0) || ((sum % 5) == 0) || ((sum % 7) == 0)) ? 1 : 0;
    }
    
    for (i = 0; i < 3; i++)
    {
        st[s] = i;
        sols += back(s + 1, n);
    }
    
    return sols;
}

int main(void)
{
    int T, tests;
    
    freopen("b2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &tests);
    for (T = 1; T <= tests; T++)
    {
        int i, n;
        
        scanf("%s", str), n = strlen(str);
        for (i = 0; i < n; i++)
            str[i] -= '0';
            
        printf("Case #%d: %d\n", T, back(0, n - 1));
    }
    
    return 0;
}
