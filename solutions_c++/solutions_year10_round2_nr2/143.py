#include<cstdio>

int x[100];
int v[100];
int can[100];

int main()
{
    int ti, teste;
    scanf("%d", &teste);
    for (ti=0;ti<teste;ti++)
    {
        int resp = 0;
        int n, k, b, t;
        scanf("%d %d %d %d", &n, &k, &b, &t);
        int i;
        for (i=0; i<n; i++)
        {
            scanf("%d", &x[i]);
        }
        for (i=0; i<n; i++)
        {
            scanf("%d", &v[i]);
        }
        for (i=0; i<n; i++)
        {
            if (((b - x[i] - 1) / v[i]) + 1 > t)
            {
                can[i] = 0;
            }
            else
            {
                can[i] = 1;
            }
        }
        int count = 0;
        for (i=n-1; i>=0; i--)
        {
            if (can[i] == 1)
            {
                count++;
                resp += (n - i) - count;
            }
            if (count == k)
                break;
        }
        if (i>=0)
        {
            printf("Case #%d: %d\n", ti+1, resp);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n", ti+1);
        }
    }
    return 0;
}
