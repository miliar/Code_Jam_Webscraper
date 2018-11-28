#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
using namespace std;

fstream fin, fout;
int N;
double f, R, t, r, g;

double F(double x, double r)
{
       return r*r/2 * asin(x/r) + x/2 * sqrt(r*r - x*x);
}

double calcIntegral(double a, double b, double r, double c)
{
       return F(b,r) - F(a, r) - c*(b-a);       
}

double calcArea(double x1, double x2, double y1, double y2, double r)
{
       double s = 0;
       double r2 = r*r;
       
       double yLeft = sqrt(r2 - x1*x1);
       double yRight = sqrt(r2 - x2*x2);
       double xBottom = sqrt(r2 - y1*y1);
       double xTop = sqrt(r2 - y2*y2);
       
       if (y1 <= yLeft && yLeft <= y2)
       {
              if (x1 <= xBottom && xBottom <= x2)
              {
                   s = calcIntegral(x1, xBottom, r, y1);
              }
              else
              {
                  s = calcIntegral(x1, x2, r, y1);
              }
       }
       else if (x1 <= xTop && xTop <= x2)
       {
            if (y1 <= yRight && yRight <= y2)
            {
                   s = (xTop - x1) * (y2 - y1);
                   s += calcIntegral(xTop, x2, r, y1);
            }
            else
            {
                s = (xTop - x1) * (y2 - y1);
                s += calcIntegral(xTop, xBottom, r, y1);
            }
       }
       else if (x1*x1 + y1*y1 <= r*r)
       {
            s = (x2 - x1)*(y2 - y1);
       }
       else
       {
           s = 0;
       }
       
       return s;
}

double calculateP(double f, double R, double t, double r, double g)
{
       double p = 1;
       double myR = R - t - f;
       
       double s = 0;
       
       int i = 0, j;
       
       while (r + f + i*(g + 2*r) < myR)
       {
             j = 0;
             while (r + f + j*(g + 2*r) < myR)
             {
                 s = s + calcArea(r + f + i*(g + 2*r), r + g - f + i*(g + 2*r), r + f + j*(g + 2*r), r + g - f + j*(g + 2*r), myR);
                 j++;  
             }
             i++;
       }
       
       s = s*4;
       
       p = 1 - s / (3.14159265*R*R);
       
       return p;
}

int main()
{
    fin.open("input.txt", ios::in);
    fout.open("output.txt", ios::out);
    
    fin >> N;
    
    int k = 0;
    double p;
        
    while (k < N)
    {
          k++;
          fin >> f >> R >> t >> r >> g;
          
          p = calculateP(f, R, t, r, g);
          
          fout << resetiosflags(ios::fixed) << setprecision(1);
          fout << "Case #" << k <<": ";
          fout << setiosflags(ios::fixed) << setprecision(6);
          fout <<p << "\n";
    }

    //system("pause");
    
    return 0;
    
 
    
}
