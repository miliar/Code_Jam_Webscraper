#include <stdio.h>

inline int abs(int x){return x<0 ? -x : x;}

const int INF = 1000000;

struct Tree
{
    int g, c;
    int zero, one;
} tree[10000];

int main()
{
    FILE *in = fopen("input.txt", "r");
    FILE *out=fopen("output.txt", "w");
    int T, test;
    fscanf(in, "%ld", &T);
    for (test = 1;test<=T;test++)
    {
        int M, V, i, x;
        fscanf(in, "%ld %ld", &M, &V);
        for (i=0;i<(M-1)/2;i++)
        {
            fscanf(in, "%ld %ld", &tree[i].g, &tree[i].c);
            tree[i].zero = INF;
            tree[i].one = INF;
        }
        for (i=0;i<(M+1)/2;i++)
        {
            fscanf(in, "%ld", &tree[(M-1)/2 + i].g);
            if (tree[(M-1)/2 + i].g)
            {
                tree[(M-1)/2 + i].one = 0;
                tree[(M-1)/2 + i].zero = INF;
            }
            else
            {
                tree[(M-1)/2 + i].one = INF;
                tree[(M-1)/2 + i].zero = 0;
            }
        }
        for (i=(M-1)/2 - 1;i>=0;i--)
        {
            int l, r;
            l = (i+1)*2 - 1;
            r = l + 1;

            int zz, zo, oz, oo, min;
                zz = tree[l].zero + tree[r].zero;
                zo = tree[l].zero + tree[r].one;
                oz = tree[l].one + tree[r].zero;
                oo = tree[l].one + tree[r].one;

            if (tree[i].g == 0 || tree[i].c==1) // or
            {

                tree[i].zero = zz; //zero;
                if (tree[i].g!=0) tree[i].zero++;

                min = INF;
                if (zo<min) min = zo;
                if (oz<min) min = oz;
                if (oo<min) min = oo;

                if (tree[i].g!=0) min++;
                tree[i].one = min; // one

            }
            if (tree[i].g == 1 || tree[i].c==1) // and
            {
                min = INF;
                if (zz<min) min = zz;
                if (zo<min) min = zo;
                if (oz<min) min = oz;
                if (min<tree[i].zero)
                {
                    if (tree[i].g!=1) min++;
                    tree[i].zero = min; // zero;
                }

                if (oo<tree[i].one)
                {
                    tree[i].one = oo; // one
                    if (tree[i].g!=1) tree[i].one++;
                }
            }
            //printf("%ld %ld\n", tree[i].zero, tree[i].one); //delete

        }
        if (V==1) x = tree[0].one;
        else x = tree[0].zero;

        fprintf(out, "Case #%ld: ", test);
        if (x<INF) fprintf(out, "%ld\n", x);
        else fprintf(out, "IMPOSSIBLE\n");

    }

    fclose(in);
    fclose(out);
    return 0;
}
