#include <iostream>
//#include <string>
//#include <vector>
//#include <list>
//#include <algorithm>
#include <cmath>
using namespace std;
#define M_PI       3.14159265358979323846
//typedef unsigned long long tull;
//const int MAX = 100000;

long double dist(long double x, long double y)
{
  return sqrt(x*x+y*y);
}

int main() 
{
  freopen("C-small-attempt1.in", "rt", stdin);
  freopen("C-small-attempt1.out", "wt", stdout);
  int N;
  cin >> N;

  long double f,R,t,r,g;
  long double prob;
  long double l, fr, full_sq, step, x, y, cx1, cy1, cx2, cy2;
  long double ao, bo, ab, alfa, Ssec, Stri;
  bool fl1, fl2;

  for (int inn=0; inn<N; ++inn)
  {
    cin >> f >> R >> t >> r >> g;
    prob = 0;
    if (g < 2*f)
      cout << "Case #" << inn+1 << ": 0.0" << endl;
    else
    {
      x = r+f; y = r+f;
      step = g + 2*r;
      l = g - 2*f;
      full_sq = l*l;
      fr = R-t-f;
      while (x < fr)
      {
        y = r+f;
        while (y < fr)
        {
          if (dist(x,y)<fr)
          if (dist(x+l,y+l)<fr)
          {
            prob += full_sq;
          }
          else
          {
            if (dist(x,y+l)<fr)
            {//(1)
              cy1 = y+l;
              cx1 = sqrt(fr*fr - cy1*cy1);
              fl1 = true;
            }
            else
            {//(2)
              cx1 = x;
              cy1 = sqrt(fr*fr - cx1*cx1);
              fl1 = false;
            }

            if (dist(x+l,y) < fr)
            {//(3)
              cx2 = x+l;
              cy2 = sqrt(fr*fr - cx2*cx2);
              fl2 = true;
            }
            else
            {//(4)
              cy2 = y;
              cx2 = sqrt(fr*fr - cy2*cy2);
              fl2 = false;
            }

            if (fl1 && fl2) //(1)(3)
            {
              prob += l*(cx1-x) + (cy2-y)*(x+l-cx1) + (y+l-cy2)*(x+l-cx1)/2;
            }
            else if (fl1 && !fl2) //(1)(4)
            {
              prob += l*(cx1-x) + (cx2-cx1)*l/2;
            }
            else if (!fl1 && fl2) //(2)(3)
            {
              prob += l*(cy2-y) + (cy1-cy2)*l/2;
            }
            else if (!fl1 && !fl2)  //(2)(4)
            {
              prob += (cy1-y)*(cx2-x)/2;
            }

            
            ab = sqrt( (cx1-cx2)*(cx1-cx2) + (cy1-cy2)*(cy1-cy2) );

            alfa = acos ( (2*fr*fr - ab*ab)/(2*fr*fr) );
             
            //Ssec = ab*fr/2;
            Ssec = fr*fr*alfa/2;
            
            Stri = fr*fr*sin(double(alfa))/2;

            prob += (Ssec-Stri);

          }
          y += step;
        }
        x += step;
      }
      cout << "Case #" << inn+1 << ": " << 1-(4*prob)/(M_PI*R*R) << endl;
    }
  }
  return 0;
}
