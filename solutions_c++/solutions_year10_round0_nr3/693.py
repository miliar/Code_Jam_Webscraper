#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdio.h>
#include <string.h>
using namespace std;


int g[1000+2];
int rem[1000+2];
long long eur[1000000+2];

int main()
{
    int T,R,k,N;
    scanf("%d",&T);
    for (int t = 0;t < T;t++)
    {
        bool continue_t = false;
        scanf("%d %d %d",&R,&k,&N);
        memset(g,0,sizeof(g));
        for (int n = 0;n < N;n++)
            scanf("%d",&g[n]);
        memset(rem,0,sizeof(rem));
        memset(eur,0,sizeof(eur));

        int i = 0;
        for (int r = 1;r <= R;r++)
        {
            bool break_r = false;
            long long accum = 0;
            int oldi = i; 
            while (accum+g[i%N] <= k)
            {
                accum += g[i%N];
                i++;
                if (i%N == 0)
                {
                    if (i-oldi == N)
                    {
                        printf("Case #%d: %lld\n",t+1,R*accum);
                        break_r = true;
                        continue_t = true;
                        break;
                    }
                    else if (rem[i-oldi] == 0)
                        rem[i-oldi] = r;
                    else
                    {
                        int oldr = rem[i-oldi];
                        long long eurRep = (R-oldr)/(r-oldr)*(eur[r-1]-eur[oldr-1]);
                        long long eurBE = eur[(R-oldr)%(r-oldr)+oldr];
                        printf("Case #%d: %lld\n",t+1,eurRep+eurBE);
                        break_r = true;
                        continue_t = true;
                        break;
                    }
                }
            }
            if (break_r)
                break;
            eur[r] = eur[r-1]+accum;
        }
        if (continue_t)
            continue;
        printf("Case #%d: %lld\n",t+1,eur[R]);
    }
    return 0;
}
