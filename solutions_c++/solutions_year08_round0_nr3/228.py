#define _USE_MATH_DEFINES

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double IntegrateCircle(double x1, double x2, double r)
{
    double r2 = r * r;
    return (x2 / 2 * sqrt(r2 - x2 * x2) + r2 / 2 * asin(x2 / r))
        - (x1 / 2 * sqrt(r2 - x1 * x1) + r2 / 2 * asin(x1 / r));
}

int main()
{
    FILE* fin = stdin;
    FILE* fout = stdout;
    fopen_s(&fin, "C-large.in", "rt");
    fopen_s(&fout, "output.out", "wt");
    int n;
    fscanf_s(fin, "%d", &n);
    for (int count = 1; count <= n; count++)
    {
        double f, R, t, r, g;
        fscanf_s(fin, "%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
        double result;
        if (2 * f >= g)
            result = 1;
        else
        {
            double fullArea = M_PI * R * R;

            R -= t + f;
            r += f;
            g -= 2 * f;

            double R2 = R * R;
            double missArea = 0;
            double blockWidth = g + 2 * r;
            for (double x = r; x < R; x += blockWidth)
            {
                double h1 = sqrt(R2 - x * x);
                double h2 = x + g < R ? sqrt(R2 - (x + g) * (x + g)) : 0;
                int numBlock = (int)(h2 / blockWidth) + (fmod(h2, blockWidth) >= g + r ? 1 : 0);
                missArea += numBlock * g * g;
                for (double y = numBlock * blockWidth + r; y < h1; y += blockWidth)
                {
                    if (y < h2)
                        missArea += IntegrateCircle(x, x + g, R) - g * y;
                    else
                    {
                        double tempX = sqrt(R2 - y * y);
                        missArea += IntegrateCircle(x, tempX, R) - (tempX - x) * y;
                    }
                    if (y + g < h1)
                    {
                        double tempX = sqrt(R2 - (y + g) * (y + g));
                        missArea -= IntegrateCircle(x, tempX, R) - (tempX - x) * (y + g);
                    }
                }
            }
            missArea *= 4;
            result = 1 - missArea / fullArea;
        }
        fprintf_s(fout, "Case #%d: %lf\n", count, result);
    }
    fclose(fin);
    fclose(fout);
	return 0;
}

