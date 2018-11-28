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

int calc(ll x, ll y) {
  return (x % 3) * 3 + (y % 3);
}

void decalc(int a, ll* x, ll* y) {
  *x = a / 3;
  *y = a % 3;
}

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    ll n;
    ll A, B, C, D, x0, y0, M;
    scanf("%lli%lli%lli%lli%lli%lli%lli%lli", &n, &A, &B, &C, &D, &x0, &y0, &M);
    typedef pair<ll, ll> par;
    vector<par> p;
    p.push_back(par(x0, y0));
    for (ll i = 1; i < n; ++i) {
      x0 = (A * x0 + B) % M;
      y0 = (C * y0 + D) % M;
      p.push_back(par(x0, y0));
    }
    sort(p.begin(), p.end());
    p.erase(unique(p.begin(), p.end()), p.end());
    n = p.size();

    ll num[9];
    fill(&num[0], &num[9], 0);
    for (int i = 0; i < n; ++i)
      ++num[calc(p[i].first, p[i].second)];

    ll res = 0;
    for (int a = 0; a < 9; ++a)
      for (int b = a; b < 9; ++b)
        for (int c = b; c < 9; ++c) {
          ll x[3], y[3];
          decalc(a, &x[0], &y[0]);
          decalc(b, &x[1], &y[1]);
          decalc(c, &x[2], &y[2]);
          if ((x[0] + x[1] + x[2]) % 3 == 0 &&
              (y[0] + y[1] + y[2]) % 3 == 0) {
            ll total;
            if (a == c)
              total = num[a] * (num[a] - 1) * (num[a] - 2) / 6;
            else if (a == b)
              total = num[a] * (num[a] - 1) * num[b] / 2;
            else if (b == c)
              total = num[a] * num[b] * (num[b] - 1) / 2;
            else
              total = num[a] * num[b] * num[c];
            res += total;
          }
        }
    printf("%lli\n", res);
  }
  return 0;
}
