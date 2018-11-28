#include <cmath>
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;
template <class T> inline T sqr(const T x) {return x*x;}
template <class T> inline void Swap(T &a, T &b)
{
    T tmp = a;
    a = b;
    b = tmp;
}

double GetIntegral(double r, double x)
{
    return 0.5*x*sqrt(r*r - x*x) + (r*r)/2 * asin(x/r);
}
double GetS(double x1, double x2, double r)
{
    return GetIntegral(r, x2) - GetIntegral(r, x1);
}

int main()
{
    ifstream in("input.txt", ios::in);
    ofstream out("output.txt", ios::out);
    int N, test;
    in >> N;
    
    for (test=1;test<=N;test++)
    {
        double f, R, t, r, g, res=-1, S=0, Square, x, y;
        in >> f >> R >> t >> r >> g;
        
        Square=sqr(g-2*f);
        
        if (2*f>=g) res=1;
        else
        {
            x=r;
            y=r;
            while(sqr(x+f)+sqr(y+f)<sqr(R-t-f) )
            {
                while(sqr(x+f)+sqr(y+f)<sqr(R-t-f) )
                {
                    double x1 = x + f, y1 = y + f, x2 = x + g - f, y2 = y + g - f;
                    bool ur = sqr(x2) + sqr(y2) <= sqr(R-t-f),
                         ul = sqr(x1) + sqr(y2) <= sqr(R-t-f),
                         dr = sqr(x2) + sqr(y1) <= sqr(R-t-f);
                    
                    
                    if (ur) S+=Square;
                    else
                    {
                        if (ul && dr)
                        {
                            double x3, y3;
                            x3 = sqrt(sqr(R-t-f) - sqr(y2));
                            y3 = sqrt(sqr(R-t-f) - sqr(x2) );
                            S+= (y2-y1)*(x3-x1) + GetS(x3, x2, R-t-f) - y1*(x2-x3);
                        }
                        else if (ul && !dr)
                        {
                            double x3, x4;
                            x3 = sqrt(sqr(R-t-f) - sqr(y2));
                            x4 = sqrt(sqr(R-t-f) - sqr(y1));
                            if (x3>x4) Swap(x3, x4);
                            S+= (y2-y1)*(x3-x1) + GetS(x3, x4, R-t-f) - y1*(x4-x3);
                        }
                        else if (!ul && dr)
                        {
                            /*double y3, y4;
                            y3 = sqrt(sqr(R-t-f) - sqr(x1));
                            y4 = sqrt(sqr(R-t-f) - sqr(x2));
                            if (y3>y4) Swap(y3, y4);*/
                            S+= GetS(x1, x2, R-t-f) - (x2-x1)*y1;
                        }
                        else // !ul && !dr
                        {
                             double x3;
                             x3 = sqrt(sqr(R-t-f) - sqr(y1));
                             S+= GetS(x1, x3, R-t-f) - (x3-x1)*y1;
                        }
                        
                    }
                    
                    x+=g+2*r;
                }
                y+=g+2*r;
                x=r;
            }
            res = 1 - 4*S/(M_PI*sqr(R) );
        }
        out << setiosflags(ios::fixed);
        out << "Case #" << test << ": " << setprecision(10) << res << endl;
    }
    
    in.close();
    out.close();
    
    return 0;
}
