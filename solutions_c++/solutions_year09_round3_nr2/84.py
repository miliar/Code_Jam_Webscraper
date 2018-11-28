#include<iostream>
#include<cmath>
#include<vector>
using namespace std;

vector<int> x, y, z, vx, vy, vz;

double dist_center(double t, vector<double> &out){
  int N = x.size();

  double xc = 0;
  double yc = 0;
  double zc = 0;
  for(int i = 0; i < N; i++){
    xc += (x[i] + t * vx[i]);
    yc += (y[i] + t * vy[i]);
    zc += (z[i] + t * vz[i]);
  }

  xc /= N;
  yc /= N;
  zc /= N;

  out.push_back(xc);
  out.push_back(yc);
  out.push_back(zc);
  return sqrt( xc * xc + yc * yc + zc * zc );
}

double sq(double x){return x * x;}

double dot(vector<double> a, vector<double> b) {
  double res = 0;
  for(int i = 0; i < 3; i++)
    res += a[i] * b[i];
  return res;
}

int main(){
  int T;
  cin >> T;
  for(int tno = 0; tno < T; tno++){
    int N;
    cin >> N;
    x.clear(); y.clear(); z.clear(); vx.clear(); vy.clear(); vz.clear();
    for(int i = 0; i < N; i++){
      int a,b,c,d,e,f;
      cin >> a >> b >> c >> d >> e >> f;
      x.push_back(a);
      y.push_back(b);
      z.push_back(c);
      vx.push_back(d);
      vy.push_back(e);
      vz.push_back(f);
    }

    vector<double> zero, one;
    dist_center(0, zero);
    dist_center(1, one);
    vector<double> d(3);
    for(int i = 0; i < 3; i++){
      d[i] = one[i] - zero[i];
    }


    double tmin, dmin;
    if( dot(d,d) < 1e-14 ) {
      tmin = 0;
    } else {
      vector<double> m(3);
      double t = -dot(zero, d) / dot(d, d);
      if( t < 0 ) tmin = 0;
      else tmin = t;
    }
    
    dmin = dist_center(tmin, one);
    printf("Case #%d:", tno + 1);
    printf(" %.8f %.8f\n", dmin, tmin);
  }
}
