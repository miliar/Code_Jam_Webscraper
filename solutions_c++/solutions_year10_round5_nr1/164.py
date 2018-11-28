#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <functional>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SZ(a) ((int)((a).size()))
#define REPSZ(i,v) REP(i,SZ(v))
#define ALL(a) (a).begin(),(a).end()
typedef long long Int;
template<class T> inline T sq(T x){return x * x;}
template<class T> inline void checkmin(T &a,T b){if(b<a)a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a)a=b;}

const int SIZE = 1000 * 1000 + 100;

vector<int> primes;
bool isPrime[SIZE];

void MakePrimes(){
  fill( &isPrime[0] , &isPrime[SIZE] , true);
  isPrime[0] = isPrime[1] = false;
  primes.clear();
  for(int i=2; i < SIZE; i++){
    if( isPrime[i] ){
      primes.push_back( i );
      if( i > SIZE / i )continue;
      for(int j=i*i; j < SIZE; j+=i)
        isPrime[j] = false;
    }
  }
}

Int modulo(Int x, Int mod) {
  return (x % mod + mod) % mod;
}

bool check(const vector<int> &v,int A, int P, int &out ) {
  int N = v.size();
  if( N < 2 ) return true;

  Int S = v[0];
  Int B = v[1] - A * S;
  B = modulo(B, P);

  bool ok = true;
  for(int i = 1; i < N; i++) {
    S = modulo( A * S + B, P );
    if( S != v[i] ) {
      ok = false;
      break;
    }
  }
  if( ok ) {
    out = modulo( A * S + B, P );
    return true;
  }
  return false;
}

void run() {
  int D, K;
  cin >> D >> K;

  vector<int> a;
  REP(i, K) {
    int x; cin >> x; a.push_back(x);
  }

  int lim = 1; REP(i, D) lim *= 10;
  int large = *max_element( ALL(a) );
  
  int ans = -1;
  for(int i = 0; primes[i] <= lim; i++) {
    if( primes[i] <= large ) continue;
    
    int out = -1;
    for(int A = 0; A < primes[i]; A++) { 
      if( check(a, A, primes[i], out) ) {
        if( ans == -1 || ans == out ) {
          ans = out;
        }
        else
        {
          cout << "I don't know." << endl;
          return;
        }
      }
    }
  }
  
  if( ans == -1 ) {
    cout << "I don't know." << endl;
  } else 
    cout << ans << endl;
}

int main() {
  MakePrimes();

  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    printf("Case #%d: ", tno);
    run();
  }
  return 0;
}
