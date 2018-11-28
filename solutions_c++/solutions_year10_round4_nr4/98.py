#include <iostream>
#include <math.h>

using namespace std;

double sqr(double x)
{
    return x*x;
}

struct circle
{
    double x, y, r;

    double operator * (const circle &other)
    {
        double d = sqrt(sqr(x - other.x) + sqr(y - other.y));

        double a = acos((d*d + r*r - sqr(other.r)) / 2 / d / r);

        return r * r * a - r * r * sin(2*a) / 2;
    }
} c[1<<13];

int main()
{
    int t;
    cin >> t;
    cout.setf(ios::fixed);
    cout.precision(10);
    for (int tt=1; tt<=t; tt++)
    {
        int n, m;
        cin >> n >> m;

        for (int i=0; i<n; i++)
            cin >> c[i].x >> c[i].y;

        cout << "Case #" << tt << ":";

        for (; m--;)
        {
            int x, y;
            cin >> x >> y;

            for (int i=0; i<n; i++)
                c[i].r = sqrt(sqr(c[i].x - x) + sqr(c[i].y - y));

            cout << " " << c[0] * c[1] + c[1] * c[0];
        }
        cout << endl;
    }
    return 0;
}
