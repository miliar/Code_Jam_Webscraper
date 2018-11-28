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

const int maxn = 2048;

bool mapa[maxn][maxn];
int dy[] = { 1, 0, -1, 0 },
    dx[] = { 0, -1, 0, 1 };
int minxb[maxn], maxxb[maxn], minyb[maxn], maxyb[maxn];

int main() {
  int casos;
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    int l, i, x = 0, y = 0;
    scanf("%i", &l);
    typedef pair<int, int> par;
    vector<par> v;
    v.push_back(par(x, y));
    vector<int> dirv;    
    int dir = 0, minx = 0, miny = 0, maxx = 0, maxy = 0;
    dirv.push_back(dir);
    for (i = 0; i < l; ++i) {
      int t;
      string s, r;
      cin >> s >> t;
      while (t--) r += s;
      for (int j = 0; j < r.size(); ++j) {
        if (r[j] == 'F') {
          x += dx[dir];
          y += dy[dir];
          v.push_back(par(x, y));
          minx <?= x;
          miny <?= y;
          maxx >?= x;
          maxy >?= y;
          dirv.push_back(dir);
        } else if (s[j] == 'L') dir = (dir + 1) % 4;
        else dir = (dir + 3) % 4;
      }
    }

    memset(mapa, 0, sizeof(mapa));
    for (i = 0; i < v.size(); ++i) {
      v[i].first -= minx;
      v[i].second -= miny;
      mapa[v[i].first][v[i].second] = true;
    }
    maxx -= minx;
    maxy -= miny;

    for (x = 0; x <= maxx; ++x)
      for (y = 0; y <= maxy; ++y) {
        minxb[y] = infinito; maxxb[y] = -1;
        minyb[x] = infinito; maxyb[x] = -1;
      }
    for (i = 0; i < v.size(); ++i) {
      x = v[i].first; y = v[i].second;
      bool cambio = i > 0 && dirv[i] != dirv[i - 1];
      if (dirv[i] % 2 == 1 || cambio) {
        minyb[x] <?= y; maxyb[x] >?= y;
      }
      if (dirv[i] % 2 == 0 || cambio) {
        minxb[y] <?= x; maxxb[y] >?= x;
      }
    }
    int res = 0;
    for (x = 0; x <= maxx - 1; ++x)
      for (y = 0; y <= maxy - 1; ++y)
        if (minxb[y] <= x && maxxb[y] > x /*&& minxb[y + 1] <= x && maxxb[y + 1] > x */||
            minyb[x] <= y && maxyb[x] > y /*&& minyb[x + 1] <= y && maxyb[x + 1] > y*/) {
          ++res;
        }
    ll area = 0;
    int n = v.size();
    for (i = 0; i < v.size() - 1; ++i) {
      ll x1 = v[i].first, y1 = v[i].second,
         x2 = v[i + 1].first, y2 = v[i + 1].second;
      area += x1 * y2 - x2 * y1;
    }
    if (area < 0) area = -area;
    res -= area / 2;
    printf("%i\n", res);
  }
  return 0;
}
