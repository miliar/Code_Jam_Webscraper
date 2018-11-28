#include <cstdio>
#include <cassert>

int main()
{
    FILE *f = fopen("in.txt", "r");
    FILE *out = fopen("out.txt", "w");
    assert(f && out);

    int data[100][100], earc[100];
    double wp[100], owp[100], oowp[100];

    int num;
    fscanf(f, "%d", &num);
    for (int i = 1; i <= num; i++)
    {
        fprintf(out, "Case #%d:\n", i);

        int com;
        fscanf(f, "%d", &com);
        fgetc(f);

        for (int j = 0; j < com; j++)
        {
            for (int k = 0; k < com; k++)
                data[j][k] = fgetc(f);

            fgetc(f);
        }

        for (int j = 0; j < com; j++)
        {
            int totwin = 0, total = 0;

            for (int k = 0; k < com; k++)
            {
                if (data[j][k] == '1')
                    totwin++;
                if (data[j][k] != '.')
                    total++;
            }
            wp[j] = double(totwin)/total;
        }

        for (int z = 0; z < com; z++)
        {
            double ar = 0;
            int arc = 0;

            for (int j = 0; j < com; j++)
            {
                int totwin = 0, total = 0;

                if (data[j][z] != '.')
                    arc++;
                else
                    continue;

                for (int k = 0; k < com; k++)
                {
                    if (k == z)
                        continue;

                    if (data[j][k] == '1')
                        totwin++;
                    if (data[j][k] != '.')
                        total++;
                }

                ar += double(totwin)/total;
            }

            owp[z] = ar/arc;
            earc[z] = arc;
        }


        for (int z = 0; z < com; z++)
        {
            double ar = 0;
            int arc = 0;

            for (int j = 0; j < com; j++)
            {
                if (data[j][z] != '.')
                {
                    arc++;
                    ar += owp[j];
                }
            }

            oowp[z] = ar/arc;
        }


        for (int j = 0; j < com; j++)
        {
            fprintf(out, "%.12lf\n", 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j]);
        }
    }

}
