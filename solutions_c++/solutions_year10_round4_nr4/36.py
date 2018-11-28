#include <iostream>
#include <iomanip>
#include <complex>
#include <vector>
#include <cassert>
using namespace std;

typedef complex<double> pt;

double calc(double l, double r0, double r1)
{
  double c=(r0*r0+l*l-r1*r1)/(2*r0*l);
  double t=acos(c)*2;
  return (r0*r0*t/2)-(r0*r0*sin(t)/2);
}

int main()
{
  cout<<setiosflags(ios::fixed)<<setprecision(12);

  int cases; cin>>cases;
  for (int c=1; c<=cases; c++){
    int n, m; cin>>n>>m;
    assert(n==2);

    vector<pt> ps(n);
    for (int i=0; i<n; i++){
      double x, y; cin>>x>>y;
      ps[i]=pt(x, y);
    }

    cout<<"Case #"<<c<<":";
    for (int i=0; i<m; i++){
      double x, y; cin>>x>>y;
      pt q(x, y);

      double r0=abs(ps[0]-q);
      double r1=abs(ps[1]-q);
      double l=abs(ps[0]-ps[1]);

      double area=0;
      if (l<(r0+r1)){
	area=calc(l, r0, r1)+calc(l, r1, r0);
      }

      cout<<" "<<area;
    }
    cout<<endl;
  }
  return 0;
}
