#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)

#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

#define eps (1e-6)

void dumpV(vector<int> v) {
  cout << "v{";
  REP(i, v.size()){
    cout << v[i] << " ";
  }
  cout << "}" << endl;
}

bool isMultiple(long long a, long long b) {
  if(a<b) return (b%a)==0;
  else return (a%b)==0;
}

void solve()
{
  long long N, L, H;
  cin >> N >> L >> H;
  vector<long long> other(N);
  REP(i, N) {
    cin >> other[i];
  }
  bool OK=true;
  FOR(i, L, H+1) {
    OK=true;
    REP(j, N) {
      if(!isMultiple(other[j], i)) {
        OK=false;
        break;
      }
    }
    if(OK) {
      cout << i;
      return;
    }
  }
  if(!OK) {
    cout << "NO";
  }
}

int main()
{
  int T;
  cin >> T;
  for(int i=0;i<T;i++) {
    cout << "Case #" << (i+1) << ": ";
    solve();
    cout << endl;
  }
}
