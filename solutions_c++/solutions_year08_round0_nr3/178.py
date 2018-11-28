#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

double f, g, t, r, R, White;
const double PI = acos(-1.0);
struct Square
{
    double x1, x2, y1, y2;
};
Square sqr[1024][1024];

double dist(double x1, double y1, double x2, double y2)
{
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}
double xmult(double x1,double y1,double x2,double y2,double x0,double y0){
	return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);
}
double getS(double x1,double y1,double x2,double y2,double x3,double y3){
	return fabs(xmult(x1,y1,x2,y2,x3,y3))/2;
}
double Solve()
{
     if(g <= 2 * f) return 1.0;
     int i, j;
     int N = R / (g + r + r) + 2;
     //cout << N << endl;
     double len = g + r + r, td, d1, d2, ss = (g - f - f) * (g - f - f);
     double p1x, p1y, p2x, p2y, Total = R * R * PI;
     for(i = 0; i <= N; ++i)
     {
         for(j = 0; j <= N; ++j)
         {
              sqr[i][j].x1 = r + f + len * i;
              sqr[i][j].x2 = sqr[i][j].x1 + g - f - f;
              sqr[i][j].y1 = r + f + len * j;
              sqr[i][j].y2 = sqr[i][j].y1 + g - f - f;
         }
     }
     White = 0;
     R = R - f - t;
     for(i = 0; i <= N; ++i)
     {
         for(j = 0; j <= N; ++j)
         {
              if(dist(0, 0, sqr[i][j].x1, sqr[i][j].y1) >= R) continue;
              //printf("ASDASDASD");
              if(dist(0, 0, sqr[i][j].x2, sqr[i][j].y2) <= R) White += ss;
              else 
              {
                  d1 = dist(0, 0, sqr[i][j].x1, sqr[i][j].y2);
                  d2 = dist(0, 0, sqr[i][j].x2, sqr[i][j].y1);
                  if(d1 < R && d2 < R)
                  {
                        White += ss;
                        p1y = sqr[i][j].y2;
                        p1x = sqrt(R * R - p1y * p1y);
                        p2x = sqr[i][j].x2;
                        p2y = sqrt(R * R - p2x * p2x);
                        White -= (sqr[i][j].y2 - p2y) * (sqr[i][j].x2 - p1x) / 2;
                        White += PI * R * R / 2 / PI * (atan(p1y / p1x) - atan(p2y / p2x)) - getS(0, 0, p1x, p1y, p2x, p2y);
                  }
                  else if(d1 > R && d2 > R)
                  {
                        p1x = sqr[i][j].x1;
                        p1y = sqrt(R * R - p1x * p1x);
                        p2y = sqr[i][j].y1;
                        p2x = sqrt(R * R - p2y * p2y);
                        White += (p2x - sqr[i][j].x1) * (p1y - sqr[i][j].y1) / 2;
                        White += PI * R * R / 2 / PI * (atan(p1y / p1x) - atan(p2y / p2x)) - getS(0, 0, p1x, p1y, p2x, p2y);
                  }
                  else if(d1 < R && d2 > R)
                  {
                        p1y = sqr[i][j].y2;
                        p1x = sqrt(R * R - p1y * p1y);
                        p2y = sqr[i][j].y1;
                        p2x = sqrt(R * R - p2y * p2y);
                        White += (p1x - sqr[i][j].x1 + p2x - sqr[i][j].x1) * (g - f - f) / 2;
                        White += PI * R * R / 2 / PI * (atan(p1y / p1x) - atan(p2y / p2x)) - getS(0, 0, p1x, p1y, p2x, p2y);
                  }
                  else
                  {
                        p1x = sqr[i][j].x1;
                        p1y = sqrt(R * R - p1x * p1x);
                        p2x = sqr[i][j].x2;
                        p2y = sqrt(R * R - p2x * p2x);
                        White += (p1y - sqr[i][j].y1 + p2y - sqr[i][j].y1) * (g - f - f) / 2;
                        White += PI * R * R / 2 / PI * (atan(p1y / p1x) - atan(p2y / p2x)) - getS(0, 0, p1x, p1y, p2x, p2y);
                  }
              }
         }
     }
     //cout << White << " SS " << Total << endl;
     return 1 - (White * 4 / Total);
}

int main()
{
    
    int T, ctr;

    
    freopen("C_L.in", "r", stdin);
    freopen("C_L.out", "w", stdout);
    scanf("%d", &T);
    cout << fixed << setprecision(6);
    for(ctr = 1; ctr <= T; ++ctr)
    {
        cin >> f >> R >> t >> r >> g;
        cout << "Case #" << ctr << ": " << Solve() << endl;
    }
}
/*
10
0.25 1.0 0.1 0.01 0.5
0.25 1.0 0.1 0.01 0.9
0.00001 10000 0.00001 0.00001 1000
0.4 10000 0.00001 0.00001 700
1 100 1 1 10

*/
