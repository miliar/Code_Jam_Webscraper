#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

static double f, r, R, t, g, RT;

// indefinite integral of sqrt(r^2 - x^2)
static inline double integ(double x, double r)
{
    if (x > r) x = r;
    double y = sqrt(r * r - x * x);
    return 0.5 * (x * y + r * r * atan2(x, y));
}

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        double ans = 1.0;
        double area = 0.0;
        cin >> f >> R >> t >> r >> g;
        r += f;
        g -= 2 * f;
        t += f;
        RT = R - t;
        if (g > 0.0 && RT > 0.0)
        {
            int wh = (int) ceil(RT / (2 * r + g)) + 2;

            for (int i = 0; i < wh; i++)
                for (int j = 0; j < wh; j++)
                {
                    double minx = r + (2 * r + g) * i;
                    double maxx = minx + g;
                    double miny = r + (2 * r + g) * j;
                    double maxy = miny + g;
                    if (minx * minx >= RT * RT - miny * miny)
                        continue;
                    if (maxx * maxx > RT * RT - maxy * maxy)
                    {
                        if (minx * minx <= RT * RT - maxy * maxy)
                        {
                            double minx2 = sqrt(RT * RT - maxy * maxy);
                            area += (minx2 - minx) * g;
                            minx = minx2;
                        }

                        if (maxx * maxx > RT * RT - miny * miny)
                            maxx = sqrt(RT * RT - miny * miny);

                        area += integ(maxx, RT) - integ(minx, RT);
                        area -= miny * (maxx - minx);
                    }
                    else
                        area += g * g;
                    // printf("i = %d j = %d area = %.9f\n", i, j, area);
                }
            ans = 1.0 - area / (M_PI * R * R / 4.0);
        }
        printf("Case #%d: %.9f\n", cas + 1, ans);
    }
    return 0;
}
