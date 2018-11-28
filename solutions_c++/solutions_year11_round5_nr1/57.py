#include<cstdio>
#include<vector>
#include<complex>

using namespace std;

typedef complex<double> pt;
typedef vector<pt> polygon;

double cross(const pt& a, const pt& b)
{
  return imag(conj(a)*b);
}

double area(const polygon& p)
{
  double A = 0;
  for(int i=0; i<(int)p.size(); ++i)
    A += cross(p[i], p[(i+1)%p.size()]);
  return abs(A/2);
}

void solve()
{
  int W, L, U, G;
  int xl[128], yl[128], xu[128], yu[128];
  scanf("%d%d%d%d", &W, &L, &U, &G);

  for(int i=0; i<L; ++i)
    scanf("%d%d", &xl[i], &yl[i]);
  for(int i=0; i<U; ++i)
    scanf("%d%d", &xu[i], &yu[i]);

  polygon P;
  for(int i=0; i<L; ++i)
    P.push_back(pt(xl[i], yl[i]));
  for(int i=U-1; i>=0; --i)
    P.push_back(pt(xu[i], yu[i]));
  double A = area(P);

  for(int i=1; i<G; ++i) {
    double target = A / G * i;
    double lo = 0, hi = W;

    while(hi-lo > 1e-8) {
      double mid = (hi+lo) / 2;
      polygon Q;

      for(int j=0; j<L; ++j) {
	if(xl[j] > mid) {
	  Q.push_back(pt(mid, yl[j-1]+(mid-xl[j-1])*(yl[j]-yl[j-1])/(xl[j]-xl[j-1])));
	  break;
	}
	Q.push_back(pt(xl[j], yl[j]));
      }

      int iu;
      for(iu=0; iu<U; ++iu) {
	if(xu[iu] >= mid) {
	  Q.push_back(pt(mid, yu[iu-1]+(mid-xu[iu-1])*(yu[iu]-yu[iu-1])/(xu[iu]-xu[iu-1])));
	  break;
	}
      }
      for(iu--; iu>=0; --iu)
	Q.push_back(pt(xu[iu], yu[iu]));

      if(area(Q) < target)
	lo = mid;
      else
	hi = mid;
    }

    printf("%.7f\n", lo);
  }
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int C=1; C<=T; ++C) {
    printf("Case #%d:\n", C);
    solve();
  }
}
