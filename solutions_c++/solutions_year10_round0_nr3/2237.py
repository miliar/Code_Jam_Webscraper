#include <cstdio>

using namespace std;

int money[1000], next[1000], g[1000], loop[1000], loopi[1000], loopj[1000];

int main ()
{
    freopen ("C-small-attempt1.in", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int T;
    scanf ("%d", &T);
    for (int t=1; t<=T; t++)
    {
        int R,K,N;
        scanf ("%d %d %d", &R, &K, &N);

        // make graph
        for (int i=0; i<N; i++)
        {
            money[i] = 0; next[i] = 0; loop[i] = 0;
            scanf ("%d", &g[i]);
        }
        for (int i=0; i<N; i++)
        {
            next[i]=i;
            while (money[i] + g[next[i]] <= K)
            {
                money[i] += g[next[i]];
                next[i]++;
                if (next[i] == N) next[i] = 0;
                if (next[i]==i) break;
            }
            //printf ("%d %d\n", money[i], next[i]);
        }

        // find loop
        int m=0, n=0, li=0;
        loopi[0] = 0;
        while (loop[next[m]] == 0)
        {
            loop[next[m]] = money[m] + loop[m];
            m = next[m];
            n++;
            loopi[m] = n;
            loopj[n] = m;
        }
        //printf ("asfd%d %d %d", n, loopi[next[m]], loopi[m]);
        int offset = R % (loopi[m] - loopi[next[m]] + 1);
        int money1 = loop[loopj[offset]];
        if (offset == 0) money1 = loop[m];
        int money2 = ((R - loopi[next[m]]) / (loopi[m] - loopi[next[m]] + 1)) * (loop[m] + money[m] - loop[next[m]]);

        //printf ("%d %d %d %d\n", next[m], m, loopi[next[m]], loopi[m]);
        //printf ("%d %d %d\n", loopj[loopi[next[m]]-1], (loopi[m] - loopi[next[m]] + 1), money1);
        //printf ("%d %d %d\n", money[0], loopj[R % (loopi[m] - loopi[next[m]] + 1)], money1);
        //printf ("%d %d %d\n", money[0], loopj[R % (loopi[m] - loopi[next[m]] + 1)], money2);
        //printf ("%d %d %d\n", m, loopj[R % (loopi[m] - loopi[next[m]] + 1)], money1);
        printf ("Case #%d: %d\n", t, money1 + money2);
    }

    return 0;
}
