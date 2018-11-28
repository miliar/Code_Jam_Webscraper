#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "A"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

vector<int> tens;
vector<int> primes;
vector<bool> is_cons;
const int MAXN = 1000000;

int ppow(int a, int n, int p) {
  if (n == 0) {
    return 1 % p;
  } else if (n == 1) {
    return a % p;
  }
  int result = ppow(a, n / 2, p);
  if (n % 2) {
    return (((ll(result) * result) % p) * a) % p;
  } else {
    return (ll(result) * result) % p;
  }
}

int inverse(int x, int p) {
  if (x == 0) {
    cerr << "inverting 0" << endl;
    abort();
  }
  int t = ppow(x, (p - 2), p);
  if ((ll(t) * x) % p != 1) {
    cerr << "wrong inverse" << endl;
    abort();
  }
  return t;
}

int GetNextNumber(int S, int p, int A, int B) {
  return (ll(A) * S + B) % p;
}

bool Check(const vector<int>& S, int p, int A, int B) {
  for (int i = 0; i + 1 < S.size(); ++i) {
    if (GetNextNumber(S[i], p, A, B) != S[i + 1]) {
      return false;
    }
  }
  return true;
}

int GetNext(int d, const vector<int>& S) {
  if (S.size() == 1) {
    //cout << "only one element" << endl;
    return -1;
  }
  if (S.back() == S[(int)S.size() - 2]) {
    //cout << "two equal elements at the end" << endl;
    return S.back();
  }
  if (S.size() == 2) {
    //cout << "2 different elements" << endl;
    return -1;
  }
  int result = -1;
  int bestA, bestB, bestP;
  for (int prime_index = 0; prime_index < primes.size() && primes[prime_index] <= tens[d]; ++prime_index) {
    int p = primes[prime_index];
    bool good_prime = true;
    for (int i = 0; i < S.size(); ++i) {
      if (S[i] >= p) {
        good_prime = false;
        break;
      }
    }
    if (!good_prime) {
      continue;
    }
    for (int i = 0; i + 2 < S.size(); ++i) {
      if (S[i + 1] != S[i]) {
        int denominator = (S[i + 1] + p - S[i]) % p;
        int numerator = (ll(S[i + 1]) * S[i + 1] + p - ((ll(S[i]) * S[i + 2]) % p)) % p;
        int B = (ll(numerator) * inverse(denominator, p)) % p;
        int A;
        if (S[i] != 0) {
          A = (ll(S[i + 1] + p - B) * inverse(S[i], p)) % p;
        } else {
          A = (ll(S[i + 2] + p - B) * inverse(S[i + 1], p)) % p;
        }
        if (Check(S, p, A, B)) {
          if (result == -1) {
            result = GetNextNumber(S.back(), p, A, B);
            bestA = A;
            bestB = B;
            bestP = p;
          } else {
            int x = GetNextNumber(S.back(), p, A, B);
            if (x != result) {
              //cout << "possible " << result << " and " << x << endl;
              return -1;
            }
          }
        }
      }
    }
  }
  //cout << "A = " << bestA << ", B = " << bestB << ", p = " << bestP << endl;
  return result;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  tens.push_back(1);
  for (int i = 1; i <= 6; ++i) {
    tens.push_back(tens.back() * 10);
  }
  is_cons.assign(MAXN, false);
  for (int i = 2; i < MAXN; ++i) {
    if (!is_cons[i]) {
      primes.push_back(i);
      for (ll j = ll(i) * i; j < MAXN; j += i) {
        is_cons[j] = true;
      }
    }
  }
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int d, length;
    cin >> d >> length;
    vector<int> S(length);
    for (int i = 0; i < length; ++i) {
      cin >> S[i];
    }
    int result = GetNext(d, S);
    cout << "Case #" << test_index + 1 << ": ";
    cerr << "Case #" << test_index + 1 << ": ";
    if (result == -1) {
      cout << "I don't know." << endl;
    } else {
      cout << result << endl;
    }
  }
  return 0;
}
