#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <cfloat>
#include <string>

typedef unsigned long long ull;

#define FOR(i,n) for (int i=0; i<(n); i++)
#define ALL(v) (v).begin(),(v).end()
#define PV(v) for (int __i=0; __i<(v).size(); __i++) cout << (v)[__i] << " "; cout << endl;

using namespace std;

#define SQ(x) ((x)*(x))

int main()
{
  int _N;
  cin >> _N;

  int N;
  double x,y,z,a,b,c;
  long long x0,y0,z0,a0,b0,c0;

  long long xi,yi,zi,ai,bi,ci;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> N;
      x=y=z=a=b=c=0.0;
      xi=yi=zi=ai=bi=ci=0;
      for (int i=0; i<N; i++)
	{
	  cin >> x0 >> y0 >> z0 >> a0 >> b0 >> c0;
	  xi+=x0;
	  yi+=y0;
	  zi+=z0;
	  ai+=a0;
	  bi+=b0;
	  ci+=c0;
	}
      x=double(xi)/double(N);
      y=double(yi)/double(N);
      z=double(zi)/double(N);
      a=double(ai)/double(N);
      b=double(bi)/double(N);
      c=double(ci)/double(N);

      if (a*a+b*b+c*c==0.0)
	cout << sqrt(x*x+y*y+z*z) << " " << 0.0 << endl;
      else
	{
	  double t=-(a*x+b*y+c*z)/(a*a+b*b+c*c);
	  //      cout << "t: " << t << endl;
	  //      printf("%lf %lf %lf\n",x,y,z);
	  cout.precision(10);
	  if (t<=0.0)
	    cout << sqrt(x*x+y*y+z*z) << " " << 0.0 << endl;
	  else
	    cout << sqrt(SQ(x+a*t)+SQ(y+b*t)+SQ(z+c*t)) << " " << t << endl;
	}
    }

  return 0;
}
