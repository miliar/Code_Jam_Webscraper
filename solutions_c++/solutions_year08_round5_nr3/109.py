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

int f[16][1024];
int broken[16];

bool vale[1024];
int maskoc[1024], unos[1024];

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    int ly, lx, y, x;
    scanf("%i%i", &ly, &lx);
    for (y = 0; y < ly; ++y) {
      broken[y] = 0;
      for (x = 0; x < lx; ++x)  {
        char c;
        scanf(" %c", &c);
        if (c == 'x')
          broken[y] |= 1 << x;
      }
    }
    for (int mask = 0; mask < (1 << lx); ++mask) {
      bool ult1 = false;
      int mc = 0;
      unos[mask] = 0;
      for (x = 0; x < lx; ++x)
        if (mask & (1 << x)) {
          if (ult1) break;
          ++unos[mask];
          if (x > 0) 
            mc |= 1 << (x - 1);
          if (x < lx - 1)
            mc |= 1 << (x + 1);
          ult1 = true;
        }
        else ult1 = false;
      vale[mask] = (x == lx);
      if (vale[mask])
        maskoc[mask] = mc;
    }
       
    fill(&f[0][0], &f[1][0], 0);
    for (y = 0; y < ly; ++y) {
      for (int mask = 0; mask < (1 << lx); ++mask) {
        f[y + 1][mask] = 0;
        int ocup = broken[y] | mask, quedan = ((1 << lx) - 1) & ~ocup;
        int m = quedan;
        for (;;) {
          if (vale[m])
            f[y + 1][mask] >?= f[y][maskoc[m]] + unos[m];
          if (!m) break;
          m = (m - 1) & quedan;
        }
      }
    }
    printf("%i\n", f[ly][0]);
  }
  return 0;
}
