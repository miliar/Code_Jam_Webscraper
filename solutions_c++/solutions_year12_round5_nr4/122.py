#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define X first
#define Y second
#define PB push_back
#define FOR(x,y) for (int x = 0; x < int(y); ++x)
#define debug(x) cerr << #x << " = " << x << endl

typedef long long ll;
typedef long double ld;
typedef pair<int, int> P;
typedef vector<bool> Vb;
typedef vector<Vb> Mb;
typedef vector<char> Vc;
typedef vector<Vc> Mc;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<P> Vp;
typedef vector<Vp> Mp;
typedef vector<string> Vs;
typedef vector<Vs> Ms;

typedef queue<int> Q;
typedef priority_queue<int> PQ;
typedef stack<int> STACK;
typedef set<int> SET;
typedef SET::iterator Sit;
typedef map<int, int> MAP;
typedef MAP::iterator Mit;
typedef stringstream SS;

template <class Ta, class Tb> inline Tb cast(Ta a) { SS ss; ss << a; Tb b; ss >> b; return b; };

const double EPS = 1e-9;
const int INF = 1000000000;
const int MOD = 1000000007;
const int diri[8] = { -1, 0, 1, 0, -1, 1, 1, -1 };
const int dirj[8] = { 0, 1, 0, -1, 1, 1, -1, -1 };

char conv(char c) {
  if (c == 'o') return '0';
  if (c == 'i') return '1';
  if (c == 'e') return '3';
  if (c == 'a') return '4';
  if (c == 's') return '5';
  if (c == 't') return '7';
  if (c == 'b') return '8';
  if (c == 'g') return '9';
  return '-';
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int k;
    cin >> k;
    
    string s;
    cin >> s;
    
    Mi mat(128, Vi(128, 0));
    
    int n = s.size();
    for (int i = 0; i + 1 < n; ++i) {
      mat[int(s[i])][int(s[i + 1])] = 1;
      if (conv(s[i]) != '-') mat[int(conv(s[i]))][int(s[i + 1])] = 1;
      if (conv(s[i + 1]) != '-') mat[int(s[i])][int(conv(s[i + 1]))] = 1;
      if (conv(s[i]) != '-' and conv(s[i + 1]) != '-') mat[int(conv(s[i]))][int(conv(s[i + 1]))] = 1;
    }
    
    int res = 0;
    
    Vi in(128), out(128);
    for (int i = 0; i < 128; ++i)
      for (int j = 0; j < 128; ++j)
        if (mat[i][j]) {
          ++out[i];
          ++in[j];
          ++res;
        }
    
    int n1 = 0, n2 = 0;
    for (int i = 0; i < 128; ++i) {
      int t = in[i] - out[i];
      if (t < 0) n1 += -t;
      else if (t > 0) n2 += t;
    }
    
    res += max(0, max(n1, n2) - 1);
    
    cout << "Case #" << cas << ": " << res + 1 << endl;
  }
}
