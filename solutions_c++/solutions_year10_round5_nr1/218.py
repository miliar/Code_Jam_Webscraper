#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;

const int MAX_SIZE = 1000000;

bool is_prime[MAX_SIZE];
vector<int> primes;

void init_primes() {
  memset(is_prime, true, sizeof(is_prime));
  is_prime[0] = is_prime[1] = false;
  for (int i = 2; i < MAX_SIZE; i++) {
    if (is_prime[i]) {
      primes.push_back(i);
      for (int j = i * 2; j < MAX_SIZE; j += i) {
        is_prime[j] = false;
      }
    }
  }
}

int extended_gcd(int a, int b, int& x, int& y) {
  if (a % b == 0) {
    x = 0;
    y = 1;
    return b;
  } else {
    int x2, y2;
    int d = extended_gcd(b, a % b, x2, y2);
    x = y2;
    y = x2 - y2 * (a / b);
    return d;
  }
}

int check(int p, const vector<int>& seq) {
  int d = seq[1] - seq[0];
  if (d < 0) d += p;
  int a, b;
  extended_gcd(d, p, a, b);
  a *= seq[2] - seq[1];
  a %= p;
  if (a < 0) a += p;
  b = seq[1] - seq[0] * a;
  b %= p;
  if (b < 0) b += p;
  int s = seq[0];
  for (int i = 1; i < seq.size(); i++) {
    s = (a * s + b) % p;
    if (s != seq[i]) {
      return -1;
    }
  }
  return (a * s + b) % p;
}

int main() {
  init_primes();
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int D, K;
    cin >> D >> K;
    int max_size = 1;
    for (int i = 0; i < D; i++) {
      max_size *= 10;
    }
    vector<int> seq;
    for (int i = 0; i < K; i++) {
      int num;
      cin >> num;
      seq.push_back(num);
    }
    int y = -1;
    if (K >= 2 && seq[0] == seq[1]) {
      y = seq[0];
      for (int i = 0; i < K; i++) {
        if (seq[i] != y) {
          y = -1;
          break;
        }
      }
    } else if (K > 2) {
      int m = *max_element(seq.begin(), seq.end());
      vector<int>::iterator it = upper_bound(primes.begin(), primes.end(), m);
      for (; it != primes.end(); ++it) {
        int p = *it;
        if (p > max_size) {
          break;
        }
        int x = check(p, seq);
        if (x != -1) {
          if (y == -1) {
            y = x;
          } else if (y != x) {
            y = -1;
            break;
          }
        }
      }
    }
    cout << "Case #" << t << ": ";
    if (y == -1) {
      cout << "I don't know.";
    } else {
      cout << y;
    }
    cout << endl;
  }
}
