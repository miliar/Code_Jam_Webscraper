#include <iostream>
#include <vector>
using namespace std;

bool prime[1001000];
vector<int> primes;

int main() {
  for (int i = 2; i <= 1000000; i++) prime[i] = true;
  for (int i = 2; i*i <= 1000000; i++) {
    if (!prime[i]) continue;
    for (int j = i*i; j <= 1000000; j+=i)
      prime[j] = false;
  }
  for (int i = 2; i <= 1000000; i++) if (prime[i]) { primes.push_back(i); }

  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    long long N; cin >> N;

    long long res = (N == 1 ? 0 : 1);
    for (int i = 0; i < primes.size(); i++) {
      long long p = primes[i];
      if (p*p > N) break;
      long long cur = p;
      while (cur*p <= N) {
        res++;
        cur *= p;
      }
    }
    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
