#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const int mxprime = 100;

int primes[1 << 20];

int prime ( int a ){
  if ( a == 1 ) return 0;
  
  for ( int i = 2; i * i <= a; ++i )
      if ( a % i == 0 ) return 0;
    
    return 1;
}

int prime_power ( int a ){
  if ( a == 1 ) return 1;
  int br = 1;
  
  for ( int i = 2; i <= a; ++i )
      if ( prime ( i ) && a % i == 0 ) --br;
  
  return br == 0;
}

void find_primes ( ){
  primes[1] = 1;
  
  for ( long long i = 2; i <= ( 1 << 20 ); ++i )
      if ( !primes[i] )
	for ( long long j = i * i; j <= ( 1 << 20 ); j += i )
	  primes[j] = 1;
}
void solve(){
    long long N;
    int mn = 0, mx = 0;
    
    cin >> N;
    
    if ( N == 1 ) { cout << 0 << endl; return ;}
    int br = 0;
    
    for ( long long i = 1; i * i  <= N; ++i )
	if ( !primes [ i ] ){
	//  cout << i << endl;
	  long long tmp = i * i;
	  int tbr = 0;
	  while ( tmp <= N ) { tmp *= i; tbr++; }
	  
	  br += tbr;
	}
    
    cout << br + 1 << endl;
}

int main(){
  int tests;
  cin >> tests;
  find_primes();
  for ( int i = 1; i <= tests; ++i ){
    cout << "Case #" << i << ": ";
    solve();
  }
}