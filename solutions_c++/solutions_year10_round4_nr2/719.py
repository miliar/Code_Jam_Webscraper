#include<stdio.h>

int two[20];
int M[3000];
int p;


int mmin(int a, int b)
{
    if(a < b)
        return a;
    else
        return b;
}

int main()
{
    int T, test, ans, i, j;
    int tmp;
    two[0] = 1;
    for(i = 1; i <= 10; i ++)
        two[i] = two[i - 1] * 2;
    scanf("%d", &T);
    for(test = 1; test <= T; test ++)
    {
        scanf("%d", &p);
        for(i = 0; i < two[p]; i ++)
            scanf("%d", M + i);
        for(i = p - 1; i >= 0; i --)
            for(j = 0; j < two[i]; j ++)
                scanf("%d", &tmp);
        ans = 0;
        for(i = p; i >= 1; i --)
        {
            for(j = 0; j < two[i]; j += 2)
            {
                if(M[j] > 0 && M[j + 1] > 0)
                {
                    M[j / 2] = mmin(M[j], M[j + 1]) - 1;
                }
                else
                {
                    ans ++;
                    M[j / 2] = mmin(M[j], M[j + 1]);
                }
            }
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}
