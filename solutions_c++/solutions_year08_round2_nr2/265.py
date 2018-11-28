#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream in("sets.in");
ofstream out("sets.out");

vector<int> primes;
long long a,b,p;
vector<bool> sieve,been;

void flood(long long x) {
  if (been[x-a]) {
    return;
  }
  been[x-a] = 1;
  for (int i = 0; i < primes.size(); i++) {
    if (x % primes[i] == 0) {
      long long y = a + (primes[i] - a%primes[i]);
      while (y <= b) {
	flood(y);
	y += primes[i];
      }
    }
  }
}

int main() {
  int C;
  in >> C;

  for (int casenum = 1; casenum <= C; casenum++) {
    in >> a >> b >> p;

    primes.clear();    
    sieve.clear();
    sieve.resize(b-a+1,1);
    for (int x = 2; x <= b-a; x++) {
      if (sieve[x]) {
	if (x >= p) {
	  primes.push_back(x);
	}
	for (int y = 2*x; y <= b-a; y += x) {
	  sieve[y] = 0;
	}
      }
    }
    
    been.clear();
    been.resize(b-a+1,0);

    int numcomponents = 0;
    
    for (long long x = a; x <= b; x++) {
      if (!been[x-a]) {
	flood(x);
	numcomponents++;
      }
    }

    out << "Case #" << casenum << ": " << numcomponents << endl;
  }
  return 0;
}
