#include <algorithm>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define repeat(n) for ( int repc = (n); repc > 0; --repc )
typedef long long int64;

char *bitsieve;
vector<int> primes;

inline bool isprime( int x ) { return x == 2 || x > 2 && (x & 1) && (bitsieve[x>>4] & (1 << ((x>>1)&7))); }
inline void _bs_set( int x ) { bitsieve[x>>4] |= 1 << ((x>>1)&7); }
inline void _bs_unset( int x ) { bitsieve[x>>4] &= ~(1 << ((x>>1)&7)); }

void init( int upto )
{
   int i, j;

   bitsieve = new char[upto/16 + 1];
   memset(bitsieve, upto/16+1, 0);
   for ( i=3; i<=upto; i+=2 ) _bs_set(i);

   for ( i=3; i*i<=upto; i+=2 )
      if ( isprime( i ) )
         for ( j=i*i; j<=upto; j+=i+i )
            _bs_unset( j );

   primes.push_back(2);
   for (i=3; i<=upto; i+=2) {
      if (isprime(i)) {
         primes.push_back(i);
      }
   }
}

inline int64 mod(int64 a, int p) {
   a %= p;
   if (a < 0) a += p;
   return a;
}

int64 power(int64 a, int n, int p) {
   if (n == 0) return 1%p;
   if (n%2 == 1) return mod(a*power(a, n-1, p), p);
   int64 x = power(a, n/2, p);
   return mod(x*x, p);
}

int64 mod_inv(int64 a, int p) {
   return mod(power(a, p-2, p), p);
}

int D, K;
vector<int64> S;

int calc() {
   bool found_consecutive = false;
   for (int i=1; i<K; ++i) {
      if (S[i-1] == S[i]) {
         found_consecutive = true;
      } else if (found_consecutive) {
         return -1;
      }
   }
   
   if (found_consecutive) {
      return S[K-1];
   }

   if (K <= 2) {
      return -1;
   }

   int
      minp = *max_element(S.begin(), S.end()) + 1,
      maxp = 1;
   repeat (D) maxp *= 10;

   int ans = -1;
   for (int j=0; j<(int)primes.size() && primes[j] <= maxp; ++j) {
      int P = primes[j];
      if (P < minp) {
         continue;
      }
      
      int64 A = mod((S[2]-S[1]) * mod_inv(S[1]-S[0], P), P);
      int64 B = mod(S[1] - A*S[0], P);
      bool ok = true;
      for (int i=2; i<K; ++i) {
         if (mod(A*S[i-1]+B, P) != S[i]) {
            ok = false;
            break;
         }
      }
               
      if (ok) {
         int x = mod(A*S[K-1]+B, P);
         if (ans != -1 && ans != x) {
            return -1;
         }
         ans = x;
      }
   }
   return ans;
}

int main(void) { 
   cin.sync_with_stdio(0);

   init(1000000);

   int CASES; cin >> CASES;
   for (int tt=1; tt<=CASES; ++tt) { // caret here
      cin >> D >> K;
      S.resize(K);
      for (int i=0; i<K; ++i) {
         cin >> S[i];
      }

      int ans = calc();
      cout << "Case #" << tt << ": ";
      if (ans == -1) {
         cout << "I don't know.";
      } else {
         cout << ans;
      }
      cout << "\n";
   }

   return 0;
} 
