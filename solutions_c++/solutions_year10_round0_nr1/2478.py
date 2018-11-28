#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <utility>

using namespace std;

#define FOR(i,s,n) for (int i = (int)(s); i < (int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair

int power_of_two(int p)
{
  int ret = 1;
  REP(i, p) ret *= 2;
  return ret;
}

bool is_nbits_on(int N, int v)
{
  REP(i, N) {
    if (!(v & 1)) return false;
    v >>= 1;
  }
  return true;
}

int main()
{
  int T, N, K;

  cin >> T;
  REP(cs, T) {
    cin >> N >> K;
    
    int npow2 = power_of_two(N);
    while (K >= npow2) {
      K -= npow2;
    }

    cout << "Case #" << cs+1 << ": " << (is_nbits_on(N, K) ? "ON" : "OFF") << endl;
  }

  return 0;
}
