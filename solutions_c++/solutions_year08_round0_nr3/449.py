#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

#define dd long double
#define forn(i,n) for(int i=0;i<(n);i++)

dd f, R, t, r, g;
dd radio;

inline dd area3(dd x1, dd y1, dd p1x, dd p1y, dd p2x, dd p2y)
{
    return 0.5 * abs(x1 * p1y + p1x * p2y + p2x * y1 -
                  x1 * p2y - p1x * y1  - p2x * p1y);
}

inline dd area4(dd x1, dd y1, dd x2, dd y2, dd x3, dd y3, dd x4, dd y4)
{
    return 0.5 * abs(x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 -
                     x1 * y4 - x2 * y1 - x3 * y2 - x4 * y3);
}

inline dd area5(dd x1, dd y1, dd x2, dd y2, dd x3, dd y3, dd x4, dd y4, dd x5, dd y5)
{
    return 0.5 * abs(x1 * y2 + x2 * y3 + x3 * y4 + x4 * y5 + x5 * y1 -
                     x1 * y5 - x2 * y1 - x3 * y2 - x4 * y3 - x5 * y4);
}


dd areaint(dd x1, dd y1, dd x2, dd y2)
{
      int cuenta = 0;
      cuenta += (x1 * x1 + y1 * y1 <= radio * radio);
      cuenta += (x1 * x1 + y2 * y2 <= radio * radio);
      cuenta += (x2 * x2 + y1 * y1 <= radio * radio);
      cuenta += (x2 * x2 + y2 * y2 <= radio * radio);
      dd p1x, p1y, p2x,p2y;
      dd area;
      switch (cuenta)
      {
             case 0:
                  return 0.0;
                  break;
             case 1:
                  p1x = x1;
                  p1y = sqrt(radio *radio - x1 * x1);
                  p2x = sqrt(radio *radio - y1 * y1);
                  p2y = y1;
                  area = area3(x1,y1,p1x,p1y,p2x,p2y);
                  break;
             case 2:
                  if (x2 * x2 + y1 * y1 <= radio * radio)
                  {
                         p1x = x1;
                         p1y = sqrt(radio * radio - x1 * x1);
                         p2x = x2;
                         p2y = sqrt(radio * radio - x2 * x2);
                         area = area4(x1,y1,p1x,p1y,p2x,p2y,x2,y1);
                  }
                  else
                  {
                         p1x = sqrt(radio * radio - y1 * y1);
                         p1y = y1;
                         p2x = sqrt(radio * radio - y2 * y2);
                         p2y = y2;
                         area = area4(x1,y1,p1x,p1y,p2x,p2y,x1,y2);
                  }
                  break;
             case 3:
                  p1x = x2;
                  p1y = sqrt(radio * radio - x2 * x2);
                  p2x = sqrt(radio * radio - y2 * y2);
                  p2y = y2;
                  area = area5(x1,y1,x2,y1,p1x,p1y,p2x,p2y,x1,y2);
                  break;
             case 4:
                  return (x2 - x1) * (y2 - y1);
                  break;
      }
      dd angulo = abs(acos((p1x * p2x + p1y * p2y) / sqrt((p1x * p1x + p1y * p1y)*(p2x  * p2x + p2y * p2y))));
      return area + 0.5 * angulo * radio * radio - area3(0,0,p1x,p1y,p2x,p2y);
}

int main()
{
    int n;
    cin >> n;
    dd pi = 2 * asin(1);
    forn(casos,n)
    {
      cin >> f >> R >> t >> r >> g;
      radio = R - t - f;
      dd x1,y1,x2,y2;
      x1 = r + f;
      y1 = r + f;
      x2 = r + g - f;
      y2 = r + g - f;
      int tope;
      for (tope = 1;x1 * x1 + y1 * y1 <= radio * radio;tope++)
      {
          x1 += g + 2 * r;
          x2 += g + 2 * r;
      }
      x1 = r + f;
      y1 = r + f;
      x2 = r + g - f;
      y2 = r + g - f;
      dd total = 0.0;
      forn(i,tope)
      forn(j,tope)
        total += areaint(x1 + i * (g + 2 * r),y1 + j * (g + 2 * r),x2 + i * (g + 2 * r),y2 + j * (g + 2 * r));
//      cout << "Case #" << casos+1 << ": " << 1 - (4 * total / (pi * R * R)) << endl;
      cout << "Case #" << casos+1 << ": ";
      printf("%0.15f\n",double(1 - (4 * total / (pi * R * R))));
    }
    return 0;
}
