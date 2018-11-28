#include <algorithm>
#include <assert.h>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ext/hash_map>
#include <ext/hash_set>
#include <fstream>
#include <iostream>
#include <sstream>
#include <numeric>
#include <limits>
#include <iomanip>
using namespace std;

namespace __gnu_cxx {
template<> struct hash< std::string > {
  size_t operator()( const std::string& x ) const {
    return hash< const char* >()( x.c_str() );
  }
};
}

using __gnu_cxx::hash_map;

#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define LL long long
#define LD long double
#define vi vector<int>
#define vl vector<LL>
#define vs vector<string>
#define vb vector<bool>
#define ii pair<int, int>
#define vii vector<ii>
#define SET(v, i) (v | (1 << i))
#define CLEAR(v, i) (v & (1 << i))
#define TOGGLE(v, i) (v ^ (1 << i))

template <typename T, template<typename ELEM, typename ALLOC=std::allocator<ELEM> > class Container>
void Print(const Container<T>& v, const string& delimeter = " ") {
  for (typename Container<T>::const_iterator it = v.begin(); it != v.end(); ++it) {
    cout << *it << delimeter;
  }

  cout << endl;
}

template <class T>
void Print(const T& v, const string& delimeter = "\n") {
  cout << v << delimeter;
}

string Solve(const vs& b) {
  int d1x = 0, d1o = 0, d1t = 0;
  int d2x = 0, d2o = 0, d2t = 0;
  int cnt_empty = 0;
  for (int i = 0; i < 4; ++i) {
    int hx = 0, ho = 0, ht = 0;
    int vx = 0, vo = 0, vt = 0;
    for (int j = 0; j < 4; ++j) {
      if (b[i][j] == 'X') ++hx;
      if (b[i][j] == 'O') ++ho;
      if (b[i][j] == 'T') ++ht;

      if (b[j][i] == 'X') ++vx;
      if (b[j][i] == 'O') ++vo;
      if (b[j][i] == 'T') ++vt;

      if (b[i][j] == '.') ++cnt_empty;
    }
    if (hx + ht == 4 || vx + vt == 4)
      return "X won";
    if (ho + ht == 4 || vo + vt == 4)
      return "O won";

    if (b[i][i] == 'X') ++d1x;
    if (b[i][i] == 'O') ++d1o;
    if (b[i][i] == 'T') ++d1t;

    if (b[i][3 - i] == 'X') ++d2x;
    if (b[i][3 - i] == 'O') ++d2o;
    if (b[i][3 - i] == 'T') ++d2t;
  }

  if (d1x + d1t == 4 || d2x + d2t == 4)
    return "X won";
  if (d1o + d1t == 4 || d2o + d2t == 4)
    return "O won";

  if (cnt_empty == 0) return "Draw";
  return "Game has not completed";
}

int main() {
  char ip[10];
  FILE* f = fopen("A-large.in", "r");
  FILE* out = fopen("test.txt", "w");
  int n;
  fgets(ip, 100, f);
  sscanf(ip, "%d", &n);
  for (int t = 1; t <= n; ++t) {
    vs b;
    for (int i = 0; i < 4; ++i) {
      fgets(ip, 100, f);
      b.push_back(ip);
    }
    //Print(b);
    fprintf(out, "Case #%d: %s\n", t, Solve(b).c_str());
    fgets(ip, 100, f);
  }
  fclose(out);
  fclose(f);
  return 0;
}
