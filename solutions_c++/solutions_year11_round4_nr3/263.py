
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <cmath>
#include <complex>
#include <numeric>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,s) for(__typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) ((s).begin()), ((s).end())

typedef long long integer;

#define N 1234567LL

/** prime **/
bool isNotPrime[N];
int primes[N];
int nPrimes;
void init_primes() {
  isNotPrime[0] = isNotPrime[1] = true;
  REP(i, N){
    if(isNotPrime[i] == false){
      primes[nPrimes++] = i;
      for(int j = i + i; j < N; j += i)
	isNotPrime[j] = true;
    }
  }
}
bool isPrime(integer a) {
  if(a < N)
    return !isNotPrime[a];
  REP(i, nPrimes){
    int p = primes[i];
    if((integer)p * p > a)
      break;
    if(a % p == 0)
      return false;
  }
  return true;
}

integer border[N];
int main(void) {
  init_primes();
  cerr << nPrimes << endl;
  int nCases;
  cin >> nCases;
  
  int nBorders = 0;
  REP(i, nPrimes){
    integer p = primes[i];
    integer pp = p * p;
    while(pp < N*N){
      border[nBorders++] = pp;
      pp *= p;
    }
  }
  
  cerr << nBorders << endl;
  sort(border, border + nBorders);
  
//   for(int i = 1; i <= 20; ++i){
//     integer res = (upper_bound(border, border + nBorders, i) - border) + 1;
//     cerr << i << ": " << res << endl;
//   }
  
  REP(iCase, nCases) {
    integer n;
    cin >> n;
    integer res;
    if(n == 1){
      res = 0;
    }else{
      res = (upper_bound(border, border + nBorders, n) - border) + 1;
    }
    
    cout << "Case #" << (iCase+1) << ": " << res << endl;
  }
  
  return 0;
}
