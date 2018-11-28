#include <iostream>
#include <fstream>
#include <stdio.h>
#include <math.h>

#define PI 3.14159265
#define SQR(x) (x) * (x)

using namespace std;

double circCorrsp(double r, double x)
{
    return sqrt(r * r - x * x);
}

double circArea(double r, double y1, double y2)
{
    if (r<=0)
        return 0;

    if (y1 > r) y1 = r;
    if (y2 > r) y2 = r;
    if (y1 < 0) y1 = -y1;
    if (y2 < 0) y2 = -y2;

    double tmp;
    if (y1 > y2)
    {
        tmp = y1;
        y1 = y2;
        y2 = tmp;
    }

    double x1 = circCorrsp(r, y1);
    double x2 = circCorrsp(r, y2);
    double a = asin(y1 / r);
    double b = asin(y2 / r);
    return (r * r * (0.5f * (b - a) - 0.25f * (sin(2 * b) - sin(2 * a))) - (x1 - x2) * y1);
}

double dist(double x1, double y1, double x2, double y2)
{
    return sqrt(SQR(x2 - x1) + SQR(y2-y1));
}

double rectCirc(double x, double y, double w, double h, double r)
{
    if (w < 0) w = -w;
    if (h < 0) h = -h;

    if (x < 0)
    {
        w += x;
        x = 0;
    }
    if (y < 0)
    {
        h += y;
        y = 0;
    }

    if (x > r || y > r || w < 0 || h < 0 || dist(0, 0, x, y) >= r)
        return 0;

    if (dist(0, 0, x + w, y + h) <= r)
        return w * h;

    if (x + w > r)
        w = r - x;
    if (y + h > r)
        h = r - y;

    double bX = circCorrsp(r, y);
    double tX = circCorrsp(r, y + h);
    double lY = circCorrsp(r, x);
    double rY = circCorrsp(r, x + w);

    if (tX < x)
    {
        tX = x;
        h = lY - y;
    }
    if (rY < y)
    {
        rY = y;
        w = bX - x;
    }

    double a = w * h - (x + w - tX) * (y + h - rY);

    return a + circArea(r, rY, y + h);
/*
    if (circCorrsp(r, y + h) < x)
        h = circCorrsp(r, x) - y;

    if (circCorrsp(r, x + w) < y)
        w = circCorrsp(r, y) - x;

    double cx1 = x + w;
    double cy1 = circCorrsp(r, cx1);

    double cy2 = y + h;
    double cx2 = circCorrsp(r, cy2);

    if (cy1 > y + h)
        return w * h;

    double tmp = 0;
    if (cx1 > x + w)
    {
        cx1 = x + w;
        double cy1 = circCorrsp(r, cx1);
        tmp = (cx1 - cx2) * (cy1 - y);
    }

    w = cx2 - x;

    return w * h + tmp + circArea(r, cy1, cy2);
*/
}

int main()
{
    int n;
    double f, rr, t, r, g;
    double x, y, w, ir, a, stride;
    char buf[1000];
    ifstream fin;
    ofstream fout;

    fin.open("in.txt");
    if (fin.fail())
        exit(1);
    fout.open("out.txt");

    fin >> n;

    for (int tt = 1; tt <= n; ++tt)
    {
        fin >> f >> rr >> t >> r >> g;

        w = r + r + f + f;
        a = 0;
        ir = rr - t - f;
        stride = r + r + g;

        for (y = -(r+f); y < ir; y += stride)
        {
            a += rectCirc(0, y, ir, w, ir);
        }
        for (x = -(r+f); x < ir; x += stride)
        {
            for (y = -(r+f); y < ir; y += stride)
            {
                a -= rectCirc(x, y, w, w, ir);
            }
            a += rectCirc(x, 0, w, ir, ir);
        }
        fout << "Case #" << tt << ": ";
        sprintf(buf, "%0.6f\n", (4 * a + (rr * rr - ir * ir) * PI) / (rr * rr * PI));
        fout << buf;
        //cout << "Case #" << tt << ": " << a << endl;
    }

    return 0;
}
