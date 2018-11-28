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
const int mod = 10007;

int f[128][128],
    dx[] = { 1, 2 },
    dy[] = { 2, 1 };

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    int lx, ly, rocks, i, j;
    scanf("%i%i%i", &ly, &lx, &rocks);
    memset(f, 0, sizeof(f));
    for (i = 0; i < rocks; ++i) {
      int a, b;
      scanf("%i%i", &a, &b);
      --a; --b;
      f[a][b] = -1;
    }

    for (i = ly - 1; i >= 0; --i)
      for (j = lx - 1; j >= 0; --j) if (f[i][j] == 0) {
        if (i == ly - 1 && j == lx - 1)
          f[i][j] = 1;
        else {
          for (int m = 0; m < 2; ++m) {
            int a = i + dy[m], b = j + dx[m];
            if (a < ly && b < lx && f[a][b] >= 0)
              f[i][j] = (f[i][j] + f[a][b]) % mod;
          }
        }
      }
    printf("%i\n", f[0][0]);

  }
  return 0;
}
