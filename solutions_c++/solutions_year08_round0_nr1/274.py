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
#define vector dvect

// END CUT HERE
typedef long long ll;
const int infinito = 1000000000;

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    map<string, int> nomserv;
    char cad[1000];

    printf("Case #%i: ", caso);
    int n;
    scanf("%i\n", &n);
    for (int i = 0; i < n; ++i) {
      gets(cad);
      nomserv[cad] = i;
    }

    int q, cambios = 0;
    scanf("%i\n", &q);
    set<int> s;
    while (q--) {
      gets(cad);
      if (nomserv.find(cad) == nomserv.end()) continue;
      int t;
      s.insert(t = nomserv[cad]);
      if (s.size() == n) {
        ++cambios;
        s.clear();
        s.insert(t);
      }
    }
    printf("%i\n", cambios);
  }
  return 0;
}
