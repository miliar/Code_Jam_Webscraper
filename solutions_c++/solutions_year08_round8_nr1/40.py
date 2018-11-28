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
#define vector dvect

typedef long long ll;
const int infinito = 1000000000;
const double eps = 1e-11;

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    ll x1[3], y1[3], x2[3], y2[3], i;
    for (i = 0; i < 3; ++i)
      scanf("%lli%lli", &x1[i], &y1[i]);
    for (i = 0; i < 3; ++i)
      scanf("%lli%lli", &x2[i], &y2[i]);
    int perm[3];
    for (i = 0; i < 3; ++i)
      perm[i] = i;
    bool vale = false;
    double xsol, ysol;
    do {
      ll xa = x1[0] - x2[perm[0]], xb = x1[1] - x2[perm[1]], xc = x1[2] - x2[perm[2]];
      ll ya = y1[0] - y2[perm[0]], yb = y1[1] - y2[perm[1]], yc = y1[2] - y2[perm[2]];
      // solve a*xa + b*xb + c*xc = 0,
      //       a*ya + b*yb + c*yc = 0,
      //       a + b + c = 1
      ll rx = -xc, ry = -yc;
      xa -= xc; xb -= xc;
      ya -= yc; yb -= yc;
      ll det = xa * yb - xb * ya;
      if (det == 0) {
        continue;
      } else {
        double a = (double)(rx * yb - ry * xb) / det;
        double b = (double)(xa * ry - ya * rx) / det;
        double c = 1 - a - b;
//        if (a < -eps || b < -eps || c < -eps) continue;

        vale = true;
        xsol = a * x1[0] + b * x1[1] + c * x1[2];
        ysol = a * y1[0] + b * y1[1] + c * y1[2];
        break;
      }
    } while (next_permutation(&perm[0], &perm[3]));
    if (!vale)
      puts("No Solution");
    else
      printf("%lf %lf\n", xsol, ysol);
    fflush(stdout);
  }
  return 0;
}
