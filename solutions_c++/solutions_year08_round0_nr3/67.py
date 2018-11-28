#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <cmath>
#define sqr(x) ((x)*(x))
#define PI 3.14159265358979323846264338327950288L

using namespace std;

long double arcarea(long double x1, long double y1, long double x2, long double y2, long double r)
{
    long double b = sqrt(sqr(x1 - x2) + sqr(y1 - y2));
    long double a = b / 2;
    long double alpha = 2 * asin(a / r);
    return 0.5L * sqr(r) * (alpha - sin(alpha));
}

int main()
{
    int N;
    cin >> N;
    for(int cccccc=0;cccccc < N;++cccccc)
    {
        cout << "Case #" << cccccc+1 << ": ";

        // CODE
        long double f, R, t, r, g;
        cin >> f >> R >> t >> r >> g;
        long double inR = R - t - f;
        r += f;
        g -= 2*f;
        long double ans = 0L;
        if (g <= 0 || inR <= r)
        {
            ans = 1.0L;
        }
        else
        {
            long double area = 0L;
            long double x, y = r + g;
            while (y - g < inR)
            {
                // full rectangle
                int maxX = (inR >= y) ? (int)((sqrt(sqr(inR) - sqr(y)) + r) / (g + 2 * r)) : 0;
                area += sqr(g) * maxX;
                
                // partial
                x = (maxX + 1) * (g + r * 2) - r;
                while (sqr(x - g) + sqr(y - g) < sqr(inR))
                {
                    bool bx2 = (sqr(x) + sqr(y - g) < sqr(inR));
                    bool bx4 = (sqr(x - g) + sqr(y) < sqr(inR));
                    
                    if (bx2 && bx4)
                    {
                        long double y5 = sqrt(sqr(inR) - sqr(x));
                        long double x6 = sqrt(sqr(inR) - sqr(y));
                        long double delta = (x6 - (x - g)) * g + (x - x6) * (y5 - (y - g)) + 0.5L * (y - y5) * (x - x6) + arcarea(x6, y, x, y5, inR);
                        area += delta;
                    }
                    else if (bx2)
                    {
                        long double y5 = sqrt(sqr(inR) - sqr(x));
                        long double y6 = sqrt(sqr(inR) - sqr(x - g));
                        long double delta = (y5 - (y - g)) * g + (y6 - y5) * g * 0.5L + arcarea(x - g, y6, x, y5, inR);
                        area += delta;
                    }
                    else if (bx4)
                    {
                        long double x5 = sqrt(sqr(inR) - sqr(y - g));
                        long double x6 = sqrt(sqr(inR) - sqr(y));
                        long double delta = (x6 - (x - g)) * g + (x5 - x6) * g * 0.5L + arcarea(x5, y - g, x6, y, inR);
                        area += delta;
                    }
                    else
                    {
                        long double x5 = sqrt(sqr(inR) - sqr(y - g));
                        long double y6 = sqrt(sqr(inR) - sqr(x - g));
                        long double delta = (x5 - (x - g)) * (y6 - (y - g)) * 0.5L + arcarea(x5, y - g, x - g, y6, inR);
                        area += delta;
                    }
                    // next loop
                    x += g + 2 * r;
                }
                // next loop
                y += g + 2 * r;
            }

            ans = 1 - (area * 4) / (PI * sqr(R));
        }
        
        if (ans > 1) cout << "ERROR! ";
        if (ans < 0) cout << "ERROR! ";
        
        cout << fixed << setprecision(6) << ans << endl;
        // END OF CODE
    }
    return 0;
}