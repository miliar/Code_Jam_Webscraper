#include <iostream>
#include "math.h"
#include "stdio.h"

using namespace std;

double myabs( double n )
{
  if (n < 0)
    return -n;
  else
    return n;
}

double sqr (double x)
{
  return x * x;
}

int main()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    int N;
    cin >> N;

    double x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0;
    for (int j = 0; j < N; j++)
    {
      double x1, y1, z1, vx1, vy1, vz1;
      cin >> x1 >> y1 >> z1 >> vx1 >> vy1 >> vz1;
      x += x1;
      y += y1;
      z += z1;
      vx += vx1;
      vy += vy1;
      vz += vz1;
    }

    x /= N;
    y /= N;
    z /= N;
    vx /= N;
    vy /= N;
    vz /= N;

    double a = x * vx + y * vy + z * vz;
    double b = vx * vx + vy * vy + vz * vz;
    double t;

    cerr << i + 1 << " : " << a << b << endl;
    if (myabs(b) < 1e-100)
      t = 0;
    else
      t = - a / b;

    if (t < 0)
      t = 0;

    //printf( "Case #%d: %.7f %.7f\n", i + 1, (float) sqrt( b * t * t + 2 * a * t + x * x + y * y + z * z ), (float) t);
    printf( "Case #%d: %.7f %.7f\n", i + 1, (float) sqrt( sqr(x + vx * t) + sqr( y + vy * t ) + sqr( z + vz * t) ), (float) t);
  }

  return 0;
}

