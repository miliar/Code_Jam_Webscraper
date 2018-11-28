#include <iostream>
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <complex>
#include <iterator>
#include <memory>
#include <utility>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) make_pair((a), (b))
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;

ll gcd(ll a, ll b) {
  return a == 0 ? b : gcd(b % a, a);
}

int T;
string G;

const char kMap[26] = {
  'y', 'h', 'e', 's', 'o',
  'c', 'v', 'x', 'd', 'u',
  'i', 'g', 'l', 'b', 'k',
  'r', 'z', 't', 'n', 'w',
  'j', 'p', 'f', 'm', 'a',
  'q'
};

int main() {
  cin >> T;
  cin.ignore();
  for (int t = 1; t <= T; ++t) {
    getline(cin, G);
    for (int i = 0; i < G.size(); ++i) {
      if (G[i] == ' ') continue;
      G[i] = kMap[G[i] - 'a'];
    }
    printf("Case #%d: %s\n", t, G.c_str());
  }
}
