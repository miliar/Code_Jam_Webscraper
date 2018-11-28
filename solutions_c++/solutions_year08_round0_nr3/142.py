#include <cstdio>
#include <cmath>

const double Eps = 1e-8;
const double Pi = 3.1415926535897932384;

double f, r, t, l, g;

int Incircle(double X, double Y)
{
    return (X * X + Y * Y + Eps <= (r - t) * (r - t));
}

void Cross(double X1, double Y1, double X2, double Y2, double &X, double &Y)
{
    if (fabs(X1 - X2) <= Eps)
    {
        X = X1;
        Y = sqrt((r - t) * (r - t) - X * X);
    }
    else
    {
        Y = Y1;
        X = sqrt((r - t) * (r - t) - Y * Y);
    }
}

double Area(double X1, double Y1, double X2, double Y2, double X3, double Y3)
{
    return fabs(X1 * Y2 - X2 * Y1 + X2 * Y3 - X3 * Y2 + X3 * Y1 - X1 * Y3) / 2.0;
}

double Side(double X1, double Y1, double X2, double Y2)
{
    double Arc = abs(atan2(X1, Y1) - atan2(X2, Y2));
    return Arc * (r - t) * (r - t) / 2.0 - Area(0, 0, X1, Y1, X2, Y2);
}

double Count(double X1, double Y1, double X2, double Y2)
{
    double p1, q1, p2, q2;
    int A, B;
    if (Incircle(X2, Y2))
        return fabs(X1 - X2) * fabs(Y1 - Y2);
    A = 1 - Incircle(X1, Y2);
    if (A)
        Cross(X1, Y1, X1, Y2, p1, q1);
    else
        Cross(X1, Y2, X2, Y2, p1, q1);

    B = 1 - Incircle(X2, Y1);
    if (B)
        Cross(X1, Y1, X2, Y1, p2, q2);
    else
        Cross(X2, Y1, X2, Y2, p2, q2);

    if (A && B)
        return Area(X1, Y1, p1, q1, p2, q2) + Side(p1, q1, p2, q2);
    else if (A)
        return Area(X1, Y1, p1, q1, X2, Y1) + Area(p1, q1, X2, Y1, p2, q2) + Side(p1, q1, p2, q2);
    else if (B)
        return Area(X1, Y1, X1, Y2, p1, q1) + Area(X1, Y1, p1, q1, p2, q2) + Side(p1, q1, p2, q2);
    else
        return Area(X1, Y1, X1, Y2, p1, q1) + Area(p1, q1, p2, q2, X1, Y1) + Area(p2, q2, X2, Y1, X1, Y1) + Side(p1, q1, p2, q2);
}

double Work()
{
    double X = l, Y = l, Ret = 0;
    while (Incircle(X, Y))
    {
        while (Incircle(X, Y))
        {
            Ret += Count(X, Y, X + g, Y + g);
            Y += g + 2 * l;
        }
        X += g + 2 * l;
        Y = l;
    }
    return Ret * 4;
}


int main()
{
    int Cases;
    scanf("%d", &Cases);
    for (int Case = 1; Case <= Cases; Case ++)
    {
        scanf("%lf%lf%lf%lf%lf", &f, &r, &t, &l, &g);
        r += f;
        t += 2 * f;
        l += f;
        g -= 2 * f;
        
        printf("Case #%d: ", Case);
        if (g <= Eps || t >= r + Eps)
            printf("%.6lf\n", 1.0);
        else
            printf("%.6lf\n", 1.0 - Work() / (Pi * (r - f) * (r - f)));
    }
    return 0;
}
