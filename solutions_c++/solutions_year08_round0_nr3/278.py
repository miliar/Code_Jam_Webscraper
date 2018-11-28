#include <cassert>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;
using namespace __gnu_cxx;
#define foreach(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
template<class a,class b>
ostream& operator<<(ostream& os,pair<a,b> p) {os<<"("<<p.first<<","<<p.second<<")";return os;}
template<typename T>
ostream& operator<<(ostream& os, vector<T> vec) {os<<"{";foreach(i,vec) {os<<*i; if (i != --vec.end()) os<<",";}os<<"}";return os;}
template<typename T,typename _A=allocator<T> >
struct dvect: public vector<T,_A> { dvect(size_t n=0,const T& val=T()):vector<T,_A>(n,val) {}
  template<typename _InputIterator> dvect(_InputIterator f,_InputIterator l):vector<T,_A>(f,l) {}
  dvect(const vector<T, _A>& v) : vector<T, _A>(v) {}
  const T& operator[](int n) const throw();  T& operator[](int n) throw(); };
template<typename T,typename _A>
const T& dvect<T, _A>::operator[](int n) const throw() {
  try {return this->at(n);}
  catch(out_of_range e) {cerr << "Vector index out of bounds: "<<n<<endl;
    cerr<< " size: " << this->size()<< endl << " index: " << n << endl;
    cerr<<e.what()<<endl;
    cerr << *this << endl;
    throw;
  }
}
template<typename T,typename _A>
T& dvect<T, _A>::operator[](int n) throw(){
  return const_cast<T&>(const_cast<const dvect*>(this)->operator[](n));
}

const double pi = acos(-1.0);

double mod2(double x, double y) { return x * x + y * y; }

double arco(double x1, double y1, double x2, double y2, double r) {
  double ang = atan2(y2, x2) - atan2(y1, x1);
  assert(ang >= 0);
  return ang / 2 * r * r - fabs(x1 * y2 - x2 * y1) / 2;
}

double calc(double x1, double y1, double l, double r) {
  double r2 = r * r;
  double x2 = x1 + l, y2 = y1 + l;

  if (mod2(x1, y1) >= r2) return 0;
  if (mod2(x2, y2) <= r2) return l * l;

  if (mod2(x2, y1) >= r2) {
    if (mod2(x1, y1 + l) >= r2) {
      double a = sqrt(r2 - y1 * y1) - x1,
             b = sqrt(r2 - x1 * x1) - y1;
      return a * b / 2 + arco(x1 + a, y1, x1, y1 + b, r);
    } else {
      double a = sqrt(r2 - y1 * y1) - x1,
             b = sqrt(r2 - y2 * y2) - x1;
      return l / 2 * (a + b) + arco(x1 + a, y1, x1 + b, y2, r);
    }
  } else {
    if (mod2(x1, y2) >= r2) {
      double a = sqrt(r2 - x2 * x2) - y1,
             b = sqrt(r2 - x1 * x1) - y1;
      return l / 2 * (a + b) + arco(x2, y1 + a, x1, y1 + b, r);
    } else {
      double a = sqrt(r2 - x2 * x2) - y1,
             b = sqrt(r2 - y2 * y2) - x1;
      return 1.0 / 2 * (l * (a + b + l) - a * b) + arco(x2, y1 + a, x1 + b, y2, r);
    }
  }
}

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    double f, R, t, r, g;
    scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);

    double area = 0, areatotal = pi * R * R;
    double lado = g - 2 * f, s = R - t - f;
    if (lado > 0 && s > 0) {
      double d = g + 2 * r;
      for (int i = 0; r + d * i <= R - t; ++i)
        for (int j = 0; ; ++j) {
          double x1 = r + d * i + f, y1 = r + d * j + f;
          if (x1 * x1 + y1 * y1 >= s * s) break;
          area += calc(x1, y1, lado, s);
        }
    }
    printf("%lf\n", max(0.0, 1 - area * 4 / areatotal));
  }
  return 0;
}
