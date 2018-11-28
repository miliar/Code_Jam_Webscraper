// Philip_PV

#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <ctime>
#include <memory.h>
//#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<double, double> pdd;
typedef pair<int, int> pii;

/*
#define x first
#define y second
//*/

inline int nextint() {
  int res = 0;
  int neg = 1;

  char c = 0; while (c != '-' && (c < '0' || c > '9')) c = getchar();
  if (c == '-') c = '0', neg = -1;
  while (c >= '0' && c <= '9') {
    res = res * 10 + c - '0';
    c = getchar();
  }
  return neg * res;
}

#ifdef _DEBUG
  #define dbg(x) { cerr << #x << " = " << x << endl; }
#else
  #define dbg(x) ;
#endif

#define forn(_i,_n) for (int _i = 0; _i < (int)(_n); ++_i)
#define mp make_pair

#define SIZE 1250000
bool np[SIZE];
vector<int> primes;

int main() {
  for (int i = 2; i < SIZE; i++) if (!np[i]) {
    primes.push_back(i);
    for (ll j = (ll)i * i; j < SIZE; j += i)
      np[j] = true;
  }
  cerr << primes.size() << endl;

  cout.precision(15);
  cout << fixed;

  int _T; cin >> _T;
  for (int _t = 1; _t <= _T; _t++) {
    cerr << _t << " ";

    cout << "Case #" << _t << ": ";

   ll n; cin >> n;

   int ans_max = 1, ans_min = 0;
   for (int i = 0; i < (int)primes.size() && primes[i] <= n; i++) {
     int p = primes[i];
     ll tmp = p;
     while (tmp <= n) tmp *= p, ans_max++;
     ans_min++;
   }
   if (n == 1) ans_min = 1;

   cout << (ans_max - ans_min) << endl;
  }

  return 0;
}
