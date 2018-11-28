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
template<class T>void pv(T a,T b){for(T i=a;i!=b;++i)cerr<<*i<<" ";cout<<endl;}
template<class T> inline T sq(T x){return x * x;}
template<class T> inline void checkmin(T &a,T b){if(b<a)a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a)a=b;}


const int SIZE = 1024 * 1024;
       
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
map<int, int> factorize(int n){
  map<int, int> res;
  for(int d=2; d*d <= n ; d++ ){
    while( n % d == 0 ){
      ++res[d];
      n /= d;
    }
  }
  if(n > 1) ++res[n];
  ++res[1];
  return res;
}

Int solve() {
  Int N; cin >> N;
  if (N == 1)
    return 0;
  map <int ,int> have;
  Int hi = 0;
  for (int n = 1; n <= N; n++) {
    map<int,int> need = factorize(n);

    bool call = false;
    for (map<int,int>::iterator it = need.begin(); it != need.end(); ++it) {
      if (have[ it->first ] < it->second) {
        have[ it->first ] = it->second;
        call = true;
      }
    }
    if (call)
      hi++;
  }
    
  vector<int> sp;
  for (int n = N; n >= 1; n--) {
    map<int,int> need = factorize(n);
    for (map<int,int>::iterator it = need.begin(); it != need.end(); ++it) {
      bool check = false;
      if (it->first != 1 && have[ it->first ] == it->second) {
        check = true;
        have[it->first]++;
      }
      if (check) {
        if (n * 2 > N)
          sp.push_back(n);
      }
    }
  }

//   pv(ALL(sp));
  reverse(ALL(sp));
  have.clear();
  Int lo = 0;
  for (int i = 0; i < (int)sp.size(); i++) {
    int n = sp[i];

    map<int,int> need = factorize(n);

    bool call = false;
    for (map<int,int>::iterator it = need.begin(); it != need.end(); ++it) {
      if (have[ it->first ] < it->second) {
        have[ it->first ] = it->second;
        call = true;
      }
    }
    if (call)
      lo++;    
  }
  
  return hi - lo;
}

int main() {
  MakePrimes();
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    
    printf("Case #%d: ", tno);
    cout << solve() << endl;

  }
  return 0;
}
