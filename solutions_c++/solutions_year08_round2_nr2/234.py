#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define MAXVAL 10001

bool sieve[MAXVAL];
vector<int> allprimes;

void initprimes() {
  sieve[0] = true;
  sieve[1] = true;

  for (int i=2; i<MAXVAL; i++) {
    if (sieve[i]) continue;
    allprimes.push_back(i);
    int n = 2*i;
    while (n < MAXVAL) {
      sieve[n] = true;
      n += i;
    }
  }
}

void getprimes(int P, int B, vector<int> &primes) {
  for (int i=0; i<(int)allprimes.size(); i++) {
    int p = allprimes[i];
    if (p > B) break;
    if (p >= P) primes.push_back(p);
  }
}

bool shouldjoin(int a, int b, vector<int> &primes) {
  for (int i=0; i<(int)primes.size(); i++) {
    int p = primes[i];
    if ((a % p == 0) && (b % p == 0)) {
      return true;
    }
  }
  return false;
}

int getset(int i, vector<int> &parent) {
  while (parent[i] != i) i = parent[i];
  return i;
}

void dounion(int i, int j, vector<int> &parent) {
  i = getset(i, parent);
  j = getset(j, parent);
  parent[j] = i;
}

int main() {
  initprimes();

  int C;
  cin >> C;

  for (int casenum=1; casenum <= C; casenum++) {
    int A, B, P;
    cin >> A >> B >> P;

    vector<int> primes;
    getprimes(P, B, primes);

    int N = B+1-A;

    vector<int> parent(N);
    for (int i=0; i<N; i++) parent[i] = i;

    for (int i=0; i<N; i++) {
      for (int j=i+1; j<N; j++) {
	int a = A+i;
	int b = A+j;
	if (shouldjoin(a, b, primes)) {
	  dounion(i, j, parent);
	}
      }
    }
    
    vector<bool> alive(N);
    for (int i=0; i<N; i++) {
      int s = getset(i, parent);
      alive[s] = true;
    }

    int ans = 0;
    for (int i=0; i<N; i++) {
      if (alive[i]) ans++;
    }

    cout << "Case #" << casenum << ": " << ans << endl;
  }

  return 0;
}
