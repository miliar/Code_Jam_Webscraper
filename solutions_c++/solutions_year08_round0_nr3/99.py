
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

double sqr(double x) { return x * x; }

double SegArea(double x0, double y0, double x1, double y1, double R)
{
  double a0 = atan2(y0, x0);
  double a1 = atan2(y1, x1);
  double pieA = 0.5 * (a1 - a0) * sqr(R);
  double dist = sqrt(sqr(x0 - x1) + sqr(y0 - y1));
  double h = sqrt(R*R - sqr(0.5 * dist));
  double A = pieA - h * (0.5 * dist);
  return A;
}

int main()
{
  int N;
  cin >> N;
  for (int n = 1; n <= N; ++n)
  {
    double f, R, t, r, g;
    cin >> f >> R >> t >> r >> g;

    double P;
    if ((f >= (R - t)) || (g <= (2.0 * f)))
      P = 1.0;
    else
    {
      double totalA = M_PI * sqr(R) / 4.0;
      double A = 0.0;
      int K = int(ceil((R - t - (r + f)) / (2.0 * r + g)));
      for (int x = 0; x < K; ++x)
      {
        for (int y = K - 1; y >= 0; --y)
        {
          double xo = x * (2.0 * r + g) + r + g - f;
          double yo = y * (2.0 * r + g) + r + g - f;
          double xi = xo + f - g + f;
          double yi = yo + f - g + f;
          if ((xo*xo + yo*yo) <= sqr(R - t - f))
          {
            A += sqr(g - 2.0 * f) * (y + 1);
            break;
          }
          else if ((xi*xi + yi*yi) >= sqr(R - t - f))
            A += 0.0;
          else
          {
            bool xc = ((xo*xo + yi*yi) <= sqr(R - t - f));
            bool yc = ((xi*xi + yo*yo) <= sqr(R - t - f));
            if (xc && yc)
            {
              double xop = sqrt(sqr(R - t - f) - xo*xo);
              double yop = sqrt(sqr(R - t - f) - yo*yo);
              A += SegArea(xo, xop, yop, yo, R - t - f);
              A += (xop - yi) * (g - 2.0 * f);
              A += (yop - xi) * (g - 2.0 * f);
              A -= (xop - yi) * (yop - xi);
              A += 0.5 * (xo - yop) * (yo - xop);
            }
            else if (xc)
            {
              double xop = sqrt(sqr(R - t - f) - xo*xo);
              double xip = sqrt(sqr(R - t - f) - xi*xi);
              A += SegArea(xo, xop, xi, xip, R - t - f);
              A += (xop - yi) * (g - 2.0 * f);
              A += 0.5 * (xip - xop) * (g - 2.0 * f);
            }
            else if (yc)
            {
              double yop = sqrt(sqr(R - t - f) - yo*yo);
              double yip = sqrt(sqr(R - t - f) - yi*yi);
              A += SegArea(yip, yi, yop, yo, R - t - f);
              A += (yop - xi) * (g - 2.0 * f);
              A += 0.5 * (yip - yop) * (g - 2.0 * f);
            }
            else
            {
              double xip = sqrt(sqr(R - t - f) - xi*xi);
              double yip = sqrt(sqr(R - t - f) - yi*yi);
              A += SegArea(yip, yi, xi, xip, R - t - f);
              A += 0.5 * (yip - xi) * (xip - yi);
            }
          }
        }
      }
      P = 1.0 - A / totalA;
    }

    cout << "Case #" << n << ": " << P << endl;
  }

  return 0;
}

