#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");
void SolveCase();

typedef __int64 ll;
vector<ll> primes;

int main() {
  int ub = 60000;
  vector<bool> is_prime(ub, 0);
  for (int i = 2; i < ub; i++)
    for (int j = 2*i; j < ub; j += i)
      is_prime[j] = false;
  for (int i = 2; i < ub; i++)
    if (is_prime[i])
      primes.push_back(i);

  int N;
  in >> N;
  for (int tc = 1; tc <= N; tc++) {
    out << "Case #" << tc << ": ";
    SolveCase();
  }
  return 0;
}

void Gen(const vector<ll> &p, const vector<int> &pc, int pos, ll x, vector<ll> *result) {
  if (pos == p.size()) {
    result->push_back(x);
  } else {
    ll y = 1;
    for (int i = 0; i <= pc[pos]; i++) {
      Gen(p, pc, pos+1, x*y, result);
      y *= p[i];
    }
  }
}

vector<ll> Factor(ll n) {
  vector<ll> p;
  vector<int> pc;
  for (int i = 0; i < (int)primes.size(); i++)
  if (n % primes[i] == 0) {
    p.push_back(primes[i]);
    pc.push_back(0);
    while (n % primes[i] == 0) {
      pc[pc.size() - 1]++;
      n /= primes[i];
    }
  }
  if (n > 1) {
    p.push_back(n);
    pc.push_back(1);
  }
  vector<ll> result;
  Gen(p, pc, 0, 1, &result);
  return result;
}

void SolveCase() {
  int N, M, A;
  in >> N >> M >> A;
  cout << A << endl;
  bool success = false;
  for (ll x = 0; x <= N; x++)
  for (ll y = 0; y <= M; y++) {
    ll diff = x*y - A;
    if (diff < 0) continue;
    vector<ll> factors = Factor(diff);
    for (int i = 0; i < (int)factors.size(); i++) {
      if (factors[i] <= N && diff/factors[i] <= M) {
        ll a = x;
        ll b = (diff/factors[i]);
        ll c = factors[i];
        ll d = y;
        cout << (a*d - b*c) << " " << A << endl;
        out << "0 0 " << a << " " << b << " " << c << " " << d << endl;
        goto done;
      }
    }
  }
  out << "IMPOSSIBLE" << endl;
done:;
}
