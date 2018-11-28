#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct Pt
{
  double x;
  double y;
  double z;
};

struct Quad
{
  double n;
  double t;
  double t2;
};

struct FlyVec
{
  Pt start;
  Pt dir;
};

void dump_fv(FlyVec fv)
{
  cerr << "(" << fv.start.x << ", " << fv.start.y << ", " << fv.start.z << ") + (";
  cerr << fv.dir.x << ", " << fv.dir.y << ", " << fv.dir.x << ")*t" << endl;
}

int main()
{
  int T;
  cin >> T;
  
  for (int loop=0;loop<T;loop++)
  {
    int N;
    cin >> N;
    
    vector<FlyVec>  flies(N);
    
    for (int j=0;j<N;j++)
    {
      cin >> flies[j].start.x;
      cin >> flies[j].start.y;
      cin >> flies[j].start.z;
      
      cin >> flies[j].dir.x;
      cin >> flies[j].dir.y;
      cin >> flies[j].dir.z;
    }  
    FlyVec M;
    M.start.x=0; for (int i=0;i<N;i++){M.start.x += flies[i].start.x;} M.start.x /= N;
    M.start.y=0; for (int i=0;i<N;i++){M.start.y += flies[i].start.y;} M.start.y /= N;
    M.start.z=0; for (int i=0;i<N;i++){M.start.z += flies[i].start.z;} M.start.z /= N;
    
    M.dir.x=0; for (int i=0;i<N;i++){M.dir.x += flies[i].dir.x;} M.dir.x /= N;
    M.dir.y=0; for (int i=0;i<N;i++){M.dir.y += flies[i].dir.y;} M.dir.y /= N;
    M.dir.z=0; for (int i=0;i<N;i++){M.dir.z += flies[i].dir.z;} M.dir.z /= N;
    
    
//    cerr << "M is " ; dump_fv(M);
    
//    if (M.dir.x == 0 && M.dir.y == 0 && M
    
    Quad dt;
    dt.n = 0; dt.t = 0; dt.t2=0;
    
    dt.n = M.start.x*M.start.x + M.start.y*M.start.y + M.start.z*M.start.z;
    dt.t = M.start.x*M.dir.x*2 + M.start.y*M.dir.y*2 + M.start.z*M.dir.z*2;
    dt.t2 = M.dir.x*M.dir.x + M.dir.y*M.dir.y + M.dir.z*M.dir.z;
    
//    cerr << "dt is " << dt.t2 <<" * t^2   +   " << dt.t << " * t   +   " << dt.n << endl;
    
    double a = dt.t2;
    double minv,mint;
    if (a > 0) {
 //     cerr << "case 1" << endl;
      double h = dt.t/(-2*a);
      
      if (h < 0)
      {
//        cerr << "lt 0" << endl;
        mint = 0;
        minv = sqrt(M.start.x*M.start.x + M.start.y*M.start.y + M.start.z*M.start.z);
      }
      else
      {
//        cerr << "gt 0 " << h << endl;
       // cerr <<
//          cerr << "base of sqrt is " << dt.n + dt.t * h + dt.t2*h*h << endl;
          
          double bsq = dt.n + dt.t * h + dt.t2*h*h;
          if (bsq < 0 && bsq > -0.000000001)
          {
            bsq = 0;
          }
        minv = sqrt(bsq);
        mint = h;
      }
      
    }
    else {
      cerr << "case 2" << endl;
      mint = 0;
      minv = sqrt(M.start.x*M.start.x + M.start.y*M.start.y + M.start.z*M.start.z);
    }
    
    printf("Case #%d: %0.8f %0.8f\n", loop+1, minv, mint);
  }
}
