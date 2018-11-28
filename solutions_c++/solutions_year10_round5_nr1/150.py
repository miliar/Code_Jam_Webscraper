#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))

using namespace std;

const int maxp = 1000000;
const int maxk = 10;

long long x[maxk];
bool prime[maxp];

long long exp(long long a, int n, int p) {
  if (a == 0)
    return 0;

  if (n == 0)
    return 1;
  
  if (n % 2)
    return (a*exp(a, n-1, p)) % p;
  else {
    long long t = exp(a, n/2, p);
    return (t*t) % p;
  }
}

int main() {
  memset(prime, 1, sizeof(prime));
  prime[0] = prime[1] = false;
  for (int p = 2; p < maxp; p++)
    if (prime[p]) {
      for (int q = 2*p; q < maxp; q += p)
	prime[q] = false;
    }

  int T;
  cin >> T;
  for (int C = 1; C <= T; C++) {
    cout << "Case #" << C << ": ";

    int d, k;
    cin >> d >> k;
    REP(i, k)
      cin >> x[i];

    if (k == 1) {
      cout << "I don't know." << endl;
      continue;
    }
	

    if (x[1] == x[0]) {
      cout << x[0] << endl;
      continue;
    }

    if (k == 2) {
      cout << "I don't know." << endl;
      continue;
    }

    long long n = 1;
    REP(i, d)
      n *= 10;

    long long m = 0;
    REP(i, k)
      m = max(m, x[i]);

    set<long long> res;
    for (long long p = m+1; p < n; p++)
      if (prime[p]) {
	long long a = ((x[2]-x[1]+p) * exp(x[1]-x[0]+p, p-2, p)) % p;
	long long b = (x[1]-a*x[0]) % p;
	while (b < 0)
	  b += p;

	bool ok = true;
	for (int i = 1; i < k; i++)
	  if ((x[i]-a*x[i-1]-b) % p != 0) {
	    ok = false;
	    break;
	  }

	if (ok) 
	  res.insert((a*x[k-1]+b) % p);
      }

    if (res.size() == 0)
      cerr << "Prazno" << endl;

    if (res.size() == 1)
      cout << *res.begin() << endl;
    else
      cout << "I don't know." << endl;
  }
}
