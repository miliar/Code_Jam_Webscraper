// =====================================================================================
//   [ Filename    ]  pb.cpp
//   [ Description ]  
//   [ Created     ]  09/13/2009 05:19:39 PM CST
//   [ Author      ]  Jiunru Yang , yangjiunru [at] gmail.com, NTUEE
// =====================================================================================

#include <iostream>
#include <cmath>

using namespace std;

void solve(int caseNo)
{
   unsigned nFF;
   cin >> nFF;
   double t, d;
   double x, y, z, vx, vy, vz;
   x = 0;
   y = 0;
   z = 0;
   vx = 0;
   vy = 0;
   vz = 0;
   for (unsigned i = 0; i < nFF; ++i) {
      double xa, ya, za, vxa, vya, vza;
      cin >> xa >> ya >> za >> vxa >> vya >> vza;
      x += xa;
      y += ya;
      z += za;
      vx += vxa;
      vy += vya;
      vz += vza;
   }
   x /= (double)nFF;
   y /= (double)nFF;
   z /= (double)nFF;
   vx /= (double)nFF;
   vy /= (double)nFF;
   vz /= (double)nFF;
   //printf ("%lf %lf %lf %lf %lf %lf\n", x, y, z, vx, vy, vz);

   if (abs(vx) < 1e-9 && abs(vy) < 1e-9 && abs(vz) < 1e-9) {
      t = 0;
      d = sqrt(x*x+y*y+z*z);
   }
   else if ((x * vy == y * vx) && (z * vy == y * vz)) {
      if (x * vx > 0) { // t = 0
         t = 0;
         d = sqrt(x*x+y*y+z*z);
      }
      else { // d = 0
         d = 0;
         t = sqrt(x*x+y*y+z*z)/sqrt(vx*vx+vy*vy+vz*vz);
      }
   }
   else { // not parallel
      t = (0.0-(x*vx+y*vy+z*vz))/(vx*vx+vy*vy+vz*vz);
      if (t < 0) { // t = 0
         t = 0;
         d = sqrt(x*x+y*y+z*z);
      }
      else {
         double nx = x + t * vx;
         double ny = y + t * vy;
         double nz = z + t * vz;
         d = sqrt(nx*nx+ny*ny+nz*nz);
      }
   }

   cout << "Case #" << caseNo << ": ";

   printf ("%.8lf %.8lf\n", d, t);
}

int main()
{
   int T;
   cin >> T;
   for (int t = 1; t <= T; ++t)
      solve(t);
   return 0;
}
