#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

const long long MAX = 1000000000000; // 10^12
const int SQRT_MAX = 1000000;

vector<char> bitsieve;
vector<int> primes;

inline bool isprime( int x ) { return x == 2 || x > 2 && (x & 1) && (bitsieve[x>>4] & (1 << ((x>>1)&7))); }
inline void _bs_set( int x ) { bitsieve[x>>4] |= 1 << ((x>>1)&7); }
inline void _bs_unset( int x ) { bitsieve[x>>4] &= ~(1 << ((x>>1)&7)); }

void sieve( int upto )
{
  int i, j;

  bitsieve.resize( upto / 16 + 1 );
  fill( bitsieve.begin(), bitsieve.end(), 0 );
  for ( i=3; i<=upto; i+=2 ) _bs_set(i);

  for ( i=3; i*i<=upto; i+=2 )
    if ( isprime( i ) )
      for ( j=i*i; j<=upto; j+=i+i )
        _bs_unset( j );

  primes.clear();
  primes.push_back(2);
  for (i=3; i<=upto; i+=2) {
    if (isprime(i)) {
      primes.push_back(i);
    }
  }
}

int main(void) {
  cin.sync_with_stdio(0);
  sieve(SQRT_MAX);

  vector<long long> ppowers;
  ppowers.push_back(1);
  for (int i=0; i<(int)primes.size(); ++i) {
    int p = primes[i];
    long long X = p;
    while (X <= MAX / p) {
      X *= p;
      ppowers.push_back(X);
    }
  }
  sort(ppowers.begin(), ppowers.end());

  int CASES; cin >> CASES;
  for (int tt=1; tt<=CASES; ++tt) { // caret here
    long long n, result;
    cin >> n;
    if (n == 1) {
      result = 0;
    } else {
      result = upper_bound(ppowers.begin(), ppowers.end(), n) - ppowers.begin();
    }
    cout << "Case #" << tt << ": " << result << "\n";
  }

  return 0;
}
