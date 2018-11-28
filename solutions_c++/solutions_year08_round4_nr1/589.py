#include <stdio.h>
#include <string.h>

#define MAX_N 10001
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int M, V, C[MAX_N], R[MAX_N], S[MAX_N][2];

void AND(int p, int *t, int *f)
{
     int left = p << 1, right = (p << 1) + 1;
     
     if (S[left][1] >= 0 && S[right][1] >= 0)
        *t = S[left][1] + S[right][1];
     else *t = -1;
     
     *f = -1;
     if (S[left][0] >= 0 && S[right][0] >= 0)
        *f = S[left][0] + S[right][0];
     if (S[left][0] >= 0 && S[right][1] >= 0)
        if (*f >= 0)
           *f = MIN(*f, S[left][0] + S[right][1]);
        else *f = S[left][0] + S[right][1];
     if (S[left][1] >= 0 && S[right][0] >= 0)
        if (*f >= 0)
           *f = MIN(*f, S[left][1] + S[right][0]);
        else *f = S[left][1] + S[right][0];
}

void OR(int p, int *t, int *f)
{
     int left = p << 1, right = (p << 1) + 1;
     
     if (S[left][0] >= 0 && S[right][0] >= 0)
        *f = S[left][0] + S[right][0];
     else *f = -1;
     
     *t = -1;
     if (S[left][0] >= 0 && S[right][1] >= 0)
        *t = S[left][0] + S[right][1];
     if (S[left][1] >= 0 && S[right][0] >= 0)
        if (*t >= 0)
           *t = MIN(*t, S[left][1] + S[right][0]);
        else *t = S[left][1] + S[right][0];
     if (S[left][1] >= 0 && S[right][1] >= 0)
        if (*t >= 0)
           *t = MIN(*t, S[left][1] + S[right][1]);
        else *t = S[left][1] + S[right][1];
}

int main(void)
{
    int tests, test;
    
    freopen("a-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
    {
        int h, i;
        
        memset(C, 0, sizeof(C));
        memset(R, 0, sizeof(R));
        memset(S, 0, sizeof(S));
        
        scanf("%d%d", &M, &V);
        h = (M - 1) / 2;
        for (i = 1; i <= h; i++)
        {
            int g, c;
            scanf("%d%d", &g, &c);
            R[i] = 3 - g;
            C[i] = c;
        }
        
        for (; i <= M; i++)
            scanf("%d", R + i);
            
        for (i = M; i > h; i--)
            if (R[i])
               S[i][1] = 0, S[i][0] = -1;
            else S[i][0] = 0, S[i][1] = -1;
            
        for (; i; i--)
        {
            int min0, min1, min_0, min_1, m0, m1;
            
            if (R[i] == 2)
               AND(i, &min1, &min0);
            else OR(i, &min1, &min0);
            
            if (C[i])
               if (R[i] == 2)
               {
                  OR(i, &min_1, &min_0);
                  if (min_0 >= 0)
                     min_0++;
                  if (min_1 >= 0)
                     min_1++;
               }
               else 
               {
                    AND(i, &min_1, &min_0);
                    if (min_0 >= 0)
                       min_0++;
                    if (min_1 >= 0)
                       min_1++;
               }
            else
            {
                S[i][0] = min0;
                S[i][1] = min1;
                continue;
            }
               
            if (min0 >= 0 && min_0 >= 0)
               m0 = MIN(min0, min_0);
            else
            if (min0 >= 0)
               m0 = min0;
            else m0 = min_0;
            
            if (min1 >= 0 && min_1>= 0)
               m1 = MIN(min1, min_1);
            else
            if (min1 >= 0)
               m1 = min1;
            else m1 = min_1;
            
            S[i][0] = m0;
            S[i][1] = m1;
        }
        
        if (S[1][V] >= 0)
           printf("Case #%d: %d\n", test, S[1][V]);
        else printf("Case #%d: IMPOSSIBLE\n", test);
    }
    
    return 0;
}
