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
const int infinito = 1000000000, tamano = 10000;

int f[tamano + 1];

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    int n, i, j, k;
    scanf("%i", &n);
    typedef pair<int, int> par; // inicio, fin (inclusive)
    vector< vector<par> > v;
    map<string, int> nomcol;
    for (i = 0; i < n; ++i) {
      string s;
      cin >> s;
      int a, b;
      scanf("%i%i", &a, &b);
      if (nomcol.find(s) == nomcol.end()) {
        int size = nomcol.size();
        nomcol[s] = size;
        v.push_back(vector<par>());
      }
      v[nomcol[s]].push_back(par(a - 1, b - 1));
    }

    int colors = nomcol.size(), ret = infinito;
    for (i = 0; i < colors; ++i)
      sort(v[i].begin(), v[i].end());

    bool vale = false;
    for (i = 0; i < colors; ++i)
      for (j = i; j < colors; ++j)
        for (k = j; k < colors; ++k) {
          vector<par> w(v[i]);
          if (i != j)
            copy(v[j].begin(), v[j].end(), back_inserter(w));
          if (i != k && j != k)
            copy(v[k].begin(), v[k].end(), back_inserter(w));
//          cout << w << endl;

          fill(&f[0], &f[tamano + 1], infinito);
          f[tamano] = 0;
          for (int pos = tamano - 1; pos >= 0; --pos)
            for (int p = 0; p < w.size(); ++p)
              if (w[p].first <= pos) {
                int sig = w[p].second + 1;
                if (sig > pos)
                  f[pos] = min(f[pos], f[sig] + 1);
              }
          if (f[0] < infinito) {
            vale = true;
            ret = min(ret, f[0]);
          }
        }


    if (vale)
      printf("%i\n", ret);
    else
      puts("IMPOSSIBLE");
    fflush(stdout);
  }
  return 0;
}
