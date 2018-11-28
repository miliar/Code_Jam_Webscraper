#include <algorithm>
#include <cassert>
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

ll lx, ly;

/* Calcula mcd(a, b) y devuelve p y q tales que
 * a·p + b·q = mcd(a, b) >= 0 
 * a y b pueden ser negativos, pero no pueden ser 0 al mismo tiempo */
template<class ent>
ent euclides(ent a, ent b, ent &p, ent &q) {
  ent m, n, d;
  if (a < b) {
    swap(a, b);
    p = n = 0;
    q = m = 1;
  } else {
    q = m = 0;
    p = n = 1;
  }
  
  /* invariante: a >= b, mcd(a, b) = mcd(a inicial, b inicial)
   * y a = p * a inicial + q * b inicial,
   *   b = m * a inicial + n * b inicial */
  while (b != 0) {
    d = a / b;
    swap(a, b);
    swap(p, m);
    swap(q, n);
    b %= a;
    m = m - p * d;
    n = n - q * d;
  }

  if (a < 0) { p = -p; q = -q; a = -a; }
  return a;
}

bool solve(ll x1, ll y1, ll x2, ll y2, ll a, ll& x, ll& y) {
  a -= x1 * y2 - x2 * y1;
  ll q = x2 - x1, p = y1 - y2;
  // p·x3 + q·y3 = a, 0 <= x3 <= lx, 0 <= y3 <= ly
  for (x = 0; x <= lx; ++x)
    for (y = 0; y <= ly; ++y)
      if (p * x + q * y == a) 
        return true;
  return false;
}

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    ll x, y, a;
    scanf("%lli%lli%lli\n", &lx, &ly, &a);
    typedef pair<ll, ll> punto;
    vector<punto> borde;
    for (x = 0; x <= lx; ++x) {
      borde.push_back(punto(x, 0));
      borde.push_back(punto(x, ly));
    }
    for (y = 0; y <= ly; ++y) {
      borde.push_back(punto(0, y));
      borde.push_back(punto(lx, y));
    }
    sort(borde.begin(), borde.end());
    borde.erase(unique(borde.begin(), borde.end()), borde.end());

    int i, j, n = borde.size();
    bool posible = false;
    for (i = 0; i < n && !posible; ++i)
      for (j = i + 1; j < n && !posible; ++j) {
        ll x1 = borde[i].first, y1 = borde[i].second,
           x2 = borde[j].first, y2 = borde[j].second,
           x3, y3;
        if (solve(x1, y1, x2, y2, a, x, y) || solve(x1, y1, x2, y2, -a, x3, y3)) {
          posible = true;
          printf("%lli %lli %lli %lli %lli %lli\n", x1, y1, x2, y2, x3, y3);
          ll b = x2 * y3 - x3 * y2 - x1 * y3 + x3 * y1 + x1 * y2 - x2 * y1;
          assert(b == a || b == -a);
        }
      }
    if (!posible)
      puts("IMPOSSIBLE");
  }
  return 0;
}
