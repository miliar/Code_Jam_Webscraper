#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int T;

int dsu[1000010][2];

void dsu_make(int a) {
  dsu[a][0] = a;
  dsu[a][1] = 0;
}

int dsu_find(int a) {
  return (dsu[a][0] == a) ? a : (dsu[a][0] = dsu_find(dsu[a][0]));
}

void dsu_union(int a, int b) {
  int aR = dsu_find(a), bR = dsu_find(b);
  if (dsu[aR][1] > dsu[bR][1]) dsu[bR][0] = aR;
  else if (dsu[aR][1] < dsu[bR][1]) dsu[aR][0] = bR;
  else if (aR != bR) dsu[bR][0] = aR, dsu[aR][1]++;
}

bool primes[1000010];

int main() {
  memset(primes, 0, sizeof primes);
  for (long long i = 2; i < 1000010; i++) {
    primes[i] = true;
    for (long long j = 2; j * j <= i && primes[i]; j++) if (i % j == 0) primes[i] = false;
  }

  cin >> T;
  for (int nn = 1; nn <= T; nn++) {
    long long A, B, p; cin >> A >> B >> p;
    for (long long i = A; i <= B; i++) dsu_make(i - A);

    for (long long i = p; i < 1000010; i++) if (primes[i]) {
      long long start = ((A + i  - 1) / i) * i;
      for (long long j = start + i; j <= B; j+= i)
        dsu_union(start - A, j - A);
    }

    set<int> s;
    for (long long i = 0; i <= B - A; i++) s.insert(dsu_find(i));

    cout << "Case #" << nn << ": " << s.size() << endl;
  }
  return 0;
}