
#include <stdio.h>
#include <string.h>
#include <map>
#include <list>
#include <set>
#include <string>
#include <vector>
#include <math.h>

void GCJ_2009Round1C_B(const char*input, const char*output)
{
    FILE* fin = freopen(input, "rb", stdin);
    FILE* fout = freopen(output, "wb", stdout);

    int T, ncase = 0;
    scanf("%d", &T);
    while (ncase ++ < T)
    {
        int N;       
        scanf("%d", &N);

        double x0 = 0, vx = 0, y0 = 0, vy = 0, z0 = 0, vz = 0;
        for (int i = 0; i < N; i ++)
        {
            int a[6];
            scanf("%d%d%d%d%d%d", &a[0], &a[1], &a[2], &a[3], &a[4], &a[5], &a[6]);
            x0 += a[0];
            y0 += a[1];
            z0 += a[2];
            vx += a[3];
            vy += a[4];
            vz += a[5];
        }
        
        double A = 0,B = 0,C = 0;
        A = vx*vx + vy*vy + vz*vz;
        B = 2*x0*vx + 2*y0*vy + 2*z0*vz;
        C = x0*x0 + y0*y0 + z0*z0;

        double tmin, dmin;
        if (A == 0.0)
        {
            tmin = 0.0;
            dmin = sqrtf(C)/N;
        }
        else
        {
            tmin = (-0.5)*B/A;
            dmin = sqrtf((double)((-0.25*B*B)/A + C))/N;
            if (tmin < 0.0)
            {
                tmin = 0.0;
                dmin = dmin = sqrtf(C)/N;
            }
        }
        printf("Case #%d: %.8lf %.8lf\n", ncase, dmin, tmin);
    }

    fclose(fin);
    fclose(fout);
}
int main(int argc, char** argv)
{
    char*in_file = "gcj.in";
    char*out_file = "gcj.out";

    GCJ_2009Round1C_B(in_file, out_file);


    return 0;
}