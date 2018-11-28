#include<iostream>
#include<string.h>
#include<math.h>

using namespace std;

#define double long double

double pos[20000][4];
int n;
int w;

double cost(int i, double x, double y, double z)
{
  return (fabs(x-pos[i][0]) + fabs(y-pos[i][1]) + fabs(z-pos[i][2])) / pos[i][3];
}

double cost(double x, double y, double z)
{
  double res = 0.0, a;
  int i;
  for (i=0; i<n; i++) {
    a = cost(i, x, y, z);
    if (a>res)
      res = a, w=i;
  }
  return res;
}

int solve()
{
  int i,j,k;
  double ll,rr,l,r,x,y,z;
  cin >> n;
  for (i=0; i<n; i++) {
    for (j=0; j<4; j++) cin >> pos[i][j];
  }

  x=y=z=0.0;

  double eps = 1e5;
  while (eps>1e-14) {
    for (k=0; k<30; k++) {
      cost(x, y, z);
      if (pos[w][0]<x) x-=eps; else x+=eps;
      if (pos[w][1]<y) y-=eps; else y+=eps;
      if (pos[w][2]<z) z-=eps; else z+=eps;
    }
    eps/=10.0;
  }

/*
  l=0; 
  r=1e6;
  while (r-l>1e-8) {
    ll=(l*2+r)/3.0;
    rr=(l+r*2)/3.0;
    if (cost(ll, 0, 0)<cost(rr, 0, 0)) r=rr;
    else l=ll;    
  }
  x = (l+r)/2.0;

  l=0; 
  r=1e6;
  while (r-l>1e-8) {
    ll=(l*2+r)/3.0;
    rr=(l+r*2)/3.0;
    if (cost(x, ll, 0)<cost(x, rr, 0)) r=rr;
    else l=ll;    
  }
  y = (l+r)/2.0;

  l=0; 
  r=1e6;
  while (r-l>1e-8) {
    ll=(l*2+r)/3.0;
    rr=(l+r*2)/3.0;
    if (cost(x, y, ll)<cost(x, y, rr)) r=rr;
    else l=ll;    
  }
  z = (l+r)/2.0;
*/
  cout << cost(x, y, z) +1e-9 << endl;

  return 0;
}

main()
{
  cout.precision(6);
  cout.setf(ios::fixed);

  int t, c=0;
  cin >> t;
  while (t--) {
    cout << "Case #" << ++c << ": ";
    solve();
  }
  return 0;
}
