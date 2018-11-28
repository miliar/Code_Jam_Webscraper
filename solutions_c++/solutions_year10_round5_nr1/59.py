// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
// MODEXP expects: 0<number<2^31, 0<=power<2^63, 0<modulus<2^31
// MODEXP returns: (number^power) % modulus
long long MODEXP(long long number, long long power, long long modulus) { if (power==0) return 1LL % modulus; if (power==1) return number % modulus; long long tmp = MODEXP(number,power/2,modulus); tmp = (tmp*tmp) % modulus; if (power&1) tmp = (tmp*number) % modulus; return tmp; }
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

#define SIEVE_MAX 1234567
#define ISPRIME(n) (!(__sito[(n)>>4] & (1<<(((n)>>1)&7)))) /* only works for odd values */
unsigned char __sito[ (SIEVE_MAX>>4) + 47 ];
vector<int> primes(1,2); 

void do_sieve() {
  memset(__sito,0,sizeof(__sito));
  int __odm = int(3+sqrt(double(SIEVE_MAX)));
  for(int i=3;i<=__odm;i+=2) if(ISPRIME(i)) { 
    int j=i*i; while(j<SIEVE_MAX) { __sito[j>>4] |= 1 << ((j>>1)&7); j+=i<<1; }
  }
  for (int i=3; i<SIEVE_MAX; i+=2) if (ISPRIME(i)) primes.push_back(i);
}

int next(long long A, long long B, long long P, vector<int> &Z) {
  for (int i=1; i<SIZE(Z); ++i) {
    long long expected = (Z[i-1] * A + B) % P;
    if (expected != Z[i]) return -1;
  }
  return (Z[ SIZE(Z)-1 ] * A + B) % P;
}

int main() {
  do_sieve();
  int T;
  cin >> T;
  FOR(t,1,T) {
    int D, K;
    cin >> D >> K;
    vector<int> Z(K);
    REP(k,K) cin >> Z[k];
    if (K==1) {
      cout << "Case #" << t << ": I don't know." << endl;
      continue;
    }
    if (K==2) {
      if (Z[0]==Z[1]) {
        cout << "Case #" << t << ": " << Z[0] << endl;
      } else {
        cout << "Case #" << t << ": I don't know." << endl;
      }
      continue;
    }
    int limit = 1;
    REP(d,D) limit *= 10;
    int largest = *max_element( Z.begin(), Z.end() );
    set<int> candidates;
    REP(p,SIZE(primes)) {
      if (primes[p] > limit) break;
      if (primes[p] <= largest) continue;
      
      int c1 = next(0,Z[1],primes[p],Z);
      if (c1 != -1) candidates.insert(c1);

      long long diff1 = (Z[1] - Z[0] + primes[p]) % primes[p];
      int c2 = next(1,diff1,primes[p],Z);
      if (c2 != -1) candidates.insert(c2);

      if (primes[p] > 2) {
        long long invdiff1 = MODEXP(diff1,primes[p]-2,primes[p]);
        long long diff2 = (Z[2] - Z[1] + primes[p]) % primes[p];
        long long A = (diff2 * invdiff1) % primes[p];
        long long AS = (A * Z[0]) % primes[p];
        long long B = (Z[1] - AS) % primes[p];
        B = (B + primes[p]) % primes[p];
        int c3 = next(A,B,primes[p],Z);
        if (c3 != -1) candidates.insert(c3);
      }
    }
    if (SIZE(candidates)==1) {
      cout << "Case #" << t << ": " << *candidates.begin() << endl;
    } else {
      cout << "Case #" << t << ": I don't know." << endl;
    }
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
