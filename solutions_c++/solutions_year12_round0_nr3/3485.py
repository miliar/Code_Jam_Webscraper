#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 10
#define MAX 2000000
int shiftnum(char *num, int len)
{
    char tmp[MAXN];
    int numlen = strlen(num), i , j;

    for(i = numlen-len, j = 0; i < numlen; i++, j++)
        tmp[j] = num[i];
    for(i = 0; i < numlen-len; i++, j++)
        tmp[j] = num[i];
    tmp[j]='\0';
    //printf("%s %s\n", num, tmp);
    return atoi(tmp);
}
int num[MAX];
int s_num[MAX];
int main()
{

    int T, i;
    freopen ("q3-s.out", "w+", stdout);
    freopen ("q3-s.in", "r", stdin);
    scanf("%d\n", &T);
    for(i = 1; i <= T; i++)
    {
        char A[MAXN], B[MAXN], tmp[MAXN];
        int ans = 0, n, m, tmpb, j, deg;
        scanf("%s %s", A, B);
        n = atoi (A);
        tmpb = atoi (B);
        memset(num, 0, MAX);
        for(deg = 1, j = 1; j < strlen(A); j++)
            deg *= 10;

        for(;n < tmpb; n++)
        {
            if(num[n] == 1)
                continue;
            num[n] = 1;
            memset(s_num, 0, MAX);
            sprintf (tmp, "%d", n);

            for(j = 1; j < strlen(A); j++)
            {
                m = shiftnum(tmp, j);
                if(m <= tmpb && n < m && s_num[m] == 0)
                {
                    //printf("%d %d\n", n, m);
                    s_num[m] = 1;
                    ans++;
                }

            }
        }
        printf("Case #%d: %d\n", i, ans);
    }
}
