#include <stdio.h>

int main()
{
    FILE *in = fopen("input.txt", "r"),
        *out= fopen("output.txt", "w");
    int T, test;
    fscanf(in, "%ld", &T);

    for (test = 1;test<=T;test++)
    {
        int H, W, R, map[100][100], i, x, y, j;
        fscanf(in, "%ld %ld %ld", &H, &W, &R);
        for (i=0;i<100;i++)
            for (j=0;j<100;j++)
                map[i][j]=0;
        for (i=0;i<R;i++)
        {
            fscanf(in, "%ld %ld", &y, &x);
            x--;y--;
            map[y][x]=-1;
        }

        map[0][0]=1;

        const int a[2][2]={{-1,-2},{-2,-1}};
        int k, x1, y1, b;

        for (i=0;i<H;i++)
            for (j=0;j<W;j++)
                if (map[i][j]!=-1)
                {
                    for (k=0;k<2;k++)
                    {
                        x1 = j + a[k][0];
                        y1 = i + a[k][1];
                        if (x1>=0 && y1>=0 && map[y1][x1]!=-1)
                        {
                            map[i][j] = (map[i][j] + map[y1][x1])% 10007;
                        }


                    }

                }
        fprintf(out, "Case #%ld: %ld\n", test, map[H-1][W-1]);
    }


    fclose (in);
    fclose(out);
    return 0;
}
