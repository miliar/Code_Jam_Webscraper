#include <iostream>
#include <cmath>

double a, b, c;
int main()
{
  int K;
  std::cin >>K;
  for (int k = 1; k<=K; ++k)
  {
    int N;
    std::cin >> N;
    a = b = c = 0;
    double X, Y, Z, VX, VY, VZ;
    X = Y = Z = VX = VY = VZ = 0;
    for (int i = 0; i < N; ++i)
    {
      double x, y, z, vx, vy, vz;
      std::cin >> x >> y >> z >> vx >> vy >>vz;
//       x/=N;
//       y/=N;
//       z/=N;
//       vx/=N;
//       vy/=N;
//       vz/=N;
      X += x;
      Y += y;
      Z += z;
      VX += vx;
      VY += vy;
      VZ += vz;
    }
//     X/=N;
//     Y/=N;
//     Z/=N;
//     VX/=N;
//     VY/=N;
//     VZ/=N;
    a = VX*VX + VY*VY+VZ*VZ;
    b = 2*(X*VX + Y*VY + Z*VZ);
    c = (X*X + Y*Y+Z*Z);
      
    double min;
    if (fabs(a)<1e-17)
      min = 0;
    else
      min = -b/(2.*a);
    if (min <0)
    {
      //      std::cout << min << std::endl;
      min = 0;
    }
    std::cout.precision(8);
    std::cout.setf(std::ios::fixed);
    double val = (a*min*min + b*min  +c)/(N*N);
    std::cout << "Case #" << k << ": " << std::sqrt(val) << " " << min << std::endl;
  }
}
