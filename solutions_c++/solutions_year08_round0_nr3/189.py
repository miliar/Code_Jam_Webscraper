#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

const double PI = acos(-1.0);


double xmult(double xa,double ya,double xb,double yb,double x0,double y0){
	return (xa-x0)*(yb-y0)-(xb-x0)*(ya-y0);
}
double distance(double xa, double ya, double xb, double yb)
{
    return sqrt((xa - xb) * (xa - xb) + (ya - yb) * (ya - yb));
}

double Tri(double xa,double ya,double xb,double yb,double x3,double y3){
	return fabs(xmult(xa,ya,xb,yb,x3,y3))/2;
}



double f, g, t, r, R, w;

struct Square
{
    double xa, xb, ya, yb;
};
Square A[1024][1024];


double Solve()
{
     if(g <= 2 * f) return 1.0;



     int N = R / (g + r + r) + 2;
     int i, j;
     double len = g + r + r, d1, d2, ss = (g - f - f) * (g - f - f);
     double p1x, p1y, p2x, p2y;
	 double ta = R * R * PI;
     for(i = 0; i <= N; ++i)
     {
         for(j = 0; j <= N; ++j)
         {
              A[i][j].xa = r + f + len * i;
              A[i][j].xb = A[i][j].xa + g - f - f;
              A[i][j].ya = r + f + len * j;
              A[i][j].yb = A[i][j].ya + g - f - f;
         }
     }
     w = 0;
     R = R - f - t;

     for(i = 0; i <= N; ++i)
     {
         for(j = 0; j <= N; ++j)
         {
              if(distance(0, 0, A[i][j].xa, A[i][j].ya) >= R) continue;
     
              if(distance(0, 0, A[i][j].xb, A[i][j].yb) <= R) w += ss;
              else 
              {
                  d1 = distance(0, 0, A[i][j].xa, A[i][j].yb);
                  d2 = distance(0, 0, A[i][j].xb, A[i][j].ya);
                  if(d1 < R && d2 < R)
                  {
                        w += ss;
                        p1y = A[i][j].yb;
                        p1x = sqrt(R * R - p1y * p1y);
                        p2x = A[i][j].xb;
                        p2y = sqrt(R * R - p2x * p2x);
                        w -= (A[i][j].yb - p2y) * (A[i][j].xb - p1x) / 2;
                        w += PI * R * R / 2 / PI * (atan(p1y / p1x) - atan(p2y / p2x)) - Tri(0, 0, p1x, p1y, p2x, p2y);
                  }
                  else if(d1 > R && d2 > R)
                  {
                        p1x = A[i][j].xa;
                        p1y = sqrt(R * R - p1x * p1x);
                        p2y = A[i][j].ya;
                        p2x = sqrt(R * R - p2y * p2y);
                        w += (p2x - A[i][j].xa) * (p1y - A[i][j].ya) / 2;
                        w += PI * R * R / 2 / PI * (atan(p1y / p1x) - atan(p2y / p2x)) - Tri(0, 0, p1x, p1y, p2x, p2y);
                  }
                  else if(d1 < R && d2 > R)
                  {
                        p1y = A[i][j].yb;
                        p1x = sqrt(R * R - p1y * p1y);
                        p2y = A[i][j].ya;
                        p2x = sqrt(R * R - p2y * p2y);
                        w += (p1x - A[i][j].xa + p2x - A[i][j].xa) * (g - f - f) / 2;
                        w += PI * R * R / 2 / PI * (atan(p1y / p1x) - atan(p2y / p2x)) - Tri(0, 0, p1x, p1y, p2x, p2y);
                  }
                  else
                  {
                        p1x = A[i][j].xa;
                        p1y = sqrt(R * R - p1x * p1x);
                        p2x = A[i][j].xb;
                        p2y = sqrt(R * R - p2x * p2x);
                        w += (p1y - A[i][j].ya + p2y - A[i][j].ya) * (g - f - f) / 2;
                        w += PI * R * R / 2 / PI * (atan(p1y / p1x) - atan(p2y / p2x)) - Tri(0, 0, p1x, p1y, p2x, p2y);
                  }
              }
         }
     }
    
     return 1 - (w * 4 / ta);
}

int main()
{
   
    int T, n;

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

    cin >> T;
	n = 0;
	cout << fixed << setprecision(6);
    while (T--)
    {
		n++;
        cin >> f >> R >> t >> r >> g;

        cout << "Case #" << n << ": " << Solve() << endl;
    }
}
