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
// BEGIN CUT HERE
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

// END CUT HERE
typedef long long ll;
const int infinito = 1000000000;

struct tren {
  int tini, tfin, orig;
  tren(int a, int b, int c) : tini(a), tfin(b), orig(c) {}
  bool operator<(const tren& b) const {
    if (tini != b.tini) return tini < b.tini;
    if (tfin != b.tfin) return tfin < b.tfin;
    return orig < b.orig;
  }
};

int leehora() {
  int h, m;
  scanf("%d:%d", &h, &m);
  return 60 * h + m;
}

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    int na, nb, t;
    scanf("%i%i%i", &t, &na, &nb);

    vector<tren> v;
    for (int i = 0; i < na + nb; ++i) {
      int a = leehora(), b = leehora();
      v.push_back(tren(a, b, i >= na));
    }
    sort(v.begin(), v.end());
    priority_queue<int, vector<int>, greater<int> > cola[2];
    int ret[2] = { 0, 0 };
    for (int i = 0; i < v.size(); ++i) {
      int o = v[i].orig;
      if (cola[o].empty() || cola[o].top() > v[i].tini)
        ++ret[o];
      else
        cola[o].pop();
      cola[1 - o].push(v[i].tfin + t);
    }
    printf("%i %i\n", ret[0], ret[1]);
  }
  return 0;
}
