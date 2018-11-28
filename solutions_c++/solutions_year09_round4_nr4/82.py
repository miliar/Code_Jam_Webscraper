#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int X[50], Y[50], R[50];

const double eps = 1e-9;

class vector
{
  public:
  double x, y;
  vector (double _x, double _y) : x(_x), y(_y){}
  vector operator +(vector o)
  {
    return vector (x + o.x, y+o.y);
  }
  vector operator -(vector o)
  {
    return vector (x - o.x, y-o.y);
  }
  double abs ()
  {
    return x*x+y*y;
  }
};

int main ()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
    cout.setf(ios::fixed,ios::floatfield);
    int n;
    cin >> n;
    int maxr = 0;
    for (int i = 0; i < n; i++)
    {
      cin >> X[i] >> Y[i] >> R[i];
      if (R[i] > maxr) maxr = R[i];
    }
    double l = maxr, r = 2000;
    while (r-l > .1e-5)
    {
      double m = (r+l)/2;
      __int64 can[1610][3] = {0};
      int z = 0;
      for (int i = 0; i < n; i++)
      {
        for (int j = i+1; j < n; j++)
        { 
          vector p1(X[i],Y[i]), p2(X[j],Y[j]);
          double a = m - R[i], b = m - R[j];
          vector v = p1 - p2;
          double d2 = v.abs();
          double d = sqrt(d2);
          if (d - eps > a + b) continue;
          double cosa = (b*b+d2-a*a)/(2*d*b);
          double sina;
          if (cosa*cosa < 1-eps) sina = sqrt(1-cosa*cosa);
          else sina = 0;
          vector u = v;
          v.x *= b * cosa / d;
          v.y *= b * cosa / d;
          vector p = p2 + v;
          u.x *= b * sina / d;
          u.y *= b * sina / d;
          vector v1(u.y,-u.x);
          vector v2(-u.y,u.x);
          vector p3 = p + v1, p4 = p + v2;
          z += 2;
          for (int k = 0; k < n; k++)
          {
            vector q(X[k],Y[k]);
            if (m + eps > sqrt((q-p3).abs())+R[k])
              can[z-2][k / 15] |= 1 << (k%15);
            if (m + eps > sqrt((q-p4).abs())+R[k])
              can[z-1][k / 15] |= 1 << (k%15);
          }
        }
          vector p1(X[i],Y[i]);
          z++;
          for (int k = 0; k < n; k++)
          {
            vector q(X[k],Y[k]);
            if (m + eps > sqrt((q-p1).abs())+R[k])
            {
              can[z-1][k / 15] |= 1 << (k%15);
            }
          }
      }
      bool ok = 0;
      for (int i = 0; (i < z) && !ok; i++)
      {
        for (int j = i; j < z; j++)
        {
          if (n < 15)
          {
            if ((can[i][0] | can[j][0]) != ((1 << n) - 1)) continue;
            ok = 1;
            break;
          }
          if ((can[i][0] | can[j][0]) != ((1 << 15) - 1)) continue;
          if (n < 30)
          {
            if ((can[i][1] | can[j][1]) != ((1 << (n-15)) - 1)) continue;
            ok = 1;
            break;
          }
          if ((can[i][1] | can[j][1]) != ((1 << 15) - 1)) continue;
          if ((can[i][2] | can[j][2]) != ((1 << (n-30)) - 1)) continue;
          ok = 1;
          break;
        }
      }
      if (ok) r = m;
      else l = m;
    }
    cout << r << endl;
  }
  return 0;
}