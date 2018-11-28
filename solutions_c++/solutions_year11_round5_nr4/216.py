#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std ;
int main(int argc, char *argv[]) {
  int kase = 0 ;
  int N = 0 ;
  char buf[1000] ;
  char dig[1000] ;
  scanf("%d", &N) ;
  for (int kase=1; kase<=N; kase++) {
    long long lo=0, hi=0 ;
    long long knownlo=-1LL, knownhi=-1LL ;
    long long res = -1 ;
    scanf("%s", &buf) ;
    int len = strlen(buf) ;
    for (int i=0; i<len; i++) {
      dig[i] = buf[len-i-1] ;
      if (dig[i] == '?') {
	if (i >= 64) {
	  knownhi &= ~(1LL<<(i-64)) ;
	} else {
	  knownlo &= ~(1LL<<i) ;
	}
      }
      if (dig[i] == '1') {
	if (i >= 64) {
	  hi |= 1LL<<(i-64) ;
	} else {
	  lo |= 1LL<<i ;
	}
      }
    }
    int maxbits = (len + 1) >> 1 ;
    vector<long long> possib ;
    possib.push_back(0) ;
    for (int i=0; i<maxbits; i++) {
      vector<long long> npossib ;
      for (int j=0; j<possib.size(); j++) {
	long long p = possib[j] ;
	long long onebit = (1LL<<i) ;
	if (dig[i] == '?') {
	  npossib.push_back(p) ;
	  npossib.push_back(p+onebit) ;
	} else {
	  long long t = p * p ;
	  if (((t >> i) & 1) == dig[i]-'0')
	    npossib.push_back(p) ;
	  t = (p + onebit) * (p + onebit) ;
	  if (((t >> i) & 1) == dig[i]-'0')
	    npossib.push_back(p+onebit) ;
	}
      }
      possib = npossib ;
      /*
      cout << "At " << i << " value is " << possib.size() << endl ;
      for (int k=0; k<possib.size(); k++)
	cout << " " << possib[k] ;
      cout << endl ;
      */
    }
    long long mask = 0xfffffff ;
    long long finallo = -1 ;
    long long finalhi = -1 ;
    for (int i=0; i<possib.size(); i++) {
      long long p = possib[i] ;
      long long v1 = (p & mask) ;
      long long v2 = ((p >> 28) & mask) ;
      long long v3 = ((p >> 56) & mask) ;
      long long s1 = v1 * v1 ;
      long long c1 = (s1 >> 28) ;
      s1 &= mask ;
      long long s2 = 2 * v1 * v2 + c1 ;
      long long c2 = (s2 >> 28) ;
      s2 &= mask ;
      long long s3 = v2 * v2 + 2 * v1 * v3 + c2 ;
      long long c3 = (s3 >> 28) ;
      s3 &= mask ;
      long long s4 = 2 * v2 * v3 + c3 ;
      long long c4 = (s4 >> 28) ;
      s4 &= mask ;
      long long s5 = v3 * v3 + c4 ;
      long long lores = (s3 << 56) + (s2 << 28) + s1 ;
      long long hires = (s3 >> 8) + (s4 << 20) + (s5 << 48) ;
      /*
      cout << "Product of " << p << " is " << hires << " " << lores << endl ;
      cout << "Known " << hi << " " << lo << endl ;
      */
      if ((lo & knownlo) == (lores & knownlo) &&
	  (hi & knownhi) == (hires & knownhi)) {
	if (res < 0) {
	  finallo = lores ;
	  finalhi = hires ;
	  res = p ;
	} else
	  cout << "Oops " << res << " " << p << endl ;
      }
    }
    cout << "Case #" << kase << ": " ;
    for (int i=len-1; i>=0; i--) {
      if (i >= 64)
	cout << (1&(finalhi>>(i-64))) ;
      else
	cout << (1&(finallo>>i)) ;
    }
    cout << endl ;
  }
}
