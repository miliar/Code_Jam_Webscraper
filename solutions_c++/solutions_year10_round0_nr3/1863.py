#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL; 
typedef vector<int> VI; 
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS; 
typedef long double LD; 

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;} 
inline LL MIN(LL a, LL b){ return a < b ? a : b;} 

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

LL A[1050],S[1050];
int TT,N,pointer;
LL K,R;

//od do vratane
LL ps(int from, int to){
  return S[to] - S[from-1];
}

//vrati posledny index, ktory sa este zmesti do intervalu
int bsearch(int zaciatok, LL najviackolko){
  int hi = N;
  int lo = zaciatok-1;
  int m;
  while( hi - lo > 1){
    m = (hi + lo)/2;
    if ( ps(zaciatok,m) <= najviackolko){ lo = m; }
    else{ hi = m; }
  }
  if ( ps(zaciatok,hi) > najviackolko) return lo;
  return hi;
}

int main(){
  cin >> TT;
  FOR(tt,TT){
    cin >> R >> K >> N;
    FOR(i,N) cin >> A[i+1];
    S[0] = 0;
    FOR(i,N) S[i+1] = S[i] + A[i+1];
    if (S[N] <= K){
      cout << "Case #" << (tt+1) << ": " << R*S[N] << endl;
      continue;
    }
    pointer = 1;
    LL res = 0;
    FOR(i,R){
      int index;
      if ( ps(pointer,N) <= K){
        res += ps(pointer,N);
        index = bsearch(1,K-ps(pointer,N));
        res += ps(1,index);
        pointer = index+1;
      }else{
        index = bsearch(pointer,K);
        //if (index <= pointer) break;
        res += ps(pointer,index);
        pointer = index + 1;
      }
      if (pointer > N) pointer = 1;
    }
    cout << "Case #" << (tt+1) << ": " << res << endl;

  }
  return 0;
}
