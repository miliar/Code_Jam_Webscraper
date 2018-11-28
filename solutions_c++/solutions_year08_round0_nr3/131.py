#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)
const double PI = 3.141592653589793238462643383279502884197;

double f, R, t, r, g, dziura, pr, gg, prpr;

bool wKole(double x, double y)
{ return x*x+y*y<=pr*pr;
}

double odc(double x1, double y1, double x2, double y2)
{ double o=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
  double a=2*asin((o/2)/pr);
  return (prpr*a-prpr*sin(a))/2;
}

int main()
{
  int n;
  cin>>n;
  cout<<fixed;
  for (int ca=1; ca<=n; ++ca)
  {
    dziura=0;
    cin>>f>>R>>t>>r>>g;
    r+=f;
    g-=2*f;
    gg=g*g;
    pr=R-t-f;
    prpr=pr*pr;
    if (g>0)
    { for (int ile=3+pr/(g+2*r), x=0; x<ile; ++x)
      { double x1=r+x*(g+2*r), x2=x1+g;
        for (int y=0; y<ile; ++y)
        { double y1=r+y*(g+2*r), y2=y1+g;
          if (wKole(x2, y2))
          { dziura+=gg;
            continue;
          }
          if (!wKole(x1, y1)) break;
          if (wKole(x2, y1) && wKole(x1, y2))
          {//1
            double xx=sqrt(prpr-y2*y2), yy=sqrt(prpr-x2*x2);
            dziura+=gg-(x2-xx)*(y2-yy)/2+odc(xx, y2, x2, yy);
            continue;
          }
          if (wKole(x1, y2))
          {//2
            double xx1=sqrt(prpr-y1*y1), xx2=sqrt(prpr-y2*y2);
            dziura+=g*(xx1+xx2-x1*2)/2+odc(xx2, y2, xx1, y1);
            continue;
          }
          if (wKole(x2, y1))
          {//3
            double yy1=sqrt(prpr-x1*x1), yy2=sqrt(prpr-x2*x2);
            dziura+=g*(yy1+yy2-y1*2)/2+odc(x1, yy1, x2, yy2);
            continue;
          }
          //4
          double xx=sqrt(prpr-y1*y1), yy=sqrt(prpr-x1*x1);
          dziura+=(xx-x1)*(yy-y1)/2+odc(x1, yy, xx, y1);       
        }
      }    
    } 
    cout<<endl<<"Case #"<<ca<<": "<<setprecision(6)<<(1-4*dziura/(PI*R*R))<<endl;
  }

  char ccccc;
  cin>>ccccc;

  return 0;
}
