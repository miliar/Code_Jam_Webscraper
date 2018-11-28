#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
    int t, n;
    int tot = 0, to = 0, tb = 0, po = 1, pb = 1;
    FILE *fin = fopen("A-large.in", "r");
    FILE *fout = fopen("A-large.out", "w");
    fscanf(fin, "%d", &t);
    for (int idx = 0; idx < t; idx++)
    {
        fscanf(fin, "%d", &n);
        tot = 0;
        to = 0;
        tb = 0;
        po = 1;
        pb = 1;
        char prev;
        for (int i = 0; i < n; i++)
        {
            char c = 0;
            int k = 0;
            fscanf(fin, " %c %d", &c, &k);
            if (i == 0) prev = c;
            if (c == 'O')
            {
                if (c == prev)
                {
                    to += (abs(k-po)+1);
                    tot += (abs(k-po)+1);
                    po = k;
                }
                else
                {
                    prev = c;
                    int cost = abs(k-po);
                    if (cost <= tb) cost = 0;
                    else cost -= tb;
                    tot += cost+1;
                    to = cost+1;
                    po = k;
                }
            }
            else if (c == 'B')
            {
                if (c == prev)
                {
                    tb += (abs(k-pb)+1);
                    tot += (abs(k-pb)+1);
                    pb = k;
                }
                else
                {
                    prev = c;
                    int cost = abs(k-pb);
                    if (cost <= to) cost = 0;
                    else cost -= to;
                    tot += cost+1;
                    tb = cost+1;
                    pb = k;
                }
            }
            //printf("%c %d %d %d %d %d\n", prev, tot, to, tb, po, pb);
        }
        fprintf (fout, "Case #%d: %d\n", idx+1, tot);
    }
    return 0;
}
