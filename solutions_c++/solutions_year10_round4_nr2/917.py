#include <stdio.h>

int t;
int p;
int team[1024];
int price[10][512];
int result;

int main()
{
    scanf("%d", &t);
    for(int i = 1; i <= t; i++)
    {
        result = 0;
        scanf("%d", &p);
        for(int j = 0; j < 1<<p; j++)
        {
            scanf("%d", team+j);
        }
        int to = 1<<(p-1);
        for(int j = 0; j < p; j++)
        {
            for(int k = 0; k < to; k++)
            {
                scanf("%d", &price[j][k]);
            }
            to>>=1;
        }

        int nowS = 0;
        for(;;)
        {
            nowS--;
            int smallest = 100;
            int smallidx = -1;
            for(int j = 0; j < 1<<p; j++)
            {
                if(team[j] < smallest)
                {
                    smallest = team[j];
                    smallidx = j;
                }
            }
            if(smallidx == -1) break;
            team[smallidx] = 1000;

            int sl, sk, sv;
            for(int j = 0; j < p-smallest; j++)
            {
                sl = -1;
                sk = -1;
                sv = 200000;
                for(int k = smallidx/2, l = 0;l<p;k/=2, l++)
                {
                    if(price[l][k] <= sv && price[l][k] != nowS)
                    {
                        sv = price[l][k];
                        sl = l;
                        sk = k;
                    }
                }
                if(sl == -1) break;
                if(price[sl][sk] >= 0) result += price[sl][sk];
                price[sl][sk] = nowS;
            }
        }

        printf("Case #%d: %d\n", i, result);
    }

    return 0;
}
