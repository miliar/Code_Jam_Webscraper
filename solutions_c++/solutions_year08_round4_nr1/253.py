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
    cerr << *this << endl;throw
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
const int maxn = 16385;

int val[maxn];
bool camb[maxn];
int f[maxn][2];

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    int v, valroot, i;
    scanf("%i%i", &v, &valroot);
    for (i = 0; i < (v - 1) / 2; ++i) {
      int c;
      scanf("%i%i", &val[i + 1], &c);
      camb[i + 1] = c;
    }
    for (; i < v; ++i)
      scanf("%i", &val[i + 1]);
    int hojas = (v - 1) / 2 + 1;
    fill(&f[0][0], &f[v + 1][0], infinito);
    for (i = v; i >= hojas; --i)
      f[i][val[i]] = 0;
    for (i = hojas - 1; i > 0; --i)
      for (int tipo = 0; tipo < 2; ++tipo) // 1 es AND
        if (tipo == val[i] || camb[i])
          for (int a = 0; a < 2; ++a)
            for (int b = 0; b < 2; ++b) {
              int res = tipo ? (a && b) : (a || b),
                  cambios = f[2 * i][a] + f[2 * i + 1][b];
              if (tipo != val[i]) ++cambios;
              f[i][res] <?= cambios;
            }
    if (f[1][valroot] < infinito)
      printf("%i\n", f[1][valroot]);
    else
      puts("IMPOSSIBLE");
  }
  return 0;
}
