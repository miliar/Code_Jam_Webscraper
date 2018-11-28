#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <ext/hash_map>
#include <ext/hash_set>
#include <fstream>
#include <iostream>
using namespace std;

namespace __gnu_cxx
{
        template<> struct hash< std::string >
        {
                size_t operator()( const std::string& x ) const
                {
                        return hash< const char* >()( x.c_str() );
                }
        };
}

using __gnu_cxx::hash_map;

#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()

const int INF = (1 << 31) - 1;

template <class T>
void print(const vector<T>& v) {
  for (int i = 0; i< sz(v); ++i)
    cout << v[i] << " ";
  cout << endl;
}

void print(const vector<string>& v) {
  for (int i = 0; i< sz(v); ++i)
    cout << v[i] << endl;
  cout << endl;
}

int Solve(const vector<int>& t, int s, int p) {
  int sure = 0, not_sure = 0;
  for (int i = 0; i < sz(t); ++i) {
    if (p > 1 && t[i] > 3 * (p - 2) + 1.5 && t[i] <= 3 * (p - 1)) {
      ++not_sure;
    } else if (t[i] > 3 * (p - 1)) {
      ++sure;
    }
  }
  return sure + min(s, not_sure);
}

int main() {
  int t;
  ifstream in("in.txt");
  ofstream out("out.txt");

  in >> t;
  for (int i = 1; i <= t; ++i) {
    int n, s, p;
    in >> n >> s >> p;
    vector<int> total;
    for (int j = 0; j < n; ++j) {
      int x;
      in >> x;
      total.push_back(x);
    }
    out << "Case #" << i << ": " << Solve(total, s, p) << endl;
  }

  in.close();
  out.close();
  return 0;
}


