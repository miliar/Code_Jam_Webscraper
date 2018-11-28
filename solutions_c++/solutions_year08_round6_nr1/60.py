
#include <stdio.h>


#include <stdio.h>



#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#define MAX 1000010
char buf[100], buf2[100];
int w[1100], h[1100], b[1100];

bool within(int a, int min, int max)
{
    return a >= min && a <= max;
}

int main()
{
        freopen("A2.in", "r", stdin);
//        freopen("small.op", "w", stdout);

    //  freopen ("C2.in","r",stdin);
      freopen ("large.op","w",stdout);
    int t, cs = 0;
    scanf("%d", &t);
    while (t--)
    {
        int n;
        scanf("%d", &n);
        gets(buf);
        for (int i = 0; i < n; i++)
        {
            gets(buf);
            sscanf(buf, "%d%d%s", &w[i], &h[i], buf2);
            if (strcmp(buf2, "BIRD") == 0)
                b[i] = true;
            else
                b[i] = false;
        }
        int hmin = MAX, hmax = 0, wmin = MAX, wmax = 0;
        for (int i = 0; i < n; i++)
        {
            if (!b[i])
                continue;
            if (w[i] > wmax)
                wmax = w[i];
            if (w[i] < wmin)
                wmin = w[i];

            if (h[i] > hmax)
                hmax = h[i];
            if (h[i] < hmin)
                hmin = h[i];
        }
        int hl = 0, hh = MAX, wl = 0, wh = MAX;
        for (int i = 0; i < n; i++)
        {
            if (b[i])
                continue;
            if (within(h[i], hmin, hmax))
            {
                if (w[i] > wl && w[i] < wmin)
                    wl = w[i];
                if (w[i] < wh && w[i] > wmax)
                    wh = w[i];


            }
            if (within(w[i], wmin, wmax))
            {
                if (h[i] > hl && h[i] < hmin)
                    hl = h[i];
                if (h[i] < hh && h[i] > hmax)
                    hh = h[i];
            }
        }
        int m;
        scanf("%d", &m);
        printf("Case #%d:\n", ++cs);
        for (int i = 0; i < m; i++)
        {
            bool done = false;
            int cw, ch;
            scanf("%d%d", &cw, &ch);
            for (int j = 0; j < n; j++)
            {
                if (cw == w[j] && ch == h[j])
                {
                    done = true;
                    if (b[i])
                    {
                        printf("BIRD\n");

                    }
                    else
                    {
                        printf("NOT BIRD\n");
                    }
                }
            }
            if (done)
                continue;
            if (within(cw, wmin, wmax) && within(ch, hmin, hmax))
            {
                printf("BIRD\n");
            }
                //            else if (ch <= hl || ch >= hh || cw <= wl || cw >= wh)
                //            {
                //                printf("NOT BIRD\n");
                //            }
            else
            {
                bool pos = true;
                int nwmin = wmin;
                int nwmax = wmax;
                int nhmin = hmin;
                int nhmax = hmax;
                if (cw < nwmin)
                    nwmin = cw;
                if (cw > nwmax)
                    nwmax = cw;
                if (ch < nhmin)
                    nhmin = ch;
                if (ch > nhmax)
                    nhmax = ch;
                for (int i = 0; i < n; i++)
                {
                    if (b[i])
                        continue;
                    if (within(w[i], nwmin, nwmax) && within(h[i], nhmin, nhmax))
                    {
                        pos = false;
                        break;
                    }
                }
                if (!pos)
                {
                    printf("NOT BIRD\n");
                }
                else
                    printf("UNKNOWN\n");
            }
        }



    }
    return 0;
}

