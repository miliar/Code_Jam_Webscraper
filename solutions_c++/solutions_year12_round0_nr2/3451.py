#include <stdio.h>
#define MAXN 102

int main()
{
    int T, i;
    freopen ("q2_l.out", "w+", stdout);
    freopen ("q2_l.in", "r", stdin);
    scanf("%d\n", &T);
    for(i = 1; i <= T; i++)
    {
        int N, S, P, num, ans = 0;
        scanf("%d %d %d", &N, &S, &P);
        while(N--)
        {
            scanf("%d", &num);
            if(num%3 == 0)
            {
                if(num/3 >= P)
                {
                    ans++;
                    continue;
                }
                else if(num/3+1 >= P && S != 0 && num != 0)
                {
                    ans++;
                    S--;
                    continue;
                }
            }
            else if(num %3 == 1)
            {
                if(num/3+1 >= P)
                {
                    ans++;
                    continue;
                }
            }
            else
            {
                if(num/3+1 >= P)
                {
                   ans++;
                    continue;
                }
                else if(num/3+2 >= P && S != 0 && num >= 2)
                {
                    ans++;
                    S--;
                    continue;
                }
            }
        }
        printf("Case #%d: %d\n", i, ans);
    }
}
