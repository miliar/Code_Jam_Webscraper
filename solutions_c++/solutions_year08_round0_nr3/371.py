// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#define _USE_MATH_DEFINES
#include "math.h"

#define Input "sample.txt"
#define Output "Result.txt"

#define err 0.000001

double Dis(double x1, double y1, double x2, double y2)
{
    double x = x1 - x2;
    double y = y1 - y2;
    return sqrt(x * x + y * y);
}

double TriangleSize(double x1, double y1, double x2, double y2, double x3, double y3)
{
    double a = Dis(x1, y1, x2, y2);
    double b = Dis(x1, y1, x3, y3);
    double c = Dis(x3, y3, x2, y2);
    double t = (a + b + c) / 2;
    return sqrt((t - a) * (t - b) * (t - c) * t);
}

double SectorSize(double r, double d)
{
    return r * r * asin(d / 2 / r);
}

double CircleSize(double r)
{
    return r * r * M_PI;
}

double GetPosOnCirle(double r, double x)
{
    return sqrt(r * r - x * x);
}

int _tmain(int argc, _TCHAR* argv[])
{
    freopen(Input, "r", stdin);
    freopen(Output, "w", stdout);

    int n;
    double f, R, t, r, g, g1;
    double result, part;
    double x, y;
    double x1, y1, x2, y2;
    int i,j,k;

    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
        g1 = g - f * 2;
        t = R - t - f;
        if (g1 < -err || t < err) 
        {
            printf("Case #%d: %.6lf\n", i, 1);
        }

        result = 0;
        j = 0;
        while (1)
        {
            x = r + (g + r + r) * j + f;
            if (x > t) break;

            if (x + g1 < t) 
            {
                y = GetPosOnCirle(t, x + g1);
                k = (y + r) / (g + r + r);
                result += g1 * g1 * k;                
            }
            else k = 0;

            while (1)
            {
                y = r + (g + r + r) * k + f;
                if (Dis(x, y, 0, 0) > t) break;                

                // rectangle is full inside
                if (Dis(x+g1, y+g1, 0, 0) < t) result += g1*g1;
                else if (k >= j)
                {
                    part = 0;
                    // rectangle's right bottom is inside
                    if (Dis(x+g1, y, 0, 0) < t)
                    {
                        y1 = GetPosOnCirle(t, x + g1);
                        part += g1 * (y1 - y);

                        // rectangle's left top is inside
                        if (Dis(x, y+g1, 0, 0) < t)
                        {
                            x1 = GetPosOnCirle(t, y + g1);
                            part += (x1 - x) * (g1 - (y1 - y));
                            x2 = x + g1;
                            y2 = y + g1;
                        }
                        else 
                        {
                            x1 = x;
                            x2 = x + g1;
                            y2 = GetPosOnCirle(t, x1);
                        }
                    }
                    else 
                    {
                        x1 = x;
                        y1 = y;
                        x2 = GetPosOnCirle(t, y1);
                        y2 = GetPosOnCirle(t, x1);
                    }

                    part += (SectorSize(t, Dis(x1, y2, x2, y1)) 
                               - TriangleSize(0, 0, x1, y2, x2, y1)
                               + TriangleSize(x1, y1, x1, y2, x2, y1));
                    result += part * (j == k ? 1 : 2);
                }
                k++;
            }
            j++;
        }

        result = 1 - (result / (CircleSize(R) / 4));
        if (result < err && result > -err) printf("Case #%d: %.6lf\n", i, 0);
        else printf("Case #%d: %.6lf\n", i, result);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
